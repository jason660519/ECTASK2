Validate index consistency for this repository.

Steps:
1. Run python3 scripts/naming_audit.py --root .
2. Focus only on broken_link findings for index.md.
3. For each broken link, propose the best fix:
   - update link target to an existing file, or
   - remove obsolete entry, or
   - create missing file only if explicitly required by the current project docs.

Output format:
- Broken links list
- Proposed edits to index.md

Do not edit files automatically in this command unless user explicitly asks to apply fixes.
