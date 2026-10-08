"""Construit le portfolio statique de Clive Gouala (aucune dépendance externe)."""
from __future__ import annotations

import html
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PROJECTS = [
    dict(slug="interim-industries", title="Interim Industries", category="Logos", cover=6,
         images=[6], intro="Un logo industriel décliné en versions monochromes, textile et accessoires.",
         scope="Logo, déclinaisons, applications"),
    dict(slug="ng-photography", title="NG Photography", category="Logos", cover=7,
         images=[7], intro="Une identité pour la photographie, du monogramme aux supports de marque.",
         scope="Monogramme, palette, supports"),
    dict(slug="la-marque", title="La Marque", category="Logos", cover=8,
         images=[8, 21], intro="Une identité vestimentaire déclinée du logotype aux publications sociales.",
         scope="Logo, textile, réseaux sociaux"),
    dict(slug="so-sweet", title="So Sweet", category="Logos", cover=9,
         images=[9], intro="Un univers graphique gourmand présenté sur des supports variés.",
         scope="Logo, couleur, applications"),
    dict(slug="sigmos-agency", title="Sigmos Agency", category="Identité", cover=11,
         images=[11, 12, 13, 19], intro="Une identité de marque construite autour d'un symbole, d'une palette et de ses usages.",
         scope="Identité, charte, communication"),
    dict(slug="les-delices-de-md", title="Les Délices de MD", category="Packaging", cover=25,
         images=[14, 15, 23, 24, 25], intro="Une marque gourmande déclinée en identité, bouteilles et packagings fruités.",
         scope="Branding, packaging, étiquettes"),
    dict(slug="mascotte-btp", title="Mascotte BTP", category="Identité", cover=17,
         images=[17], intro="Du croquis au personnage final : un poulpe ouvrier conçu autour de la polyvalence.",
         scope="Recherche, illustration, mascotte"),
    dict(slug="believe-agency", title="Believe Agency", category="Social media", cover=20,
         images=[20], intro="Des déclinaisons de marque pensées pour les publications et les couvertures sociales.",
         scope="Publications, habillage social"),
    dict(slug="canaan-holding", title="Canaan Holding", category="Édition", cover=28,
         images=[27, 28, 29], intro="Une brochure de présentation où la stratégie rencontre l'univers audiovisuel.",
         scope="Brochure, édition, mise en page"),
    dict(slug="photographie-editoriale", title="Photographie éditoriale", category="Photographie", cover=31,
         images=[31], intro="Une série de portraits en extérieur, entre couleur, mouvement et lumière naturelle.",
         scope="Portrait, direction visuelle"),
    dict(slug="affiches-sigmos", title="Affiches & création", category="Social media", cover=32,
         images=[32], intro="Une sélection de compositions graphiques, affiches et essais visuels du book.",
         scope="Affiches, composition graphique"),
]
IMAGE_DESCRIPTIONS = {
    6: "Interim Industries : logo bleu à engrenage, variantes noir et blanc et applications sur textile et accessoires.",
    7: "NG Photography : monogramme géométrique noir, palette bleue, cordon et déclinaisons du logo sur supports.",
    8: "La Marque : logo au cintre blanc sur fond marine, avec déclinaisons sur t-shirts, casquette et boutique.",
    9: "So Sweet : identité pâtisserie verte et dorée, logo gourmand, sac, t-shirt et palette de couleurs.",
    11: "Sigmos Agency : symbole blanc et nom de la marque sur une photographie sombre de projecteur de cinéma.",
    12: "Sigmos Agency : construction du symbole, déclinaisons bleues, gamme chromatique et police Poppins.",
    13: "Sigmos Agency : déclinaisons de marque sur publication, cordon, papeterie et polo bleu et blanc.",
    14: "Les Délices de MD : logo illustré de fruits et portrait souriant, sur fond violet traversé de rubans orange.",
    15: "Les Délices de MD : variantes du logo, codes couleurs et applications sur bouteilles, casquette et textile.",
    17: "Mascotte BTP : plusieurs croquis au crayon d'un poulpe ouvrier et illustration finale avec outils de chantier.",
    19: "Sigmos Agency : sélection de visuels sociaux avec maquettes Facebook et Instagram et affiches événementielles.",
    20: "Believe Agency : publications Instagram, couverture Facebook et visuels de services à dominante verte et marine.",
    21: "La Marque : trois publications sociales montrant une casquette, une photographie de mode et des t-shirts.",
    23: "Les Délices de MD : trois pots de fruits étiquetés Pomme, Orange et Goyave sur fond lumineux.",
    24: "Les Délices de MD : packaging Pomme, Orange et Goyave présenté sur trois fonds colorés distincts.",
    25: "Les Délices de MD : trio de pots fruités sur fonds rouge, vert et orange, avec étiquettes assorties.",
    27: "Canaan Holding : brochure ouverte avec couverture audiovisuelle, photographies et pages intérieures imprimées.",
    28: "Canaan Holding : doubles pages de brochure corporate montrant stratégie, production et coordonnées.",
    29: "Canaan Holding : couverture de brochure avec caméra de cinéma et portrait d'homme d'affaires.",
    31: "Photographie éditoriale : série de cinq portraits d'une femme sur une plage, foulard rouge et mer en arrière-plan.",
    32: "Affiches et création : montage d'affiches événementielles, recherches de logo et mockups de sweat à capuche.",
}
CATEGORIES = ["Tous", "Logos", "Identité", "Social media", "Packaging", "Édition", "Photographie"]


