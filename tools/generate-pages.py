"""Optional editing helper. The generated HTML files need no build or Python."""
from pathlib import Path
from datetime import date
import json
from html import escape

ROOT = Path(__file__).resolve().parents[1]
# Festes Recherchedatum, nur nach einem tatsächlichen Quellenaufruf ändern.
SOURCE_ACCESS_DATE = date(2026, 11, 4)
SOURCE_ACCESS_TEXT = 'Zuletzt aufgerufen am ' + SOURCE_ACCESS_DATE.strftime('%d.%m.%Y')
SOURCE_ACCESS_HTML = f'Zuletzt aufgerufen am <time datetime="{SOURCE_ACCESS_DATE.isoformat()}">{SOURCE_ACCESS_DATE.strftime("%d.%m.%Y")}</time>'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M4 12h15m-6-6 6 6-6 6"/></svg>'
DOWN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>'
DIAGONAL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M6 18 18 6M6 6h12v12"/></svg>'

BREADS = [
  dict(slug='weizenbrot', name='Weizenbrot', region='Vielseitiger Klassiker', origin='Vorderasien · weltweit', grain='Weizen', taste='Mild & fein', category_label='Mild & luftig',
    subtitle='Goldene Kruste. Helle Krume. Ein Brot für jeden Tag.',
    short='Mild im Geschmack, luftig im Inneren. Der helle Klassiker, der zu fast allem passt.',
    alt='Angeschnittenes helles Weizenbrot mit goldbrauner Kruste und feinporiger Krume',
    history_title='Ein Getreide geht um die Welt.',
    history=[
      'Die Geschichte des Weizenbrotes beginnt mit dem Anbau früher Weizenarten in Vorderasien. Aus einfachen Getreidefladen entwickelten sich im Lauf der Jahrtausende gelockerte Brote. Einen einzelnen Erfinder oder einen eindeutigen Ursprungsort des heutigen Weizenbrotes gibt es deshalb nicht.',
      'Weizen eignet sich besonders gut für luftige Brote: Beim Kneten bildet sein Klebereiweiß ein elastisches Gerüst, das die Gärgase festhält. Heute findet man Weizenbrot in vielen Formen – als runden Laib, Kastenbrot oder längliches Weißbrot. Gerade im Mittelmeerraum gehört helles Brot selbstverständlich auf den Tisch.'
    ],
    properties=[('Zutaten', 'Weizenmehl, Wasser, Salz und Hefe oder Sauerteig. Je nach Rezept kommen weitere Zutaten hinzu.'), ('Geschmack', 'Mild und dezent getreidig. Eine kräftige Bräunung bringt Röstaromen in die Kruste.'), ('Kruste', 'Goldgelb bis goldbraun, bei frei gebackenen Broten häufig dünn und knusprig.'), ('Krume', 'Hell, weich und locker; die Poren können je nach Teigführung fein oder unregelmäßig sein.')],
    facts=[('Ein elastisches Gerüst', 'Das beim Kneten entstehende Glutengerüst hält Gasbläschen fest. So bekommt Weizenbrot sein Volumen.'), ('Die Form entscheidet mit', 'Ein freigeschobener Laib hat mehr Krustenfläche als ein Kastenbrot. Das verändert das Verhältnis von Kruste und Krume.'), ('Auch mit Sauerteig', 'Weizenbrot muss kein reines Hefebrot sein. Ein Weizensauerteig kann für Lockerung und ein vielschichtiges Aroma sorgen.')],
    pairing='Frische Butter, milder Käse oder selbst gemachte Marmelade lassen dem feinen Brotgeschmack Raum.',
    recipe='https://www.chefkoch.de/rezepte/2497421392380064/Einfaches-Weizenbrot.html', recipe_title='Einfaches Weizenbrot', recipe_author='hulkholler', recipe_note='Ein unkompliziertes Kastenbrot mit Weizenmehl und Trockenhefe.',
    source='https://www.ploetzblog.de/baeckerlatein/brotsorten/id=611a73f0c30e586ffcd80769', source_title='Plötzblog: Einteilung der Brotsorten'),
  dict(slug='roggenbrot', name='Roggenbrot', region='Nord- & Mitteleuropa', origin='Nord- & Mitteleuropa', grain='Roggen', taste='Kräftig & würzig', category_label='Kräftig & kernig',
    subtitle='Dunkel, saftig und voller Charakter.',
    short='Kräftiges Aroma und eine saftige, dichte Krume. Ein Stück mitteleuropäische Brotkultur.',
    alt='Angeschnittenes Kastenbrot aus hundert Prozent Roggen auf einem Holzbrett',
    history_title='Verwurzelt im Norden.',
    history=[
      'Roggen kommt mit kühlen Temperaturen und weniger fruchtbaren Böden vergleichsweise gut zurecht. Das machte ihn in Nord-, Mittel- und Osteuropa zu einem wichtigen Brotgetreide. In Deutschland prägte er über lange Zeit die tägliche Brotversorgung; seine Bedeutung reichte weit über einzelne regionale Spezialitäten hinaus.',
      'Zum Roggenbrot gehört traditionell die Arbeit mit Sauerteig. Die Säuerung unterstützt die Backfähigkeit roggenreicher Teige und prägt ihr Aroma. Bis heute begegnet man Roggenbroten von Deutschland und Polen bis ins Baltikum und nach Skandinavien – mit unterschiedlichen Formen, Gewürzen und Backweisen.'
    ],
    properties=[('Zutaten', 'Roggenmehl oder Roggenschrot, Wasser, Salz und meist Sauerteig. Manche Rezepte ergänzen etwas Hefe.'), ('Geschmack', 'Kräftig getreidig, würzig und je nach Sauerteigführung mild bis deutlich säuerlich.'), ('Kruste', 'Meist kräftig gebacken, oft dunkel und rustikal aufgerissen oder fein bemehlt.'), ('Krume', 'Eher dicht und feinporig. Roggen bindet viel Wasser und sorgt für eine saftige Textur.')],
    facts=[('Kein Weizenteig', 'Roggenteig entwickelt kein vergleichbares elastisches Glutengerüst. Seine Struktur entsteht beim Backen auf andere Weise.'), ('Säure mit Aufgabe', 'Sauerteig bringt Aroma und hilft, die Stärke in roggenreichen Broten beim Backen zu stabilisieren.'), ('Eine Frage der Mischung', 'Roggenbrot und Roggenmischbrot sind unterschiedliche Bezeichnungen. Beim Mischbrot spielt auch Weizen eine größere Rolle.')],
    pairing='Kräftiger Käse, würzige Aufstriche oder einfach gesalzene Butter passen zu seinem herzhaften Charakter.',
    recipe='https://www.chefkoch.de/rezepte/2546941398669812/Reines-Roggenbrot-mit-Sauerteig.html', recipe_title='Reines Roggenbrot mit Sauerteig', recipe_author='andrea_luise', recipe_note='Ein Roggenbrot mit Vorteig und einer längeren Reifezeit.',
    source='https://www.bzfe.de/presse/pressemeldungen-archiv/getreide-abc-roggen', source_title='BZfE: Getreide-ABC Roggen'),
  dict(slug='vollkornbrot', name='Vollkornbrot', region='Das ganze Korn', origin='Viele regionale Traditionen', grain='Ganzes Getreidekorn', taste='Kernig & aromatisch', category_label='Kräftig & kernig',
    subtitle='Alles vom Korn. Viel vom Geschmack.',
    short='Schale, Keimling und Mehlkörper: Hier kommt das ganze Getreidekorn ins Brot.',
    alt='Braunes Vollkorn-Kastenbrot mit einem Längsschnitt auf einem runden Holzbrett',
    history_title='Ein Brot aus dem ganzen Korn.',
    history=[
      'Vollkornbrot ist keine einzelne regionale Erfindung. Der Name beschreibt vielmehr, welche Teile des Getreidekorns verwendet werden. Anders als bei hellem Auszugsmehl bleiben Schale und Keimling neben dem Mehlkörper erhalten. Vollkorn kann fein gemahlen oder als gröberes Schrot verarbeitet werden.',
      'Entsprechend vielfältig sind die Brote: vom lockeren Weizenvollkornbrot bis zum dichten Roggenschrotbrot. In vielen europäischen Backtraditionen haben solche Brote ihren festen Platz. Heute wird Vollkornbrot sowohl handwerklich als auch zu Hause gebacken – pur, mit Saaten oder mit verschiedenen Getreidearten.'
    ],
    properties=[('Zutaten', 'Vollkornmehl oder Vollkornschrot, Wasser, Salz und Hefe oder Sauerteig. Saaten sind möglich, aber nicht notwendig.'), ('Geschmack', 'Ausgeprägt getreidig, häufig nussig. Roggen, Weizen und Dinkel bringen jeweils eigene Aromen mit.'), ('Kruste', 'Je nach Getreide und Backweise zart bis kräftig. Sichtbare Körner sind kein Muss.'), ('Krume', 'Oft saftig und kompakter als bei hellem Brot; bei feinem Vollkornmehl trotzdem gleichmäßig und weich.')],
    facts=[('Fein ist auch voll', 'Vollkorn sagt etwas über die Bestandteile des Mehls aus, nicht über seine Körnung. Vollkornmehl kann sehr fein sein.'), ('Körner sind kein Beweis', 'Eine Saatenkruste macht ein Brot noch nicht zum Vollkornbrot. Entscheidend sind die verwendeten Getreidemahlerzeugnisse.'), ('Die Farbe reicht nicht', 'Auch ein dunkles Brot kann aus hellem Mehl bestehen. Den Vollkornanteil erkennt man zuverlässiger an Bezeichnung und Zutaten.')],
    pairing='Frischkäse, knackige Radieschen oder ein Hummus passen gut zur aromatischen Krume.',
    recipe='https://www.chefkoch.de/rezepte/1344331239198800/Saftiges-Vollkornbrot.html', recipe_title='Saftiges Vollkornbrot', recipe_author='egghead', recipe_note='Ein Kastenbrot aus Dinkelvollkornmehl mit einer Mischung aus Kernen.',
    source='https://de.wikipedia.org/wiki/Vollkornbrot', source_title='Hintergrund: Vollkornbrot'),
  dict(slug='dinkelbrot', name='Dinkelbrot', region='Mitteleuropäische Tradition', origin='Mitteleuropa', grain='Dinkel', taste='Nussig & fein', category_label='Nussig & fein',
    subtitle='Eine alte Getreideart mit feiner, nussiger Note.',
    short='Mild, leicht nussig und vielseitig. Eine alte Weizenart zeigt, was in ihr steckt.',
    alt='Angeschnittenes Dinkelbrot mit Sesam, Leinsamen, Sonnenblumenkernen, Kürbiskernen und Walnüssen',
    history_title='Altes Getreide, neu entdeckt.',
    history=[
      'Dinkel ist eng mit dem gewöhnlichen Brotweizen verwandt und gehört zu den alten Kulturgetreiden. In Teilen Mitteleuropas, etwa im südwestdeutschen Raum und in der Schweiz, hat sein Anbau eine lange Tradition. Später wurde er vielerorts von ertragreicheren Weizensorten verdrängt.',
      'Mit dem Interesse an unterschiedlichen Getreidearten ist auch Dinkelbrot wieder stärker in den Blick gerückt. Es ist kein einheitliches Rezept: Helles Dinkelmehl ergibt ein feineres, lockeres Brot, Vollkornmehl einen kräftigeren Laib. Das abgebildete Brot ist eine Variante mit Saaten und Walnüssen.'
    ],
    properties=[('Zutaten', 'Dinkelmehl oder Dinkelvollkornmehl, Wasser, Salz und Hefe oder Sauerteig. Häufig auch Saaten oder Nüsse.'), ('Geschmack', 'Mild bis kräftig getreidig, oft mit einer feinen nussigen Note; Vollkorn schmeckt ausgeprägter.'), ('Kruste', 'Goldbraun bis kräftig gebacken. Eine Saatenauflage bringt zusätzlichen Biss.'), ('Krume', 'Je nach Mehl hell oder bräunlich. Ausreichend Wasser und eine passende Teigführung halten sie saftig.')],
    facts=[('Gut geschützt', 'Das Dinkelkorn sitzt fest im Spelz. Vor dem Mahlen muss diese Hülle in einem zusätzlichen Arbeitsschritt entfernt werden.'), ('Mit Weizen verwandt', 'Dinkel gehört zur Weizenverwandtschaft und enthält Gluten. Die Getreideart ist also kein glutenfreier Ersatz.'), ('Mit Gefühl kneten', 'Dinkelteige reagieren empfindlicher auf zu langes Kneten. Eine sorgfältige Teigführung hilft, die Struktur zu erhalten.')],
    pairing='Milder Ziegenkäse, Birne oder ein Gemüseaufstrich greifen die feinen, nussigen Aromen auf.',
    recipe='https://www.chefkoch.de/rezepte/148901065524584/Dinkelbrot-einfach.html', recipe_title='Dinkelbrot – einfach', recipe_author='maeuseturm', recipe_note='Ein schlichtes Dinkel-Hefebrot für die Kastenform.',
    source='https://de.wikipedia.org/wiki/Dinkelbrot', source_title='Hintergrund: Dinkelbrot'),
  dict(slug='baguette', name='Baguette', region='Frankreich', origin='Frankreich', grain='Weizen', taste='Knusprig & mild', category_label='Mild & luftig',
    subtitle='Eine krachende Kruste. Ein französisches Ritual.',
    short='Schlanke Form, goldene Kruste, luftiges Inneres. Frankreichs täglicher Begleiter.',
    alt='Französische Baguettes mit goldbrauner, mehrfach schräg eingeschnittener Kruste',
    history_title='Mehr als ein Stangenbrot.',
    history=[
      'Das Baguette ist eng mit der französischen Alltagskultur verbunden. Seine heute vertraute, lange Form setzte sich vor allem im 20. Jahrhundert durch. Über den genauen Ursprung kursieren verschiedene Geschichten; eine einzelne beliebte Legende erklärt seine Entstehung nicht zuverlässig.',
      'In Frankreich werden Baguettes über den Tag verteilt in kleinen Chargen gebacken. Das handwerkliche Wissen reicht vom Mischen und Fermentieren bis zum Formen, Einschneiden und Backen. Seit 2022 stehen dieses Können und die Kultur rund um das Baguette auf der UNESCO-Liste des immateriellen Kulturerbes.'
    ],
    properties=[('Zutaten', 'Für die klassische Variante: Weizenmehl, Wasser, Salz sowie Hefe und/oder Sauerteig.'), ('Geschmack', 'Milde, aromatische Krume und deutliche Röstaromen in der dünnen Kruste.'), ('Kruste', 'Knusprig und goldbraun, mit mehreren charakteristischen schrägen Einschnitten.'), ('Krume', 'Hell und elastisch, mit unregelmäßiger Porung. Wie groß die Poren ausfallen, hängt von Teig und Verarbeitung ab.')],
    facts=[('Vier Grundzutaten', 'Ein klassisches Baguette kommt mit Mehl, Wasser, Salz und einem Triebmittel aus. Zeit bestimmt das Aroma wesentlich mit.'), ('Anerkanntes Handwerk', 'Die UNESCO würdigte 2022 die handwerklichen Kenntnisse und die gesellschaftliche Kultur des Baguettes.'), ('Die Kruste im Mittelpunkt', 'Durch seine schlanke Form hat das Baguette im Verhältnis zum Inneren viel Kruste – ideal für alle, die es knusprig mögen.')],
    pairing='Ein Stück Käse, etwas Butter oder Olivenöl genügen. Als Beilage nimmt die offene Krume Saucen gut auf.',
    recipe='https://www.chefkoch.de/rezepte/2587261406118751/Baguette-magique.html', recipe_title='Baguette magique', recipe_author='Chefkoch-Community', recipe_note='Ein einfaches Baguette-Rezept für zu Hause, ohne aufwendiges Kneten.',
    source='https://ich.unesco.org/en/RL/artisanal-know-how-and-culture-of-baguette-bread-01883', source_title='UNESCO: Baguette-Handwerk und -Kultur'),
  dict(slug='ciabatta', name='Ciabatta', region='Italien · Venetien', origin='Venetien, Italien', grain='Weizen', taste='Luftig & aromatisch', category_label='Mild & luftig',
    subtitle='Viel Luft. Viel Aroma. Ein kleines Stück Italien.',
    short='Unregelmäßige Poren und eine rustikale Form. Der italienische Klassiker mit der leichten Krume.',
    alt='Vier längliche, frisch gebackene Ciabattabrote mit bemehlter Kruste auf einem Abkühlgitter',
    history_title='Ein junger Klassiker aus Italien.',
    history=[
      'Ciabatta wirkt wie ein uraltes Landbrot, ist in seiner heutigen Form aber ein vergleichsweise junger Klassiker. Seine Entwicklung wird auf das Jahr 1982 und den Bäcker Arnaldo Cavallari im venezianischen Adria zurückgeführt. Das neue Brot sollte auch eine italienische Antwort auf das beliebte französische Baguette sein.',
      'Der Name bedeutet auf Italienisch „Pantoffel“ und spielt auf die flache, längliche Form an. Von Venetien aus verbreitete sich Ciabatta international. Heute findet man zahlreiche Varianten – als großer Laib, als Brötchen und mit unterschiedlichen Vorteigen. Gemeinsam ist ihnen meist ein weicher, wasserreicher Teig.'
    ],
    properties=[('Zutaten', 'Weizenmehl, viel Wasser, Salz und Hefe oder Sauerteig. Manche Varianten enthalten Olivenöl.'), ('Geschmack', 'Mild, mit getreidigen und durch längere Reife entstehenden Aromen; mit Öl auch dezent fruchtig.'), ('Kruste', 'Dünn bis mittelkräftig, knusprig und häufig mit einer unregelmäßigen Mehlzeichnung.'), ('Krume', 'Locker, elastisch und auffallend großporig. Das Innere bleibt oft leicht feucht.')],
    facts=[('Ein Pantoffel zum Essen', '„Ciabatta“ heißt auf Italienisch Pantoffel. Gemeint ist die eher flache, breite und längliche Brotform.'), ('Viel Wasser im Teig', 'Der hohe Wasseranteil trägt zur typischen offenen Porung bei. Solche Teige werden vorsichtig behandelt.'), ('Ein Vorteig bringt Aroma', 'Viele Rezepte arbeiten mit einer Biga, einem italienischen Vorteig. Es gibt aber auch andere Teigführungen.')],
    pairing='Tomaten, Basilikum und gutes Olivenöl passen ebenso wie gegrilltes Gemüse oder eine sommerliche Suppe.',
    recipe='https://www.chefkoch.de/rezepte/325981114933330/Ciabatta.html', recipe_title='Ciabatta', recipe_author='Chefkoch-Community', recipe_note='Ein Ciabatta mit Vorteig und Olivenöl – Zeit zum Reifen gehört dazu.',
    source='https://en.wikipedia.org/wiki/Ciabatta', source_title='Hintergrund: Herkunft des Ciabattas'),
  dict(slug='sauerteigbrot', name='Sauerteigbrot', region='Handwerk mit Zeit', origin='Viele Brotkulturen', grain='Weizen, Roggen oder Dinkel', taste='Vielschichtig & fein säuerlich', category_label='Kräftig & kernig',
    subtitle='Mehl, Wasser und Zeit. Den Rest macht die Kultur.',
    short='Eine lebendige Kultur, eine lange Reife. Sauerteig schenkt Brot Tiefe, Charakter und eine besondere Kruste.',
    alt='Angeschnittener handwerklicher Sauerteiglaib mit dunkler Kruste und offener Porung auf Backpapier',
    history_title='Eine lebendige Backtradition.',
    history=[
      'Sauerteig gehört zu den alten Methoden, Brotteig zu lockern. In einem Gemisch aus Mehl und Wasser arbeiten Hefen und Milchsäurebakterien zusammen. Die Hefen bilden Gas, das den Teig aufgehen lässt; die Bakterien bilden Säuren und beeinflussen so Geschmack und Teigeigenschaften.',
      'Anders als Weizen- oder Roggenbrot bezeichnet Sauerteigbrot zunächst eine Art der Teigführung, keine einzelne Getreideart. Man kann es aus Weizen, Roggen, Dinkel oder Mischungen backen. In vielen Regionen wird ein Teil des reifen Sauerteigs aufbewahrt und als Anstellgut für den nächsten Backtag weitergeführt.'
    ],
    properties=[('Zutaten', 'Mehl, Wasser, Salz und ein aktiver Sauerteig. Manche Rezepte enthalten zusätzlich Backhefe.'), ('Geschmack', 'Von mild und leicht fruchtig bis kräftig säuerlich – abhängig von Mehl, Temperatur und Reifezeit.'), ('Kruste', 'Oft kräftig und aromatisch gebacken. Form und Einschnitte beeinflussen, wie der Laib aufreißt.'), ('Krume', 'Bei Weizen häufig luftig und unregelmäßig, bei Roggen dichter und saftiger. Sauerteig legt keine feste Porung fest.')],
    facts=[('Eine Kultur, viele Helfer', 'Im Sauerteig leben Hefen und Milchsäurebakterien. Ihre Zusammenarbeit prägt Lockerung und Aroma.'), ('Immer wieder weiterführen', 'Ein Teil der Kultur wird mit frischem Mehl und Wasser gefüttert. So kann Anstellgut für weitere Backtage erhalten werden.'), ('Nicht immer sauer', 'Ein Sauerteigbrot muss nicht stark säuerlich schmecken. Temperatur, Reifezeit und die Pflege der Kultur verändern sein Aroma.')],
    pairing='Pur mit Butter entfaltet sich das Aroma besonders gut. Auch Pilze, kräftiger Käse oder geröstetes Gemüse passen.',
    recipe='https://www.chefkoch.de/rezepte/3249861483549117/Sauerteigbrot-Grundrezept.html', recipe_title='Sauerteigbrot Grundrezept', recipe_author='Igelfaenger', recipe_note='Ein Grundrezept mit Sauerteig-Vorteig und einer Mischung aus Roggen und Weizen.',
    source='https://www.bzfe.de/presse/pressemeldungen-archiv/was-machen-eigentlich-hefe-und-sauerteig', source_title='BZfE: Was machen Hefe und Sauerteig?'),
]

