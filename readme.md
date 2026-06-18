# ECTASK2

ECTASK2 is a documentation-first project for smart home network assessment deliverables.
The workspace contains report drafts/finals, Mermaid network diagrams, naming governance scripts, and archived source/export artifacts.

## Project Goals

- Maintain one clear active draft and one submission-ready report.
- Keep naming consistent with snake_case and status suffixes.
- Keep root directory minimal and easy to navigate.
- Archive generated exports and historical files outside root.

## Root Files (Active)

- `index.md`: entry page and active links.
- `project_guidelines.md`: naming, structure, and report formatting rules.
- `report_draft.md`: active report editing target.
- `report_final.md`: formatted submission-oriented report.
- `assessment_task2_report_final.md`: final optimized submission content.
- `network_diagrams.md`: Mermaid diagram showcase page.
- `smart_home_network_diagram*.mmd`: active Mermaid source variants.

## Directory Layout

- `scripts/`: utility scripts (naming audit, data conversion).
- `sheets_md/`: cleaned or source tabular markdown exports.
- `PIC/`: photo/image assets.
- `archive/`: historical, superseded, and generated output artifacts.
- `archive/diagram_exports/`: exported diagram png/jpg files.

## Naming and File Management

Follow `project_guidelines.md`:

- Use lowercase `snake_case`.
- Use status suffixes: `draft`, `final`, `orig`, `formatted`, `archive`.
- Do not place temporary exports or backup files in root.
- Keep `index.md` and `_sidebar.md` links synchronized with actual files.

## Maintenance Commands

Run naming audit:

```bash
python3 scripts/naming_audit.py --root . --write-report naming_audit_report.md
```

After renaming or moving files:

1. Re-run the naming audit.
2. Fix broken links in `index.md` and `_sidebar.md`.
3. Verify root only contains active files.

## Notes

- Mermaid source files are the canonical diagram source of truth.
- Export images are archived under `archive/diagram_exports/`.