def e(value: object) -> str:
    return html.escape(str(value), quote=True)


def picture(number: int, alt: str, *, loading="lazy", class_name="") -> str:
    alt = IMAGE_DESCRIPTIONS.get(number, alt)
    return (f'<img class="{e(class_name)}" src="/assets/media/folio-{number:02d}.webp" '
            f'alt="{e(alt)}" loading="{loading}" width="1600" height="900">')


def layout(title: str, description: str, active: str, body: str) -> str:
    nav = "".join(f'<a href="/{href}" {"aria-current=\"page\"" if active == href else ""}>{label}</a>'
                  for href, label in [("index.html", "Accueil"), ("projets.html", "Projets"),
                                      ("a-propos.html", "À propos"), ("contact.html", "Contact")])
    return f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{e(description)}"><meta name="robots" content="noindex, nofollow">
<title>{e(title)} · Clive Gouala</title><link rel="stylesheet" href="/assets/style.css">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"></head>
<body><a class="skip" href="#contenu">Aller au contenu</a>
<header class="site-header"><div class="shell nav-shell"><a class="wordmark" href="/index.html" aria-label="Clive Gouala, accueil">CLIVE<span>GOUALA</span><i>®</i></a>
<button class="menu-toggle" type="button" aria-label="Ouvrir le menu" aria-controls="nav" aria-expanded="false"><span></span><span></span></button>
<nav class="nav" id="nav" aria-label="Navigation principale">{nav}</nav><a class="header-cta" href="/contact.html">Parlons projet <span aria-hidden="true">↗</span></a></div></header>
<main id="contenu">{body}</main>
<footer class="footer"><div class="shell"><div class="footer-top"><p>Une idée en tête ?<br><a href="mailto:sigmosart@gmail.com">Créons quelque chose <span>ensemble ↗</span></a></p></div>
<div class="footer-bottom"><span>© Clive Gouala · Portfolio</span><span>Réalisateur vidéo · Designer graphique · Photographe</span><a href="#contenu">Retour en haut ↑</a></div></div></footer>
<script src="/assets/app.js" defer></script></body></html>'''


def card(p: dict, index: int, featured=False) -> str:
    image = picture(p['cover'], f"Planche du projet {p['title']} : {p['scope']}")
    return f'''<article class="project-card {'featured' if featured else ''}" data-category="{e(p['category'])}">
<a class="project-link" href="/projets/{e(p['slug'])}.html" aria-label="Voir le projet {e(p['title'])}">
<div class="project-image">{image}<span class="card-arrow" aria-hidden="true">↗</span></div>
<div class="project-meta"><span>{index:02d} / {e(p['category'])}</span><span>{e(p['scope'])}</span></div>
<h3>{e(p['title'])}</h3></a></article>'''


def home() -> str:
    work = ''.join(card(p, i + 1, i == 0) for i, p in enumerate(PROJECTS[:6]))
    categories = ''.join(f'<span>{e(c)}</span>' for c in CATEGORIES[1:])
    body = f'''<section class="hero shell"><div class="hero-copy"><p class="eyebrow"><span class="eyebrow-dot"></span>Portfolio créatif / 2026</p>