def header(current):
    def active(slug): return ' aria-current="page"' if current == slug else ''
    links = ''.join(f'<a href="{b["slug"]}.html"{active(b["slug"])}><span>{b["name"]}</span><span class="small-label">0{i+1}</span></a>' for i, b in enumerate(BREADS))
    return f'''<a class="skip-link" href="#inhalt">Zum Inhalt springen</a>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="index.html" aria-label="Brotwelten – Startseite">Brotwelten<span class="brand-mark" aria-hidden="true">.</span></a>
      <nav class="primary-nav" id="hauptnavigation" aria-label="Hauptnavigation">
        <a class="nav-link" href="index.html"{active('index')}>Startseite</a>
        <details class="bread-menu{' current' if current in [b['slug'] for b in BREADS] else ''}">
          <summary>Brotsorten {DOWN}</summary>
          <div class="dropdown">{links}</div>
        </details>
        <a class="nav-link" href="ueber-uns.html"{active('ueber-uns')}>Über uns</a>
      </nav>
    </div>
  </header>'''

def footer():
    links = '\n'.join(f'<a href="{b["slug"]}.html">{b["name"]}</a>' for b in BREADS)
    return f'''<footer class="site-footer">
    <div class="container">
      <div class="footer-top">
        <div class="footer-brand"><a class="brand" href="index.html">Brotwelten<span class="brand-mark" aria-hidden="true">.</span></a><p>Von Korn zu Kruste.<br>Geschichten, Wissen und die Vielfalt des Brotes.</p></div>
        <div><p class="footer-title">Die sieben Brotsorten</p><nav class="footer-links" aria-label="Alle Brotsorten">{links}</nav></div>
        <nav class="footer-project" aria-label="Projekt und Quellen"><p class="footer-title">Unser Projekt</p><a href="index.html">Startseite</a><a href="ueber-uns.html">Über uns</a><a href="ueber-uns.html#bildnachweise">Bildnachweise & Quellen</a><a href="ueber-uns.html#team">Das Team</a></nav>
      </div>
      <div class="footer-bottom"><span>© 2026 Brotwelten · Ein Projekt von Rico, Til und Otto</span><a href="#seitenanfang">Zurück nach oben ↑</a></div>
    </div>
  </footer>'''

