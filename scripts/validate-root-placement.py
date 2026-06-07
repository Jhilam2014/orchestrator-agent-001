#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
RESERVED = {'schemas', 'examples'}
ALLOWED_SCHEMA_EXTENSIONS = {'.json'}
violations = []
for p in ROOT.rglob('*'):
    if not p.is_file():
        continue
    rel = p.relative_to(ROOT)
    parts = rel.parts
    if not parts:
        continue
    if parts[0] == 'schemas' and not p.name.endswith('.schema.json'):
        violations.append(str(rel))
    if parts[0] == 'examples' and len(parts) > 1 and 'sample' not in p.name.lower() and 'example' not in p.name.lower():
        violations.append(str(rel))
if violations:
    print('Root placement validation failed:')
    for v in violations:
        print(' -', v)
    sys.exit(1)
print('Root placement validation passed.')
