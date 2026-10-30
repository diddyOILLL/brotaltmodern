// Optional local preview. No packages, installation or build are required.
import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const root = fileURLToPath(new URL('../', import.meta.url));
const types = { '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.svg': 'image/svg+xml', '.webp': 'image/webp', '.ttf': 'font/ttf', '.txt': 'text/plain; charset=utf-8', '.md': 'text/plain; charset=utf-8' };
const server = createServer(async (request, response) => {
  try {
    const url = new URL(request.url, 'http://localhost');
    const pathname = decodeURIComponent(url.pathname);
    const relative = pathname === '/' ? 'index.html' : pathname.replace(/^\/+/, '');
    if (relative.split('/').some(part => part.startsWith('.')) || relative.startsWith('tools/')) {
      response.writeHead(404).end('Nicht gefunden');
      return;
    }
    const filename = path.resolve(root, relative);
    if (!filename.startsWith(root) || !(await stat(filename)).isFile()) throw new Error('Missing file');
    response.writeHead(200, { 'Content-Type': types[path.extname(filename)] || 'application/octet-stream', 'Cache-Control': 'no-store' });
    const contents = await readFile(filename);
    // Local QA only: same HTML with script tags removed, without extra HTML files.
    response.end(url.searchParams.get('no-js') === '1' && filename.endsWith('.html')
      ? contents.toString('utf8').replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, '')
      : contents);
  } catch {
    response.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' }).end('Seite nicht gefunden. Bitte zur Startseite zurückkehren.');
  }
});
server.listen(4173, '127.0.0.1', () => console.log('Brotwelten: http://127.0.0.1:4173/'));