def page(slug, title, description, body):
    document = f'''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta name="theme-color" content="#F8F5EF">
  <title>{title}</title>
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/css/fonts.css">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body id="seitenanfang">
  {header(slug)}
  <main id="inhalt">
{body}
  </main>
  {footer()}
</body>
</html>
'''
    (ROOT / (slug + '.html')).write_text(document, encoding='utf-8')

def image(slug, alt, cls='', lazy=True, small=False, wide=False):
    meta = METADATA[slug]
    sizes = '(max-width: 600px) calc(100vw - 46px), (max-width: 800px) calc(50vw - 41px), (max-width: 1100px) 29vw, 390px' if small and not wide else '(max-width: 600px) calc(100vw - 46px), 46vw'
    if cls == 'about-banner':
        sizes = '(max-width: 600px) calc(100vw - 46px), 90vw'
    return f'<img class="{cls}" src="assets/images/{slug}{"-small" if small else ""}.webp" srcset="assets/images/{slug}-small.webp {meta["small_width"]}w, assets/images/{slug}-medium.webp {meta["medium_width"]}w, assets/images/{slug}.webp {meta["width"]}w" sizes="{sizes}" width="{meta["width"]}" height="{meta["height"]}" alt="{escape(alt, quote=True)}" {"loading=\"lazy\"" if lazy else "fetchpriority=\"high\""} decoding="async">'

