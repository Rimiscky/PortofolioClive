# Portfolio web · Clive Gouala

Site éditorial statique et mobile-first basé sur le book PDF remis pour le projet. **Préversion à relire**, non publiée et non fusionnée.

## Parcours

- Accueil : direction créative et sélection de réalisations.
- Projets : galerie filtrable par discipline et 11 pages de réalisations individuelles. Les briefs et résultats clients restent à documenter avec Clive avant de présenter ces pages comme des études de cas.
- À propos : portrait, démarche et outils cités dans le book.
- Contact : lien direct vers l'adresse indiquée dans le book, sans formulaire ni collecte.

## Construire et prévisualiser

Python 3.12+ uniquement, aucune dépendance pour la production :

```sh
python3 scripts/build.py
python3 -m http.server 8000 --directory dist
```

Puis ouvrir `http://localhost:8000`.

## Déploiement Hostinger (`clive.rimiscky.fr`)

Hostinger copie la branche Git **telle quelle** dans `public_html`, sans étape de build. Les branches de code (`main`, `feat/…`) n'ont pas de `index.html` à la racine : les déployer directement donne une erreur **403 Forbidden**.

Le workflow `.github/workflows/hostinger.yml` construit le site à chaque push sur `main` (ou à la demande depuis l'onglet Actions) et publie le contenu de `dist/` sur la branche **`hostinger`**. Dans hPanel → Déploiements, sélectionner la branche `hostinger` puis « Redéployer ». Les liens et médias sont absolus depuis `/` : le site doit être servi à la racine du sous-domaine.

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