<h1>Des idées.<br>Des images.<br><em>De l'impact.</em></h1>
<p class="hero-intro">Je suis Clive Gouala. Je donne forme aux identités, aux images et aux histoires qui méritent d'être vues.</p>
<div class="hero-actions"><a class="button button-primary" href="/projets.html">Explorer mon travail <span aria-hidden="true">↗</span></a><a class="text-link" href="/a-propos.html">Faire connaissance <span aria-hidden="true">↗</span></a></div>
<div class="hero-bottom"><span>Réalisateur vidéo<br>Designer graphique<br>Photographe</span><span>Défiler pour explorer ↓</span></div></div>
<div class="hero-visual"><div class="hero-photo"><img src="/assets/media/hero-photo.webp" width="593" height="950" alt="Photographie éditoriale de la série plage figurant dans le portfolio de Clive Gouala" fetchpriority="high"></div>
<div class="hero-stamp" aria-hidden="true"><span>CREATIVE<br>VISION</span><b>CG.</b></div><span class="vertical-caption">L'IMAGE A QUELQUE CHOSE À RACONTER · 2026</span></div></section>
<div class="marquee" role="group" aria-label="Domaines de création"><div class="shell">{categories}</div></div>
<section class="section shell" aria-labelledby="work-title"><div class="section-heading"><div><p class="kicker">01 / Sélection</p><h2 id="work-title">Projets <em>choisis.</em></h2></div><a class="text-link dark" href="/projets.html">Tout voir <span aria-hidden="true">↗</span></a></div>
<div class="project-grid">{work}</div><a class="mobile-more" href="/projets.html">Voir tous les projets ↗</a></section>
<section class="manifesto"><div class="shell manifesto-grid"><p class="kicker">02 / La démarche</p><div><p>Une belle image attire le regard.<br><em>Une intention claire</em> lui donne du sens.</p>
<a class="button button-outline" href="/a-propos.html">Découvrir mon parcours ↗</a></div></div></section>
<section class="section shell discipline"><p class="kicker">03 / Domaines</p><h2>Des idées au <em>rendu final.</em></h2>
<div class="discipline-list"><a href="/projets.html#filtre=Identit%C3%A9">01 <strong>Identité &amp; branding</strong><span>↗</span></a><a href="/projets.html#filtre=%C3%89dition">02 <strong>Design graphique &amp; print</strong><span>↗</span></a><a href="/projets.html#filtre=Photographie">03 <strong>Photographie &amp; vidéo</strong><span>↗</span></a></div></section>'''
    return layout('Accueil', 'Clive Gouala : vidéo, design graphique, photographie. Découvrez une sélection de réalisations.', 'index.html', body)


def projects_page() -> str:
    filters = ''.join(f'<button type="button" data-filter="{e(c)}" aria-pressed="{str(c == "Tous").lower()}">{e(c)}</button>' for c in CATEGORIES)
    cards = ''.join(card(p, i + 1) for i, p in enumerate(PROJECTS))
    body = f'''<section class="page-intro shell"><p class="kicker">Index / 01-{len(PROJECTS):02d}</p><h1>Un travail à <em>explorer.</em></h1>
<p>Identités, images, éditions et expériences visuelles. Parcourez les projets présentés dans mon book.</p></section>
<section class="section shell gallery-section" id="galerie" aria-label="Galerie de projets"><div class="filters" role="group" aria-label="Filtrer les projets">{filters}</div>
<p class="result-count" aria-live="polite">{len(PROJECTS)} projets</p><div class="project-grid gallery-grid">{cards}</div><p class="empty" hidden>Aucun projet dans cette catégorie.</p></section>'''
    return layout('Projets', 'Parcourez les réalisations de Clive Gouala : logos, identité, packaging, photographie et édition.', 'projets.html', body)


def project_page(p: dict, index: int) -> str:
    prev = PROJECTS[(index - 1) % len(PROJECTS)]
    nxt = PROJECTS[(index + 1) % len(PROJECTS)]
    images = ''.join(f'<figure class="case-figure"><a href="/assets/media/folio-{n:02d}.webp" target="_blank" rel="noopener" aria-label="Agrandir la planche {i + 1} de {e(p["title"])}">{picture(n, f"Planche {i + 1} du projet {p["title"]}")}</a><figcaption>Planche {i + 1:02d} / {e(p["title"])} · ouvrir en grand</figcaption></figure>' for i, n in enumerate(p['images']))
    body = f'''<div class="case-head shell"><a class="back-link" href="/projets.html">← Tous les projets</a><p class="kicker">{e(p['category'])} / Projet {index + 1:02d}</p>
<h1>{e(p['title'])}<span class="orange-dot">.</span></h1><div class="case-details"><p>{e(p['intro'])}</p><dl><div><dt>Discipline</dt><dd>{e(p['category'])}</dd></div><div><dt>Présenté dans le book</dt><dd>{e(p['scope'])}</dd></div></dl></div></div>
<div class="case-media shell">{images}</div><nav class="case-pagination shell" aria-label="Projets adjacents"><a href="/projets/{e(prev['slug'])}.html"><small>← Projet précédent</small><strong>{e(prev['title'])}</strong></a><a href="/projets/{e(nxt['slug'])}.html"><small>Projet suivant →</small><strong>{e(nxt['title'])}</strong></a></nav>'''
    return layout(p['title'], p['intro'], 'projets.html', body)


def about() -> str:
    body = '''<section class="page-intro shell about-intro"><p class="kicker">À propos / Le créateur derrière les images</p>