def card(b, i):
    return f'''<article class="bread-card{' featured' if i == 6 else ''}">
          <a class="card-photo" href="{b['slug']}.html" aria-label="{b['name']} entdecken">{image(b['slug'], b['alt'], small=True, wide=i == 6)}<span class="card-index" aria-hidden="true">0{i+1}</span></a>
          <div class="card-copy"><p class="image-source-note"><a href="ueber-uns.html#bildnachweise">Bildquelle</a> · {SOURCE_ACCESS_HTML}</p><div class="card-meta"><span>{b['region']}</span><span>{b['category_label']}</span></div>
          <h3><a href="{b['slug']}.html">{b['name']}</a></h3><p>{b['short']}</p><a class="text-link" href="{b['slug']}.html" aria-label="Mehr über {b['name']} erfahren">Mehr erfahren {ARROW}</a></div>
        </article>'''

def home():
    cards = '\n'.join(card(b, i) for i, b in enumerate(BREADS))
    features = ['Helle, lockere Krume', 'Saftige, eher dichte Krume', 'Schale, Keimling und Mehlkörper bleiben erhalten', 'Als helles Brot oder Vollkornbrot möglich', 'Schlanke Form mit viel knuspriger Kruste', 'Große, unregelmäßige Poren', 'Mit einer lebendigen Sauerteigkultur gebacken']
    comparison = '\n'.join(f'<tr><th scope="row"><a href="{b["slug"]}.html">{b["name"]}</a></th><td>{b["grain"]}</td><td>{b["taste"]}</td><td>{feature}</td></tr>' for b, feature in zip(BREADS, features))
    page('index', 'Brotwelten – Die Welt des Brotes.', 'Sieben Brotsorten. Sieben Geschichten. Entdecke Herkunft, Charakter und passende Rezepte – von Roggenbrot bis Ciabatta.', f'''
    <section class="hero container" aria-labelledby="hero-titel">
      <div class="hero-grid">
        <div class="hero-copy">
          <p class="eyebrow">Von Korn zu Kruste</p>
          <h1 id="hero-titel">Die Welt<br>des <em>Brotes.</em></h1>
          <p class="lead">Sieben Brotsorten. Sieben Geschichten. Entdecke die Vielfalt des Brotes – von traditionellem Roggenbrot bis zum italienischen Ciabatta.</p>
          <a class="button" href="#brotsorten">Brotsorten entdecken {DOWN}</a>
          <p class="hero-note">Ein kleines Stück Kultur. Jeden Tag.</p>
        </div>
        <figure class="hero-figure">
          {image('sauerteigbrot', BREADS[6]['alt'], 'hero-image', lazy=False)}
          <div class="hero-stamp" aria-hidden="true"><span>Mehl · Wasser</span><strong>& Zeit</strong><span>Gutes Handwerk</span></div>
          <figcaption class="photo-caption"><span>Die Schönheit des Einfachen</span><span>Foto: Vicky Ng</span><span class="source-access"><a href="ueber-uns.html#bildnachweise">Bildquelle</a> · {SOURCE_ACCESS_HTML}</span></figcaption>
        </figure>
      </div>
      <div class="intro-strip" aria-label="Was dich erwartet"><div><strong>07</strong><span>Brotsorten im Porträt</span></div><div><strong>Wissen</strong><span>Von Herkunft bis Handwerk</span></div><div><strong>Rezepte</strong><span>Zum Selberbacken</span></div></div>
    </section>
    <section class="collection container" id="brotsorten" aria-labelledby="sorten-titel">
      <div class="section-heading"><div><p class="eyebrow">Die Brotsammlung</p><h2 id="sorten-titel">Jedes Brot hat<br>seine <em>Geschichte.</em></h2></div><p>Hell oder dunkel. Mild oder kräftig.<br>Entdecke, was unsere sieben Brotsorten besonders macht.</p></div>
      <div class="collection-toolbar"><span class="result-count">7 Brotsorten im Überblick</span><a class="text-link" href="#brotvergleich">Brotsorten vergleichen {DOWN}</a></div>
      <div class="bread-grid" id="brotsammlung">{cards}</div>
    </section>
    <section class="comparison-section container" id="brotvergleich" aria-labelledby="vergleich-titel"><p class="eyebrow">Auf einen Blick</p><h2 id="vergleich-titel">Sieben Brote.<br>Viele <em>Unterschiede.</em></h2><p id="vergleich-hinweis">Typische Merkmale können je nach Rezept variieren. Vollkorn beschreibt die Bestandteile des Mehls, Sauerteig die Teigführung – ein Brot kann also zu mehreren Porträts passen.</p><p class="table-hint">Auf kleinen Bildschirmen lässt sich die Tabelle seitlich scrollen.</p><div class="table-scroll" tabindex="0" role="region" aria-label="Vergleich der sieben Brotsorten" aria-describedby="vergleich-hinweis"><table class="comparison-table"><caption>Getreide, Geschmack und Besonderheiten im Vergleich</caption><thead><tr><th scope="col">Brotsorte</th><th scope="col">Getreide / Basis</th><th scope="col">Geschmack</th><th scope="col">Besonderheit</th></tr></thead><tbody>{comparison}</tbody></table></div></section>
    <section class="story-section" aria-labelledby="geschichte-titel"><div class="container story-grid">
      <figure class="story-photo">{image('sauerteigbrot', BREADS[6]['alt'])}<figcaption>Wenige Zutaten. Viele Möglichkeiten.<span class="source-access"><a href="ueber-uns.html#bildnachweise">Bildquelle</a> · {SOURCE_ACCESS_HTML}</span></figcaption></figure>
      <div class="story-copy"><p class="eyebrow">Mehr als ein Lebensmittel</p><h2 id="geschichte-titel">Ein Stück Brot.<br>Ein Stück <em>Kultur.</em></h2><p>Mehl, Wasser, Salz und ein wenig Zeit: Aus wenigen Zutaten entsteht etwas, das Menschen seit Jahrtausenden begleitet. Brot gehört zum Alltag und erzählt zugleich von Landschaften, Getreide und handwerklichen Traditionen.</p><p>Ob kräftiges Roggenbrot im Norden oder luftiges Ciabatta in Italien – jede Region hat ihre eigenen Antworten auf eine einfache Frage: Wie wird aus Korn ein gutes Brot?</p><a class="text-link" href="ueber-uns.html">Die Idee hinter Brotwelten {ARROW}</a></div>
    </div></section>
    <section class="closing container" aria-labelledby="abschluss-titel"><p class="eyebrow">Wissen, das Appetit macht</p><h2 id="abschluss-titel">Neugierig geworden?<br>Dann <em>brich ein Stück ab.</em></h2><p>Jedes Brotporträt führt dich auch zu einem passenden Rezept.</p><a class="text-link" href="weizenbrot.html">Mit Weizenbrot beginnen {ARROW}</a></section>
''')

