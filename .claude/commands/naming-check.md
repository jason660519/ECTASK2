Read project naming rules from project_guidelines.md, then run:

python3 scripts/naming_audit.py --root . --write-report naming_audit_report.md

After running, summarize:
1. Error findings (must-fix)
2. Warning findings (should-fix)
3. Top 10 rename suggestions by impact
4. Broken links found in index.md

Do not apply any renames in this command. Report only.
