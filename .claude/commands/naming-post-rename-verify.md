Run post-rename verification for ECTASK2 naming governance.

Steps:

1. Execute:
   - python3 scripts/naming_audit.py --root . --write-report naming_audit_report.md
2. Read naming_audit_report.md and summarize:
   - Error count
   - Warning count
   - Info count
3. If Error > 0:
   - List blocking issues first (especially broken links in index.md).
4. If Error = 0 and Warning = 0:
   - Report verification PASS.
5. Always include the path to the generated report:
   - naming_audit_report.md

This command is verification-only. Do not rename files automatically.