def breadpage(b, i):
    history = ''.join(f'<p>{p}</p>' for p in b['history'])
    properties = ''.join(f'<div><dt>{title}</dt><dd>{text}</dd></div>' for title, text in b['properties'])
    facts = ''.join(f'<article class="fact"><div class="fact-number" aria-hidden="true">0{n+1}</div><h3>{title}</h3><p>{text}</p></article>' for n, (title, text) in enumerate(b['facts']))
    nxt = BREADS[(i + 1) % len(BREADS)]
    page(b['slug'], b['name'] + ' – Herkunft, Charakter & Rezept | Brotwelten', b['short'], f'''
    <div class="container breadcrumb" aria-label="Brotkrümelnavigation"><a href="index.html">Startseite</a><span aria-hidden="true">/</span><a href="index.html#brotsorten">Brotsorten</a><span aria-hidden="true">/</span><span>{b['name']}</span></div>
    <section class="detail-hero container" aria-labelledby="brot-titel"><div class="hero-grid">
      <div class="hero-copy"><p class="eyebrow">Brotporträt 0{i+1} / 07</p><h1 id="brot-titel">{b['name']}</h1><p class="lead">{b['subtitle']}</p><a class="text-link" href="#geschichte">Die Geschichte entdecken {DOWN}</a><div class="bread-tags"><span>{b['region']}</span><span>{b['category_label']}</span></div></div>
      <figure class="hero-figure">{image(b['slug'], b['alt'], 'hero-image', lazy=False)}<figcaption class="photo-caption"><span>{b['name']} · Eine von vielen Varianten</span><a href="ueber-uns.html#bildnachweise">Bildnachweis ↗</a><span class="source-access">{SOURCE_ACCESS_HTML}</span></figcaption></figure>
    </div></section>
    <div class="container"><dl class="at-a-glance"><div><dt>Verwurzelt in</dt><dd>{b['origin']}</dd></div><div><dt>Im Mittelpunkt</dt><dd>{b['grain']}</dd></div><div><dt>Der Charakter</dt><dd>{b['taste']}</dd></div></dl>
      <section class="article-section" id="geschichte" aria-labelledby="geschichte-titel"><div><p class="eyebrow">Herkunft & Geschichte</p><h2 id="geschichte-titel">{b['history_title']}</h2></div><div class="article-copy">{history}<p class="source-note">Zum Weiterlesen: <a href="{b['source']}" target="_blank" rel="noopener noreferrer">{b['source_title']} ↗</a><span class="source-access">{SOURCE_ACCESS_HTML}</span></p></div></section>
      <section class="article-section" aria-labelledby="charakter-titel"><div><p class="eyebrow">Von außen nach innen</p><h2 id="charakter-titel">Das macht<br>es <em>besonders.</em></h2><p class="pairing-note">{b['pairing']}</p></div><dl class="properties">{properties}</dl></section>
      <section class="facts-section" aria-labelledby="fakten-titel"><p class="eyebrow">Eine Scheibe Wissen</p><h2 id="fakten-titel">Schon gewusst?</h2><div class="facts-grid">{facts}</div></section>
      <section class="recipe-section" aria-labelledby="rezept-titel"><div><p class="eyebrow">Vom Lesen zum Backen</p><h2 id="rezept-titel">Jetzt wird’s<br><em>handgemacht.</em></h2></div><div class="recipe-copy"><p>{b['recipe_note']} Das passende Rezept „{b['recipe_title']}“ findest du auf Chefkoch.</p><a class="button" href="{b['recipe']}" target="_blank" rel="noopener noreferrer">Rezept auf Chefkoch ansehen ↗</a><small>Externe Rezeptseite · öffnet in einem neuen Tab</small><small class="source-access">{SOURCE_ACCESS_HTML}</small></div></section>
      <nav class="page-return" aria-label="Weiter entdecken"><a class="back-link" href="index.html">← Zurück zur Startseite</a><a class="next-link" href="{nxt['slug']}.html"><span>Nächstes Brotporträt</span>{nxt['name']} →</a></nav>
    </div>
''')

