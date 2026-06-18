# Naming Governance Skill

## Purpose

Enforce repository naming and file-management rules for ECTASK2 with a predictable, low-risk workflow.

## Inputs

- Project rule source: project_guidelines.md
- Current repository tree
- Optional previous report: naming_audit_report.md

## Use This Skill When

- You need to clean up inconsistent file naming across multiple directories.
- You need a staged rename plan with reference impact analysis.
- You need index.md link integrity checks after renames.

## Do Not Use This Skill When

- You only need a quick report without edits. Use command naming-check instead.
- You need to update one or two files manually.

## Workflow

1. Run baseline audit:
   - python3 scripts/naming_audit.py --root . --write-report naming_audit_report.md
2. Categorize findings by severity and ref impact.
3. Produce staged rename plan (A/B/C risk levels).
4. Request explicit confirmation before applying renames.
5. Apply renames in small batches.
6. Update references and links (at least index.md).
7. Re-run audit and show delta.

## Output Contract

- Summary of findings (errors/warnings/info)
- Rename table (current -> proposed)
- Reference update list
- Post-change verification results

## Safety Rules

- Never run destructive git commands.
- Never rename high-impact files without approval.
- Keep existing user edits unless explicitly instructed otherwise.
