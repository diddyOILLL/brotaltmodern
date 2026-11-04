# Qualitätsprüfung – 30. Oktober 2026

## Aktualisierung vom 4. November 2026

JavaScript wurde vollständig aus dem Website-Quellcode, den optionalen lokalen Hilfsprogrammen und dem Abgabepaket entfernt. Die Teammitglieder heißen Rico, Til und Otto. Die Hauptnavigation ist direkt sichtbar, das Brotsorten-Menü verwendet das native HTML-Element `<details>`, und alle sieben Brotporträts werden gemeinsam angezeigt.

Alle neun Seiten wurden bei 320 Pixeln Breite im Browser geprüft. Jede Seite enthält null Skripte, die Navigation ist sichtbar, und es gibt keinen horizontalen Überlauf. Das Brotsorten-Menü öffnet und schließt per Tastatur und enthält alle sieben Links. Der Wechsel zur Roggenbrotseite und die Rückkehr zu den sieben Karten der Startseite funktionieren. Auf der Projektseite wurden die Namen Rico, Til und Otto sowie die beiden Technikbereiche HTML5 und CSS3 geprüft.

Die nachfolgenden Prüfungen vom 30. Oktober dokumentieren die frühere Fassung.

## Statische Prüfung

- Genau neun HTML-Seiten im Projektstamm.
- 324 Links einschließlich interner Seitenziele und Sprungmarken geprüft.
- Alle Seiten verlinken alle anderen Seiten und das Logo führt zur Startseite.
- Alle acht Unterseiten enthalten den gut sichtbaren Rücklink „← Zurück zur Startseite“.
- 17 Bildeinbindungen mit vorhandenen lokalen Dateien, Alt-Texten und Größenangaben.
- Auch alle `srcset`-Varianten, Schriftdateien und CSS-Verweise sind vorhanden.
- Pro Seite ein `h1`, ein `main` und `lang="de"`; keine doppelten IDs.
- Sieben konkrete Rezeptlinks mit `target="_blank"` und `rel="noopener noreferrer"`.
- JavaScript-Syntax mit `node --check` geprüft.

## Browserprüfung

Im integrierten Chromium-Browser über den lokalen HTTP-Server geprüft:

- Alle neun Seiten bei 1440, 390 und 320 Pixeln Breite auf Überlauf geprüft; kein horizontaler Überlauf nach Korrektur der schmalen Kurzinfozeile.
- Startseite, Sauerteigbrot und Projektseite zusätzlich bei 768 und 1024 Pixeln geprüft.
- Desktop- und Mobilansicht visuell geprüft; sämtliche Startseitenfotos und die großen Fotos aller Unterseiten korrekt geladen.
- Geschmacksfilter „Mild & luftig“ zeigt genau Weizenbrot, Baguette und Ciabatta; „Nussig & fein“ zeigt Dinkelbrot; „Alle Brote“ stellt alle sieben wieder her.
- Mobiles Menü öffnet, das native Brotsorten-Dropdown zeigt alle sieben Einträge und ein Klick öffnet die entsprechende Brotseite.
- Rücklink von der Roggenbrotseite führt zuverlässig zu `index.html`.
- Escape schließt zunächst das Dropdown und setzt den Fokus auf dessen Schalter; ein weiteres Escape schließt das mobile Menü und setzt den Fokus auf den Menüschalter.
- Ohne Skripte: Startseite und Sauerteigseite über eine lokale QA-Ansicht mit serverseitig entfernten Script-Tags geprüft. Navigation und Inhalte sind vorhanden, das native Dropdown öffnet und alle sieben Brotkarten bleiben sichtbar. Es wurden keine zusätzlichen HTML-Dateien angelegt.
- Keine erfassten JavaScript-Fehler oder Warnungen in der Browserkonsole.

## Fotos und externe Quellen

Alle sieben tatsächlichen Fotos wurden anhand ihrer Quelle und einer gemeinsamen Bildübersicht geprüft. Bildbeschreibungen wurden an die sichtbaren Motive angepasst. Urheber und Lizenzen wurden aus den Originalseiten ausgelesen und in `BILDQUELLEN.md` sowie auf der Projektseite dokumentiert.

Alle sieben Chefkoch-URLs wurden über den Webabruf geöffnet; passende Rezepttitel und Inhalte waren auslesbar. Diese Prüfung bestätigt die Zielseiten zum Recherchezeitpunkt, nicht die zukünftige Verfügbarkeit externer Websites.

`prefers-reduced-motion` ist in CSS und JavaScript berücksichtigt und wurde im Quellcode geprüft. Es wurde keine Prüfung mit einem vollständigen Screenreader oder auf realen iOS-/Android-Geräten durchgeführt.