LICENSE_URLS = {'CC BY 2.0': 'https://creativecommons.org/licenses/by/2.0/', 'CC BY-SA 2.0': 'https://creativecommons.org/licenses/by-sa/2.0/', 'CC BY-SA 3.0': 'https://creativecommons.org/licenses/by-sa/3.0/', 'CC BY-SA 4.0': 'https://creativecommons.org/licenses/by-sa/4.0/', 'CC0': 'https://creativecommons.org/publicdomain/zero/1.0/', 'CC0 1.0': 'https://creativecommons.org/publicdomain/zero/1.0/', 'Unsplash License': 'https://unsplash.com/license'}

def credits():
    entries = []
    for b in BREADS:
        m = METADATA[b['slug']]
        license_name = m['licenses'][0]
        license_url = LICENSE_URLS.get(license_name)
        if not license_url:
            raise ValueError('Document the actual license: ' + license_name)
        entries.append(f'<li><strong>{b["name"]}:</strong> <a href="{m["source"]}" target="_blank" rel="noopener noreferrer">{escape(m["title"])}</a> · {escape(m["author"])} · <a href="{license_url}" target="_blank" rel="noopener noreferrer">{license_name}</a>. Verkleinert und als WebP gespeichert; Bildausschnitt im Layout. Die jeweilige Lizenz gilt auch für unsere Bildfassung.<span class="source-access">{SOURCE_ACCESS_HTML} (Bildquelle und Lizenz).</span></li>')
    return '\n'.join(entries)

