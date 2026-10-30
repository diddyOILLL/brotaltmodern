"""Check actual static pages, anchors, local assets and required navigation."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {'index.html', 'weizenbrot.html', 'roggenbrot.html', 'vollkornbrot.html', 'dinkelbrot.html', 'baguette.html', 'ciabatta.html', 'sauerteigbrot.html', 'ueber-uns.html'}

class Document(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.ids, self.links, self.assets, self.images = set(), [], [], []
        self.h1 = self.main = 0
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, 'Duplicate ID: ' + a['id']
            self.ids.add(a['id'])
        if tag == 'a': self.links.append(a)
        if tag == 'img':
            self.images.append(a)
            self.assets.append(a['src'])
            assert a.get('alt'), 'Missing alt text'
            assert a.get('width') and a.get('height'), 'Missing intrinsic image dimensions'
            for item in a.get('srcset', '').split(','):
                if item.strip(): self.assets.append(item.strip().split()[0])
        if tag in ['script', 'link']:
            target = a.get('src') if tag == 'script' else a.get('href')
            if target: self.assets.append(target)
        if tag == 'h1': self.h1 += 1
        if tag == 'main': self.main += 1

pages = {file.name: file.read_text(encoding='utf-8') for file in ROOT.glob('*.html')}
assert set(pages) == EXPECTED, f'Expected exactly nine pages, found {set(pages)}'
docs = {name: Document(source) for name, source in pages.items()}
link_count = image_count = 0
for name, source in pages.items():
    doc = docs[name]
    assert doc.h1 == 1 and doc.main == 1, f'{name}: one h1 and main required'
    assert '<html lang="de">' in source
    assert 'href="index.html"' in source
    assert '<details class="bread-menu' in source
    if name != 'index.html': assert '← Zurück zur Startseite</a>' in source
    destinations = set()
    for a in doc.links:
        target = urlsplit(a['href'])
        link_count += 1
        if target.scheme in ['http', 'https']:
            assert a.get('target') == '_blank', f'{name}: external target missing'
            assert {'noopener', 'noreferrer'}.issubset(set(a.get('rel', '').split()))
            continue
        path = unquote(target.path) or name
        assert (ROOT / path).is_file(), f'{name}: missing target {path}'
        destinations.add(path)
        if target.fragment:
            assert target.fragment in docs[path].ids, f'{name}: missing anchor {path}#{target.fragment}'
    assert EXPECTED.issubset(destinations), f'{name}: missing page links {EXPECTED - destinations}'
    for target in doc.assets:
        assert not urlsplit(target).scheme, 'All assets must be local'
        assert (ROOT / target).is_file(), f'{name}: missing asset {target}'
    image_count += len(doc.images)
    if name not in ['index.html', 'ueber-uns.html']:
        chefkoch = [a for a in doc.links if urlsplit(a['href']).hostname == 'www.chefkoch.de']
        assert len(chefkoch) == 1 and '/rezepte/' in chefkoch[0]['href']
for css in (ROOT / 'assets/css').glob('*.css'):
    for url in re.findall(r'url\(([^)]+)\)', css.read_text(encoding='utf-8')):
        assert (css.parent / url.strip('\"\'')).is_file(), f'Missing CSS asset {url}'
print(f'PASS: 9 pages, {link_count} links, {image_count} image instances, all anchors/assets and required return links.')
