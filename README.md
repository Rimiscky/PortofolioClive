# Portfolio web · Clive Gouala

Site éditorial statique et mobile-first basé sur le book PDF remis pour le projet. **Version de travail non déployée** : Rimiscky confirme l'accord de Clive pour présenter son portfolio personnel en ligne ; les éventuels droits de tiers et les coordonnées publiques restent à vérifier.

## Parcours

- Accueil : direction créative et sélection de réalisations.
- Projets : galerie filtrable par discipline et 11 pages de réalisations individuelles. Les images s'agrandissent dans une visionneuse avec touches fléchées, Échap et fermeture tactile ; le lien « Zoom HD » ouvre l'image originale pour examiner les détails. Les liens directs vers les fichiers restent fonctionnels sans JavaScript. Les briefs et résultats clients restent à documenter avec Clive avant de présenter ces pages comme des études de cas.
- À propos : portrait, démarche et outils cités dans le book.
- Contact : lien direct vers l'adresse indiquée dans le book, sans formulaire ni collecte.

## Construire et prévisualiser

Python 3.12+ uniquement, aucune dépendance pour la production :

```sh
python3 scripts/build.py
python3 -m http.server 8000 --directory dist
```

Puis ouvrir `http://localhost:8000`. Le domaine cible communiqué est **`clive.rimiscky.fr` (Hostinger)**, mais sa configuration et le déploiement restent à faire ultérieurement, avec autorisation distincte. L'hébergement statique doit servir **le contenu de `dist/` à la racine du sous-domaine** (les liens et médias sont absolus depuis `/`). Aucun workflow ne publie automatiquement le site.

## Tests

```sh
python3 -m unittest discover -s tests -v
```

Les tests d'interaction nécessitent `playwright` et Chromium (`python3 -m pip install playwright && python3 -m playwright install chromium`). Ils parcourent les liens/ressources et exercent les filtres, le menu, les animations, la visionneuse et le mode de mouvement réduit en navigateur réel.

## Contenu et validation avant publication

- Les 23 images WebP sont des extraits/recadrages optimisés du PDF « 2026 Portofolio CLG 2.pdf » transmis pour ce projet. Le PDF original, volumineux, n'est **pas** commité. Clive est d'accord pour présenter son portfolio personnel en ligne, selon la confirmation transmise par Rimiscky. Cet accord ne démontre pas à lui seul les éventuelles licences de photographies ou mockups créés par des tiers : en vérifier la provenance si de tels éléments figurent dans les planches.
- Les légendes synthétisent ce qui est visible dans les planches. Aucun chiffre d'audience, résultat commercial, témoignage ni date d'exécution n'est inventé.
- Vérifier avec Clive l'orthographe des marques, sa biographie et l'adresse de contact `sigmosart@gmail.com`. Les liens sociaux ne sont pas affichés faute d'URL confirmée ; aucun téléphone n'est repris.
- Toutes les pages contiennent `noindex, nofollow` jusqu'à la validation éditoriale et à une publication autorisée. `noindex` ne protège pas l'accès aux fichiers du dépôt public : vérifier la provenance des éventuels visuels de tiers avant le déploiement. Retirer la consigne d'indexation uniquement lors d'une publication autorisée.
- Pas de collecte, cookie, police distante, service tiers ni analytics. Le texte et les images restent sous la responsabilité de leurs ayants droit ; le code du site n'attribue pas de licence aux médias.