def about():
    members = [
        ('Rico', 'Leading Developer', 'Die technische Umsetzung geleitet und den Großteil der Website programmiert.'),
        ('Til', 'Bildrecherche & Designideen', 'Bilder ausgewählt, Designideen vorgeschlagen und bei der Programmierung mitgeholfen.'),
        ('Otto', 'Bildrecherche & Designideen', 'Bilder ausgewählt, Designideen vorgeschlagen und bei der Programmierung mitgeholfen.'),
    ]
    team = ''.join(
        f'<article class="team-member"><span class="team-number" aria-hidden="true">0{i}</span><h3>{name}</h3><p class="team-role">{escape(role)}</p>'
        + (f'<p class="team-contribution">{escape(contribution)}</p>' if contribution else '')
        + '</article>'
        for i, (name, role, contribution) in enumerate(members, start=1)
    )
    reading = ''.join(f'<li><a href="{b["source"]}" target="_blank" rel="noopener noreferrer">{b["source_title"]} ↗</a><span class="source-access">{SOURCE_ACCESS_HTML}</span></li>' for b in BREADS)
    page('ueber-uns', 'Über unser Projekt | Brotwelten', 'Brotwelten ist ein gemeinsames Projekt von Rico, Til und Otto. Entdecke sieben Brotsorten, ihre Herkunft, typische Eigenschaften und passende Rezeptlinks.', f'''
    <div class="container breadcrumb"><a href="index.html">Startseite</a><span aria-hidden="true">/</span><span>Über uns</span></div>
    <div class="container"><section class="about-hero" aria-labelledby="projekt-titel"><p class="eyebrow">Unser Projekt</p><h1 id="projekt-titel">Drei Köpfe.<br>Eine gemeinsame <em>Idee.</em></h1><p class="lead">Wir sind Rico, Til und Otto. Mit Brotwelten geben wir einen Einblick in die Vielfalt des Brotes – von Herkunft und Handwerk bis zu typischen Eigenschaften.</p></section>
    <figure class="about-photo">{image('sauerteigbrot', BREADS[6]['alt'], 'about-banner', lazy=False)}<figcaption class="source-access"><a href="#bildnachweise">Bildquelle</a> · {SOURCE_ACCESS_HTML}</figcaption></figure>
    <section class="about-intro" aria-labelledby="idee-titel"><div><p class="eyebrow">Die Idee dahinter</p><h2 id="idee-titel">Brotwelten.<br>Von Korn zu <em>Kruste.</em></h2></div><div><p>Brot gehört zum Alltag und hat viele Facetten. Mit Brotwelten möchten wir zeigen, wie unterschiedlich Brote in Herkunft, Zutaten und Geschmack sein können.</p><p>Wir stellen sieben Brotsorten mit ihrer Herkunft und ihren typischen Eigenschaften vor. Dazu haben wir passende Rezeptlinks auf Chefkoch und echte Fotografien ausgewählt. Die verwendeten Quellen und Bildnachweise sind dokumentiert.</p><p>Die Porträts sollen neugierig machen: auf neue Sorten, traditionelle Herstellung und die Geschichten hinter einem alltäglichen Lebensmittel.</p></div></section>
    <section class="team-section" id="team" aria-labelledby="team-titel"><p class="eyebrow">Gemeinsam umgesetzt</p><h2 id="team-titel">Unser kleines Team.</h2><div class="team-grid">{team}</div></section>
    <section class="tech-section" aria-labelledby="technik-titel"><p class="eyebrow">Was dahintersteckt</p><h2 id="technik-titel">Mit den Grundlagen gebaut.</h2><div class="tech-list"><article><h3>HTML5</h3><p>Neun eigenständige Seiten: die Startseite, sieben Brotporträts und „Über uns“ mit unserem Team. Alle Seiten sind miteinander verlinkt.</p></article><article><h3>CSS3</h3><p>Gemeinsame Farben und Schriften, flexible Raster und ein Layout für große und kleine Bildschirme.</p></article></div></section>
    <section class="credits-section" id="bildnachweise" aria-labelledby="quellen-titel"><p class="eyebrow">Transparent dokumentiert</p><h2 id="quellen-titel">Echte Bilder. Klare Quellen.</h2><p>Alle Brotaufnahmen sind Fotografien. Die Bilder wurden von Wikimedia Commons beziehungsweise Unsplash bezogen und lokal gespeichert. Das Sauerteigfoto erscheint auch auf der Startseite und als Projektmotiv.</p><p>Die Abrufdaten nennen den letzten Quellenaufruf für diese Projektarbeit.</p><ul class="credits-list">{credits()}</ul><p>Schriften: <strong>Libre Caslon Display</strong> und <strong>DM Sans</strong>, lokal eingebunden. Beide stehen unter der <a href="assets/fonts/librecaslondisplay-OFL.txt">SIL Open Font License</a>; die <a href="assets/fonts/dmsans-OFL.txt">Lizenz von DM Sans</a> liegt ebenfalls im Projekt.<span class="source-access">Schriftquellen · {SOURCE_ACCESS_HTML}.</span></p><p>Hintergrundinformationen zum Weiterlesen:</p><ul class="reading-list">{reading}</ul><p>Ausführliche Bildangaben stehen zusätzlich in <a href="BILDQUELLEN.md">BILDQUELLEN.md</a>. Rezeptquellen und Prüfumfang sind in <a href="QUELLEN.md">QUELLEN.md</a> dokumentiert.</p></section>
    <nav class="page-return" aria-label="Zurück zum Entdecken"><a class="back-link" href="index.html">← Zurück zur Startseite</a><a class="text-link" href="index.html#brotsorten">Die sieben Brotsorten {ARROW}</a></nav></div>
''')

