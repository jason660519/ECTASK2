# ECTASK2 Project Guidelines

## Purpose

This document establishes naming conventions, file management rules, and document formatting standards for the ECTASK2 project. The goal is to ensure new files are predictable, searchable, and maintainable while establishing clear formatting requirements for final deliverables.

## Part 1: Naming Conventions

### Principle 1: Lowercase English with Underscores

- Use `snake_case` for all new filenames.
- Do not introduce `CamelCase`, title case, or mixed English-Chinese filenames.
- Historical filenames may be retained for reference but should not be used for new files.

### Principle 2: Filename Structure

Filenames should convey both content and status:

**Pattern:** `topic_purpose_status.extension`

**Examples:**
- `report_draft.md`
- `report_final.md`
- `smart_home_network_diagram_simple.mmd`
- `smart_home_network_diagram_segmented.mmd`

### Principle 3: Fixed Status Suffixes

Use only the following status indicators:

- `draft`: Work in progress, actively being modified.
- `final`: Ready for submission or external use.
- `orig`: Original export file, unmodified source content.
- `formatted`: Content is stable; differences are mainly in layout or presentation.
- `archive`: No longer actively edited but retained for reference.

**Do not use:** `new`, `latest`, `fixed`, `use_this`, `v2_final_final`, etc.

## Part 2: File Management

### File Roles in This Project

- `index.md`: Project entry point; contains only active links and brief navigation.
- `project_guidelines.md`: Source document for assignment and formatting requirements.
- `report_draft.md`: Main working document for the report.
- `report_final.md`: Finalized report ready for submission.
- `assessment_task2_report_final.docx`: Word format deliverable.
- `smart_home_network_diagram*.mmd`: Multiple diagram variants on the same topic.
- `archive/diagram_exports/`: Exported diagram images (png/jpg), not edited directly.
- `scripts/excel_to_md.py`: Data transformation tools.
- `sheets_md/`: External data export directory.
- `archive/`: Historical drafts, raw exports, and original source files that should not stay in the root.

### Root Directory

**Keep only:**
- Project entry: `index.md`
- Requirements/standards: e.g., `project_guidelines.md`
- Main report: e.g., `report_draft.md`
- Final deliverable: e.g., `report_final.md`
- Word export: e.g., `assessment_task2_report_final.docx`
- Core diagrams: e.g., `smart_home_network_diagram.mmd`
- Active working draft: `report_draft.md`

**Avoid placing in root:**
- Temporary exports
- Test files
- Scattered backups of the same content
- Unnamed screenshots or attachments
- Raw Pages or office source exports that are no longer the active editing source
- Historical drafts that are not the current working version
- Exported images generated from Mermaid source files

**Explicit root exceptions:**
- `.nojekyll` may remain in root when the project is published through GitHub Pages and needs that marker.

### Root Cleanliness Enforcement

- Root should stay focused on active navigation and current working files only.
- Generated artifacts must be placed in dedicated folders (for this project: `archive/diagram_exports/` for diagram image exports).
- If a file has no active link from `index.md` or `_sidebar.md`, move it to `archive/` unless it is currently being edited.
- After each batch export or rename operation, perform a root cleanup pass before finalizing work.

### scripts/ Directory

**Rules:**
- Script names use verb-based or conversion-intent naming.
- One script = one purpose.
- Experimental one-time scripts should be deleted or archived after completion, not left in the main workflow.

**Acceptable styles:**
- `excel_to_md.py`
- `md_cleanup.py`
- `generate_report_assets.py`

### sheets_md/ Directory

**Rules:**
- Retain original exports with the `orig` suffix.
- Include language codes at the end if multiple versions exist: e.g., `_en`.
- Move processed and ready-to-use versions to the main file area, or explicitly label them with `clean` or `summary`.

**Suggested format:**
- `topic_orig.md`
- `topic_orig_en.md`
- `topic_clean.md`
- `topic_clean_en.md`

### Mermaid Diagram Naming

Maintain consistent variant suffixes for diagram files:

**Recommended pattern:**
- `smart_home_network_diagram.mmd`: Main version.
- `smart_home_network_diagram_simple.mmd`: Simplified variant.
- `smart_home_network_diagram_segmented.mmd`: Segmented or divided variant.
- `smart_home_network_diagram_by_rooms.mmd`: Room-based configuration variant.

**Rules for new diagrams:**
- Use the same prefix for related diagrams.
- Describe variants only in the suffix; do not change the topic name.
- Match the source filename when exporting to images.

**Example:**
- Source: `smart_home_network_diagram_simple.mmd`
- Export: `smart_home_network_diagram_simple.jpg`

### Markdown Document Naming

#### Report Files
- Active draft: `report_draft.md`
- Ready for submission: `report_final.md`

#### Specification Files
- Assignment requirements: `assignment_requirements.md`
- Formatting standards: `project_guidelines.md`

Use precise specification names; avoid generic terms like `Requirements.md`.

