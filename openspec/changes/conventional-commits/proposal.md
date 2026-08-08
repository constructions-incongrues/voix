## Why

Les 41 messages de commit du dépôt sont des phrases françaises descriptives, sans aucun préfixe de type — mesuré : **0 sur 41**. C'est lisible par un humain et illisible par une machine : rien ne permet de dériver un niveau de version, de filtrer un historique, ou de générer un changelog. Le dépôt versionne pourtant selon des règles écrites et précises (README, § Versions), appliquées à la main à chaque publication.

Adopter Conventional Commits rend cette dérivation possible et fait entrer la convention **par décision** — ce que `REGISTRE.md` exige de tout ce qui prescrit une façon de travailler, après le retrait d'`openspec-git-discipline` arrivée par effet de bord.

## What Changes

- Tout commit à partir de l'adoption porte un préfixe `type(scope): description`, selon la spécification Conventional Commits 1.0.0.
- Un **tableau de correspondance** relie les types aux trois niveaux de version du dépôt (majeure / mineure / corrective), qui restent la source d'autorité — la convention les sert, elle ne les remplace pas.
- La **description reste une phrase française portant un constat**, pas une étiquette de catégorie. Le type contraint le préfixe, jamais ce que la phrase sait dire.
- Un jeu de **scopes fermé**, tiré des objets réels du dépôt : `voix`, `sentinelle`, `registre`, `plugin`, `specs`, `mesure`.
- Aucune réécriture de l'historique. Les 41 commits existants restent tels quels, comme les archives : *« les réécrire pour qu'ils aient l'air à jour serait falsifier un dossier »*.
- Aucun outil de vérification n'est ajouté en v1 — voir `design.md` pour le déclencheur qui rouvrirait la question.

## Capabilities

### New Capabilities
- `convention-commits`: ce qu'un message de commit doit satisfaire pour être admis, la correspondance avec les trois niveaux de version du dépôt, et ce que la convention n'a pas le droit d'écraser.

### Modified Capabilities

Aucune. Les huit capacités existantes portent sur les voix, le dispositif et la publication ; aucune ne décrit le travail de versionnement.

## Impact

- `README.md` § Versions — le tableau majeure/mineure/corrective gagne sa colonne de types.
- Une section « Convention de commit » à écrire, dans le README ou un `CONTRIBUTING.md`.
- L'historique **à partir de l'adoption** ; rien en amont.
- Aucun code, aucune dépendance, aucun outil. Le dépôt n'a aucune dépendance runtime et cette contrainte tient.
