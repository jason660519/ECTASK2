Create a safe rename plan from current file names to naming-rule-compliant names.

Context source:
- project_guidelines.md
- naming_audit_report.md if present

Required workflow:
1. Run python3 scripts/naming_audit.py --root . --write-report naming_audit_report.md
2. Build a rename table with columns:
   - current_path
   - proposed_path
   - reason
   - reference_impact (files that must be updated)
3. Separate plan into:
   - Phase A: low-risk renames (few references)
   - Phase B: medium-risk renames
   - Phase C: high-risk renames
4. Ask for confirmation before applying any rename.

This command is planning-only by default.
