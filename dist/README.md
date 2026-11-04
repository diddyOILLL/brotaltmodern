# Brotwelten

Ein gemeinsames Projekt von Rico, Til und Otto mit **genau neun eigenständigen HTML-Seiten** über sieben Brotsorten. Die Website verwendet ausschließlich HTML5 und CSS3.

## Starten

`index.html` mit einem Doppelklick im Browser öffnen. Alle Bilder und Schriften liegen lokal im Ordner `assets/`. Das Projekt funktioniert auch ohne Internet; nur die externen Rezept- und Quellenlinks benötigen eine Verbindung.

Alternativ mit installiertem Python im Projektordner `python -m http.server 4173 --bind 127.0.0.1` ausführen und http://127.0.0.1:4173/ öffnen. Die ZIP-Datei `Brotwelten.zip` enthält die abgabefertige Website. Zum Starten entpacken, den Ordner `brotwelten` öffnen und `index.html` starten.

## Seiten

- `index.html` – Startseite und sieben Brotporträts als Fotokarten
- `weizenbrot.html`, `roggenbrot.html`, `vollkornbrot.html`, `dinkelbrot.html`
- `baguette.html`, `ciabatta.html`, `sauerteigbrot.html`
- `ueber-uns.html` – Projekt, Team, Technik, Bildnachweise und Quellen

Jede Seite enthält dieselbe Navigation, ein zur Startseite verlinktes Logo und Links zu allen anderen Seiten. Jede Unterseite besitzt zusätzlich den sichtbaren Link „← Zurück zur Startseite“.

## Anpassen

- Die Teammitglieder Rico, Til und Otto stehen in `ueber-uns.html` im Abschnitt `team`.
- **Farben, Abstände und Schriftgrößen:** zentrale Variablen und gemeinsame Regeln in `assets/css/style.css`.
- **Texte:** direkt in der jeweiligen HTML-Datei bearbeiten. Die Inhalte sind vollständig im HTML enthalten.
- Das Brotsorten-Menü lässt sich über das native HTML-Element `<details>` per Maus, Touch und Tastatur öffnen. Auf schmalen Bildschirmen stehen die Hauptlinks unter dem Logo. Alle sieben Brotkarten sind direkt sichtbar.
- **Fotos und Rechte:** siehe `BILDQUELLEN.md` sowie den Abschnitt „Bildnachweise“ auf der Projektseite. Lizenz und Urheber bei einer Weitergabe der Bilder beibehalten.

## Gestaltung und Zugänglichkeit

Warme Creme-, Braun- und Kupfertöne, lokale Serif- und Sans-Serif-Schriften, responsive CSS-Grids, sichtbarer Tastaturfokus, Sprunglink, beschriftete Navigation und native `<details>` für das Dropdown. CSS-Effekte sind zurückhaltend und werden bei `prefers-reduced-motion` abgeschaltet.

## Quellen und Prüfung

Sieben konkrete Chefkoch-Rezeptseiten sind verlinkt; sie öffnen mit `target="_blank"` und `rel="noopener noreferrer"`. Es werden keine vollständigen Rezepte kopiert. Recherche und Quellen sind in `QUELLEN.md` dokumentiert. Fotos von Wikimedia Commons und Unsplash sind lokal als WebP in zwei Größen gespeichert. Die Schriften stehen unter der SIL Open Font License; die Lizenztexte liegen in `assets/fonts/`.

`python tools/verify.py` prüft die neun Seiten, interne Links und Anker, lokale Assets, Rücklinks und externe Linkattribute. Browserprüfungen sind in `tools/QA.md` dokumentiert.

Die Hilfsprogramme unter `tools/` sind optional. `generate-pages.py` ist eine Entwicklungshilfe; Änderungen an seiner Datenbasis überschreiben beim erneuten Ausführen die HTML-Dateien. Für den Schulbetrieb wird es nicht benötigt. `package-project.py` aktualisiert die ZIP und die Kopie unter `dist/` für das Hosting. Die eigentliche Website kann immer direkt aus den neun HTML-Dateien verwendet werden.
