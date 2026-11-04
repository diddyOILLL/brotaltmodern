"""Download source photographs and fonts; keep provenance next to the project."""
from pathlib import Path
import json
import re
import urllib.request
import html
import sys
import subprocess
import time
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
sys.stdout.reconfigure(encoding='utf-8')
HEADERS = {'User-Agent': 'BrotweltenSchoolProject/1.0 (educational image attribution research)'}

def fetch(url):
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=45) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt == 3:
                raise
            time.sleep(5 * (attempt + 1))

if __name__ == '__main__':
    sys.path.insert(0, str(ROOT / '.tools'))
    try:
        from PIL import Image, ImageOps, ImageDraw
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--target', str(ROOT / '.tools'), 'Pillow', '--quiet'])
        import importlib
        importlib.invalidate_caches()
        from PIL import Image, ImageOps, ImageDraw
    import io
    images = ROOT / 'assets/images'
    images.mkdir(parents=True, exist_ok=True)
    names = {
        'weizenbrot': 'Weißbrot-1.jpg',
        'roggenbrot': '100% Rye Bread (5752657009).jpg',
        'vollkornbrot': 'Wholemeal tin loaf (8370566283).jpg',
        'dinkelbrot': 'Dinkelbrot (4212924064).jpg',
        'baguette': 'Baguettes.jpg',
        'ciabatta': 'Ciabatta Bread.jpg',
    }
    metadata = {}
    def clean(value):
        return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', value))).strip()
    for slug, filename in names.items():
        url = 'https://commons.wikimedia.org/wiki/File:' + quote(filename.replace(' ', '_'))
        cached = ROOT / '.tools' / (slug + '-source.txt')
        page = cached.read_text(encoding='utf-8') if cached.exists() else fetch(url).decode('utf-8')
        (ROOT / '.tools' / (slug + '-source.txt')).write_text(page, encoding='utf-8')
        page = html.unescape(page)
        original = html.unescape(re.search(r'class="fullImageLink"[^>]*>\s*<a href="([^"]+)"', page).group(1))
        author = re.search(r'id="fileinfotpl_aut".*?</td>\s*<td[^>]*>(.*?)</td>', page, re.S)
        licenses = re.findall(r'class="licensetpl_short"[^>]*>(.*?)</[^>]+>', page, re.S)
        print(slug, 'author:', clean(author.group(1)) if author else '?', 'licenses:', [clean(x) for x in licenses], flush=True)
        if (images / (slug + '.webp')).exists():
            photo = Image.open(images / (slug + '.webp'))
        else:
            data = fetch(original)
            photo = ImageOps.exif_transpose(Image.open(io.BytesIO(data))).convert('RGB')
            photo.thumbnail((1600, 1600))
            photo.save(images / (slug + '.webp'), 'WEBP', quality=83, method=6)
        thumb = photo.copy()
        thumb.thumbnail((700, 10000))
        thumb.save(images / (slug + '-small.webp'), 'WEBP', quality=80, method=6)
        medium = photo.copy()
        medium.thumbnail((1100, 10000))
        medium.save(images / (slug + '-medium.webp'), 'WEBP', quality=81, method=6)
        license_names = [clean(x) for x in licenses]
        license_names.sort(key=lambda value: not value.startswith('CC'))
        metadata[slug] = {'title': filename, 'source': url, 'original': original, 'author': clean(author.group(1)) if author else '', 'licenses': license_names, 'width': photo.width, 'height': photo.height, 'small_width': thumb.width, 'small_height': thumb.height, 'medium_width': medium.width, 'medium_height': medium.height}
    if not (images / 'hero.webp').exists():
        (images / 'hero.webp').write_bytes(fetch('https://images.unsplash.com/photo-1590301157172-7ba48dd1c2b2?auto=format&fit=crop&w=1800&q=85&fm=webp'))
    photo = Image.open(images / 'hero.webp').convert('RGB')
    photo.save(images / 'sauerteigbrot.webp', 'WEBP', quality=84, method=6)
    thumb = photo.copy()
    thumb.thumbnail((700, 10000))
    thumb.save(images / 'sauerteigbrot-small.webp', 'WEBP', quality=80)
    medium = photo.copy()
    medium.thumbnail((1100, 10000))
    medium.save(images / 'sauerteigbrot-medium.webp', 'WEBP', quality=81, method=6)
    metadata['sauerteigbrot'] = {'title': 'Sourdough loaf', 'source': 'https://unsplash.com/photos/bread-on-brown-wooden-table-yL9qjDDmmMU', 'original': 'https://images.unsplash.com/photo-1590301157172-7ba48dd1c2b2', 'author': 'Vicky Ng', 'licenses': ['Unsplash License'], 'width': photo.width, 'height': photo.height, 'small_width': thumb.width, 'small_height': thumb.height, 'medium_width': medium.width, 'medium_height': medium.height}
    # Persist actual fetched provenance, never guessed image credits.
    (ROOT / 'tools/image-metadata.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding='utf-8')
    sheet = Image.new('RGB', (1200, 840), '#F8F5EF')
    draw = ImageDraw.Draw(sheet)
    for index, slug in enumerate(['sauerteigbrot', *names]):
        tile = ImageOps.fit(Image.open(images / (slug + '.webp')), (390, 245))
        x, y = (index % 3) * 400, (index // 3) * 280
        sheet.paste(tile, (x, y))
        draw.text((x + 8, y + 250), slug, fill='#241B16')
    sheet.save(ROOT / 'tools/photos-review.jpg')
    fonts = ROOT / 'assets/fonts'
    fonts.mkdir(parents=True, exist_ok=True)
    css = fetch('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Libre+Caslon+Display&display=swap').decode()
    blocks = re.findall(r'@font-face\s*\{(.*?)\}', css, re.S)
    localcss = []
    seen = {}
    for block in blocks:
        family = re.search(r"font-family:\s*'([^']+)'", block).group(1)
        weight = re.search(r'font-weight:\s*([^;]+)', block).group(1)
        remote = re.search(r'url\(([^)]+)\)', block).group(1)
        filename = family.lower().replace(' ', '-') + '-' + weight + '.ttf'
        if remote not in seen:
            (fonts / filename).write_bytes(fetch(remote))
            seen[remote] = filename
        localcss.append('@font-face {' + block.replace(remote, '../fonts/' + seen[remote]) + '}')
    (ROOT / 'assets/css').mkdir(parents=True, exist_ok=True)
    (ROOT / 'assets/css/fonts.css').write_text('\n'.join(localcss), encoding='utf-8')
    for folder in ['dmsans', 'librecaslondisplay']:
        (fonts / (folder + '-OFL.txt')).write_bytes(fetch('https://raw.githubusercontent.com/google/fonts/main/ofl/' + folder + '/OFL.txt'))
    print('Photographs and local fonts downloaded.', flush=True)
