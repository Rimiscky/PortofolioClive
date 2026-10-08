# Portfolio web · Clive Gouala

Site éditorial statique et mobile-first basé sur le book PDF remis pour le projet. **Préversion à relire**, non publiée et non fusionnée.

## Parcours

- Accueil : direction créative et sélection de réalisations.
- Projets : galerie filtrable par discipline et 11 études de cas individuelles.
- À propos : portrait, démarche et outils cités dans le book.
- Contact : lien direct vers l'adresse indiquée dans le book, sans formulaire ni collecte.

## Construire et prévisualiser

Python 3.12+ uniquement, aucune dépendance pour la production :

```sh
python3 scripts/build.py
python3 -m http.server 8000 --directory dist
```

Puis ouvrir `http://localhost:8000`. L'hébergement statique doit servir **le contenu de `dist/` à la racine du domaine** (les liens et médias sont absolus depuis `/`). Aucun workflow ne publie automatiquement le site.

## Tests

```sh
python3 -m unittest discover -s tests -v
```

Les tests d'interaction nécessitent `playwright` et Chromium (`python3 -m pip install playwright && python3 -m playwright install chromium`). Les tests parcourent les liens/ressources et exercent les filtres et le menu en navigateur réel.

## Contenu et validation avant publication

- Les 23 images WebP sont des extraits/recadrages optimisés du PDF « 2026 Portofolio CLG 2.pdf » transmis pour ce projet. Le PDF original, volumineux, n'est **pas** commité. Certaines planches contiennent des photographies et mockups dont les droits de diffusion en ligne sont à confirmer avec Clive avant déploiement.
- Les légendes synthétisent ce qui est visible dans les planches. Aucun chiffre d'audience, résultat commercial, témoignage ni date d'exécution n'est inventé.
- Vérifier avec Clive l'orthographe des marques, sa biographie et l'adresse de contact `sigmosart@gmail.com`. Les liens sociaux ne sont pas affichés faute d'URL confirmée ; aucun téléphone n'est repris.
- Toutes les pages contiennent `noindex, nofollow` tant que contenu, droits des visuels et destination de production ne sont pas approuvés. Retirer cette protection uniquement lors d'une publication autorisée.
- Pas de collecte, cookie, police distante, service tiers ni analytics. Le texte et les images restent sous la responsabilité de leurs ayants droit ; le code du site n'attribue pas de licence aux médias.
