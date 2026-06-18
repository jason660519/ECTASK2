# Project Homepage

Welcome to the ECTask2 workspace. This homepage organizes the current project files and links to the main working documents.

## Main Pages

- [readme.md](./readme.md) — Project overview, structure, and maintenance workflow.
- [assessment_task2_report_final.md](./assessment_task2_report_final.md) — **Final Submission Report** (fully optimised for marking)
- [report_final.md](./report_final.md) — Previous formatted submission-oriented version of the report.
- [report_draft.md](./report_draft.md) — Main working draft of the report.
- [project_guidelines.md](./project_guidelines.md) — Unified project guidelines for report formatting and file naming management.
- [sheets_md/3c_clean_en.md](./sheets_md/3c_clean_en.md) — Cleaned summary of the home device inventory for report use.

## Diagram Sources

- `smart_home_network_diagram.mmd` — Main Mermaid source for the proposed network diagram.
- `smart_home_network_diagram_simple.mmd` — Simplified diagram variant.
- `smart_home_network_diagram_segmented.mmd` — Segmented security architecture variant.
- `smart_home_network_diagram_by_rooms.mmd` — Room-based diagram variant.

> Note: All diagrams are visually rendered on the [Network Diagrams](./network_diagrams.md) page.

## Notes

- `assessment_task2_report_final.md` is the **final, optimised report** ready for submission.
- `report_draft.md` is the active working draft.
- `sheets_md/` keeps a cleaned summary file for report usage.
- Exported diagram images are archived in `archive/diagram_exports/`.
- Raw source exports such as Pages files should be kept in `archive/` unless they are the active editable source.
- Diagram editing should use the `.mmd` files rather than the exported image.

## Rename Quick Checklist

After any filename/path change, run this short flow:

1. Run command: `.claude/commands/naming-post-rename-verify.md`
2. Confirm `naming_audit_report.md` shows `Error = 0`
3. If errors mention broken links, fix `index.md` first
4. Re-run verification until it passes