<h1>Curieux de nature.<br><em>Créatif par choix.</em></h1></section>
<section class="about-main shell"><div class="about-portrait"><img src="/assets/media/clive-portrait.webp" width="480" height="900" alt="Portrait en noir et blanc de Clive Gouala" loading="eager"><span>Clive Gouala / Créateur visuel</span></div>
<div class="about-copy"><p class="kicker">La personne & la pratique</p><h2>Bonjour, moi<br>c'est <em>Clive.</em></h2>
<p>Réalisateur vidéo, designer graphique et photographe, je travaille à la rencontre de l'image, de la marque et du récit.</p>
<p>Dans mon book, chaque projet raconte une approche : observer, expérimenter, puis trouver une forme qui sert vraiment l'idée.</p>
<p>Mes inspirations viennent aussi de l'architecture, de la mode et de la décoration. Elles nourrissent une pratique qui passe du logo à la photographie, des supports imprimés aux contenus digitaux.</p>
<a class="button button-primary" href="/contact.html">Discutons de votre projet ↗</a></div></section>
<section class="section shell about-skills"><p class="kicker">Outils & savoir-faire</p><h2>Une pratique <em>transversale.</em></h2>
<div class="skills-columns"><div><h3>Ce que je crée</h3><ul><li>Identités de marque & logotypes</li><li>Supports imprimés & packaging</li><li>Contenus pour les réseaux sociaux</li><li>Photographie & réalisation vidéo</li></ul></div><div><h3>Outils présents dans mon book</h3><ul><li>Photoshop · Illustrator · InDesign</li><li>Premiere Pro · DaVinci Resolve</li><li>After Effects · Blender</li></ul></div></div></section>'''
    return layout('À propos', 'Rencontrez Clive Gouala, réalisateur vidéo, designer graphique et photographe.', 'a-propos.html', body)


def contact() -> str:
    body = '''<section class="contact-page shell"><p class="kicker">Le prochain projet / Ensemble</p><h1>Une idée ?<br><em>Parlons-en.</em></h1>
<p>Une identité à inventer, des images à créer ou un projet à raconter ? Écrivez-moi directement.</p>
<a class="contact-mail" href="mailto:sigmosart@gmail.com">sigmosart@gmail.com <span aria-hidden="true">↗</span></a>
<div class="contact-note"><span>Réalisateur vidéo</span><span>Designer graphique</span><span>Photographe</span></div></section>'''
    return layout('Contact', 'Contactez Clive Gouala pour un projet de design, photographie ou réalisation vidéo.', 'contact.html', body)


def not_found() -> str:
    body = '''<section class="contact-page shell"><p class="kicker">Erreur 404</p><h1>Page<br><em>introuvable.</em></h1>
<p>Cette page n'existe pas ou a été déplacée.</p>
<a class="button button-primary" href="/projets.html">Voir les projets ↗</a></section>'''
    return layout('Page introuvable', 'Cette page est introuvable.', '', body)


def build_site(destination: Path) -> None:
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    assets = destination / 'assets'
    shutil.copytree(ROOT / 'assets', assets, dirs_exist_ok=True)
    for filename, content in [('index.html', home()), ('projets.html', projects_page()),
                              ('a-propos.html', about()), ('contact.html', contact()),
                              ('404.html', not_found())]:
        (destination / filename).write_text(content, encoding='utf-8')
    project_dir = destination / 'projets'
    project_dir.mkdir(exist_ok=True)
    for index, project in enumerate(PROJECTS):
        (project_dir / f"{project['slug']}.html").write_text(project_page(project, index), encoding='utf-8')
    # Hostinger (LiteSpeed/Apache) : servir index.html à la racine plutôt qu'un 403.
    (destination / '.htaccess').write_text('DirectoryIndex index.html\nOptions -Indexes\nErrorDocument 404 /404.html\n', encoding='utf-8')


if __name__ == '__main__':
    shutil.rmtree(ROOT / 'dist', ignore_errors=True)  # évite de publier des pages obsolètes
    build_site(ROOT / 'dist')
    files = sorted(f for f in (ROOT / 'dist').rglob('*') if f.is_file())
    for f in files:
        print(f"  {f.relative_to(ROOT / 'dist')}  ({f.stat().st_size // 1024} Ko)")
    print(f'Site prêt dans dist/ : {len(files)} fichiers')