def documentation():
    lines = ['# Bildquellen – Brotwelten', '', 'Bilder heruntergeladen am 30. Oktober 2026. ' + SOURCE_ACCESS_TEXT + ' (Bildquellen und Lizenzen).', '', 'Ausschließlich echte Fotografien. Originalaufnahmen wurden verkleinert und als WebP komprimiert; das Layout beschneidet sie mit `object-fit: cover`. Die unten angegebene Lizenz gilt jeweils auch für die optimierte Bildfassung. Fotografen, Originalseiten und Lizenzen sind zusätzlich auf `ueber-uns.html#bildnachweise` verlinkt.', '']
    for b in BREADS:
        m = METADATA[b['slug']]
        lic = m['licenses'][0]
        lines += [f'## {b["name"]}', f'- Dateien: `assets/images/{b["slug"]}.webp`, `assets/images/{b["slug"]}-small.webp`, `assets/images/{b["slug"]}-medium.webp`', f'- Originaltitel: {m["title"]}', f'- Urheber: {m["author"]}', f'- Originalseite: {m["source"]}', f'- Bilddatei der Quelle: {m["original"]}', f'- Verwendete Lizenz: [{lic}]({LICENSE_URLS[lic]})', f'- {SOURCE_ACCESS_TEXT} (Originalseite und Lizenz).', f'- Optimierte große Fassung: {m["width"]} × {m["height"]} px.', '']
    lines += ['Das Sauerteigmotiv wird auf mehreren Seiten verwendet. Zu jedem Foto liegen eine kleine, eine mittlere und eine große WebP-Fassung vor; der Browser wählt die passende Größe.', '', '## Schriften', '- Libre Caslon Display: https://fonts.google.com/specimen/Libre+Caslon+Display – ' + SOURCE_ACCESS_TEXT + '.', '- DM Sans: https://fonts.google.com/specimen/DM+Sans – ' + SOURCE_ACCESS_TEXT + '.', '- Bezogen über Google Fonts, lokal eingebunden. SIL Open Font License 1.1; Lizenzdateien unter `assets/fonts/`.', '', 'Das kleine typografische Favicon ist projektintern als SVG angelegt; es enthält kein Brotfoto.']
    (ROOT / 'BILDQUELLEN.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    lines = ['# Inhalts- und Rezeptquellen', '', 'Erste Recherche am 30. Oktober 2026. ' + SOURCE_ACCESS_TEXT + ' (Informations- und Rezeptquellen). Die Texte sind eigenständig formuliert. Es werden keine vollständigen Chefkoch-Rezepte oder deren Bilder übernommen.', '', '## Chefkoch-Rezepte', '', 'Die folgenden konkreten Rezeptseiten wurden bei der Recherche über Chefkoch-Suchergebnisse und die auslesbaren Seiteninhalte geprüft. Externe Websites können später ihre Inhalte, URLs oder Zugangsbedingungen ändern.', '']
    for b in BREADS:
        lines.append(f'- **{b["name"]}:** [{b["recipe_title"]}]({b["recipe"]}) – {b["recipe_note"]} {SOURCE_ACCESS_TEXT}.')
    lines += ['', '## Hintergrundinformationen', '']
    for b in BREADS:
        lines.append(f'- {b["name"]}: [{b["source_title"]}]({b["source"]}) – {SOURCE_ACCESS_TEXT}.')
    lines += ['', 'Die Herkunft vieler Brottraditionen lässt sich nicht auf einen einzelnen Ort oder Erfinder zurückführen. Entsprechend sind die historischen Texte zurückhaltend formuliert. Die sieben Porträts sind keine überschneidungsfreien Kategorien: Ein Brot kann zum Beispiel zugleich Dinkel-, Vollkorn- und Sauerteigbrot sein.']
    (ROOT / 'QUELLEN.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

if __name__ == '__main__':
    METADATA = json.loads((ROOT / 'tools/image-metadata.json').read_text(encoding='utf-8'))
    home()
    for i, bread in enumerate(BREADS):
        breadpage(bread, i)
    about()
    documentation()
    print('Generated nine independent HTML pages and source documentation.')
