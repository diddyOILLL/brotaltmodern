"""Stage hosting assets and create a portable ZIP containing exactly nine pages."""
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
DIST.mkdir(exist_ok=True)
files = list(ROOT.glob('*.html')) + [ROOT / name for name in ['README.md', 'BILDQUELLEN.md', 'QUELLEN.md']]
files += [p for p in (ROOT / 'assets').rglob('*') if p.is_file() and p.name != 'hero.webp']
for source in files:
    destination = DIST / source.relative_to(ROOT)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
with zipfile.ZipFile(ROOT / 'Brotwelten.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
    source_extras = [ROOT / 'package.json'] + [p for p in (ROOT / 'tools').iterdir() if p.is_file() and p.suffix in ['.py', '.mjs', '.json', '.md']]
    for source in files + source_extras:
        archive.write(source, Path('brotwelten') / source.relative_to(ROOT))
print(f'Prepared dist/ and Brotwelten.zip ({len(files)} files).')
