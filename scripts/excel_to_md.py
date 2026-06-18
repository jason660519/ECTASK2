import os
import re
import zipfile
import xml.etree.ElementTree as ET

INPUT_FILE = 'AllDevicesHome.xlsx'
OUT_DIR = 'sheets_md'

os.makedirs(OUT_DIR, exist_ok=True)

def safe_filename(s: str) -> str:
    return re.sub(r'[^0-9A-Za-z_\-]', '_', s).strip('_') or 'sheet'

def parse_shared_strings(zf):
    try:
        data = zf.read('xl/sharedStrings.xml')
    except KeyError:
        return []
    root = ET.fromstring(data)
    namespace = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
    strings = []
    for si in root.findall(f'.//{namespace}si'):
        texts = [t.text or '' for t in si.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')]
        strings.append(''.join(texts))
    return strings

def get_sheets(zf):
    # map rId -> target from workbook rels
    rels = {}
    try:
        rels_xml = zf.read('xl/_rels/workbook.xml.rels')
        root = ET.fromstring(rels_xml)
        for rel in root.findall('.//{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
            rid = rel.attrib.get('Id')
            target = rel.attrib.get('Target')
            rels[rid] = target
    except KeyError:
        rels = {}

    wb_xml = zf.read('xl/workbook.xml')
    root = ET.fromstring(wb_xml)
    ns = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
    sheets = []
    for s in root.findall(f'.//{ns}sheet'):
        name = s.attrib.get('name')
        rid = s.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
        target = rels.get(rid)
        if target and target.startswith('worksheets/'):
            sheets.append((name, 'xl/' + target))
    return sheets

def col_letter_to_index(col):
    idx = 0
    for c in col:
        idx = idx * 26 + (ord(c.upper()) - ord('A') + 1)
    return idx - 1

def read_sheet(zf, sheet_path, shared_strings):
    data = zf.read(sheet_path)
    root = ET.fromstring(data)
    ns = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
    rows = []
    for row in root.findall(f'.//{ns}row'):
        # determine max column in this row
        cells = {}
        max_col = -1
        for c in row.findall(f'{ns}c'):
            r = c.attrib.get('r')  # e.g., A1
            if r is None:
                continue
            col = ''.join([ch for ch in r if ch.isalpha()])
            idx = col_letter_to_index(col)
            if idx > max_col:
                max_col = idx
            value = ''
            t = c.attrib.get('t')
            v = c.find(f'{ns}v')
            if t == 's' and v is not None:
                ss_idx = int(v.text)
                value = shared_strings[ss_idx] if ss_idx < len(shared_strings) else ''
            elif v is not None and v.text is not None:
                value = v.text
            else:
                # inlineStr
                is_elem = c.find(f'{ns}is')
                if is_elem is not None:
                    t_elem = is_elem.find(f'{ns}t')
                    if t_elem is not None and t_elem.text is not None:
                        value = t_elem.text
            cells[idx] = value
        if max_col == -1:
            rows.append([])
        else:
            row_list = [cells.get(i, '') for i in range(max_col+1)]
            rows.append(row_list)
    return rows

with zipfile.ZipFile(INPUT_FILE, 'r') as zf:
    shared_strings = parse_shared_strings(zf)
    sheets = get_sheets(zf)
    count = 0
    for sheet_name, sheet_path in sheets:
        rows = read_sheet(zf, sheet_path, shared_strings)
        safe_name = safe_filename(sheet_name)
        out_path = os.path.join(OUT_DIR, f"{safe_name}_orig.md")
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(f"# {sheet_name}\n\n")
            if not rows:
                f.write('\n')
                continue
            header = [str(c) for c in rows[0]]
            f.write('| ' + ' | '.join(header) + ' |\n')
            f.write('| ' + ' | '.join(['---'] * len(header)) + ' |\n')
            for r in rows[1:]:
                cells = [str(c) for c in r]
                cells = [c.replace('\n', ' ').replace('|', '\\|') for c in cells]
                f.write('| ' + ' | '.join(cells) + ' |\n')
        count += 1
    print(f'Wrote {count} markdown files to {OUT_DIR}')