#### Navigation Files
- Project entry is always: `index.md`
- Additional overview pages: `project_overview.md` (not `homepage.md`, `main_page.md`, etc.)

### Word / Export File Naming

- Use lowercase English and underscores.
- For final submissions, use `*_final` or `*_submission` to indicate purpose.

**Examples:**
- `assessment_task2_report_final.docx`
- `report_submission.docx`

### Legacy Source Files and Archives

- Keep the active editable source in the canonical root filename, such as `report_draft.md`.
- Move one-off office source exports, raw captures, and superseded working copies into `archive/`.
- Rename archived source files to lowercase snake_case where possible.
- If an archived file is still worth keeping for provenance, leave it in `archive/` instead of the root.

### Index Synchronization

`index.md` must reflect the actual files in the project.

After adding, deleting, or renaming files:
- Verify all links in `index.md` point to existing files.
- Check that `sheets_md/` and other subdirectories have no orphaned files or broken links.

## Part 3: Report Formatting Standards

### 1. Document Layout & Geometry

- **Page size:** A4 standard.
- **Margins:** 2.54 cm (1 inch) on all sides.
- **Orientation:** Portrait (landscape allowed for appendices with wide tables).
- **Page numbering:** 
  - Arabic numerals (1, 2, 3) starting from the Introduction page.
  - Roman numerals (i, ii, iii) for preliminary pages (Executive Summary, Table of Contents).
  - Place numbers in the bottom centre or bottom right.

### 2. Typography & Font Hierarchy

- **Body font:** Arial, Calibri, or Times New Roman.
- **Body font size:** 
  - 11 pt for Arial/Calibri
  - 12 pt for Times New Roman
- **Main headings (H1):** 16 pt, bold, left-aligned.
- **Subheadings (H2):** 14 pt, bold, left-aligned.
- **Sub-subheadings (H3):** 12 pt, bold or italic, left-aligned.
- **Figure/Table captions:** 10 pt, italic; placed below figures and above tables.

### 3. Spacing & Alignment

- **Line spacing:** 1.5 lines for body text.
- **Paragraph spacing:** 6 pt or 8 pt "space after".
- Do not use double line returns to create spacing.
- **Text alignment:** Left-aligned preferred; justified if required.
- **Bullet points:** Single line spacing within items, 6 pt space after the final bullet.

### 4. Tables, Figures, & Appendices

- **Presentation:** Center-align all tables and figures.
- **Referencing:** Number every visual element (e.g., Figure 1, Table 1) and cite it in body text.
- **Appendices:** Start each appendix on a new page labeled "Appendix A", "Appendix B", etc.

### 5. Mermaid Diagrams

- **Source Files:** Maintain Mermaid source files (`.mmd` extension) as the canonical diagram source in the root directory.
- **Exported Images:** Export Mermaid diagrams to image files (`.png` preferred) and store them in the `diagrams/` directory.
- **PDF Reports:** For PDF reports (generated via `report_to_pdf.py`), always use the exported image files instead of raw Mermaid code blocks to ensure diagrams render correctly in the final PDF.
- **Web Display:** For web/display versions (Docsify), you may use raw Mermaid code blocks for dynamic rendering.

## Part 4: Project Standards & Best Practices

### Minimum Compliance Standards

From this point forward, all new files must follow these five rules:

1. **Filename format:** Lowercase English with underscores; no mixed case.
2. **Filename clarity:** Include the topic; avoid vague terms.
3. **Status indicators:** Use only `draft`, `final`, `orig`, `formatted`, `archive`.
4. **Directory organization:** Separate scripts, exports, and main files; do not mix in root.
5. **Index synchronization:** Keep `index.md` links in sync with actual files.

### Recommended Future Improvements

If gradual cleanup is desired, follow this sequence:

1. Continue using `report_draft.md` for the main working report and `report_final.md` for the submission version.
2. Maintain precise specification naming with a single canonical standards file: `project_guidelines.md`.
3. Ensure `index.md` has no broken links.
4. Standardize naming conventions in `sheets_md/` exports.
5. Move historical versions to an archive or add the `archive` suffix.

### Post-Rename Verification Workflow

After any filename or path change, always run this verification sequence:

1. Regenerate audit report:
  - `python3 scripts/naming_audit.py --root . --write-report naming_audit_report.md`
2. Review `naming_audit_report.md` and confirm:
  - Error = 0
  - Warning = 0 (or document approved exceptions)
3. If the report shows broken links, update `index.md` first.
4. Re-run the audit command until the report is clean.

For repeat use, run the one-click command:

- `.claude/commands/naming-post-rename-verify.md`

This ensures naming cleanup is always paired with link and structure validation.

### Known Issues Addressed

- **Previously:** File naming was ambiguous (e.g., `Report.md` vs. `Report_formatted.md`), making it hard to distinguish work drafts from formatting variants.
- **Previously:** `index.md` contained links to non-existent files in `sheets_md/`.
- **Solution:** This guideline establishes clear naming rules and requires index synchronization to prevent future misalignment.
