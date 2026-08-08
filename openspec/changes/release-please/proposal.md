## Why

Le dépôt écrit désormais des commits conformes à Conventional Commits, mais **rien ne s'en sert**. Le numéro de version reste posé à la main dans `.claude-plugin/plugin.json`, il n'existe aucun `CHANGELOG.md`, aucune balise git, et aucune CI. La convention adoptée par `adr/0001` a créé la matière d'une automatisation sans construire l'automatisation — c'est un coût payé sans son bénéfice.

Preuve immédiate : les deux commits qui ont introduit la convention sont sur `main` depuis une heure, le tableau des Versions les classe *corrective*, et `0.4.1` n'a pas bougé.

## What Changes

- **release-please** publie le dépôt, via GitHub Action : il lit l'historique conforme, calcule le niveau, ouvre une PR de release, tient un `CHANGELOG.md`, met à jour `.claude-plugin/plugin.json` et pose la balise à la fusion.
- **BREAKING** — les types de commit deviennent **l'autorité** sur le niveau de version. Le tableau du README cesse de trancher et devient la description d'une configuration. Cela **supersède `adr/0001`**, dont le garde-fou n°2 posait l'inverse ; un `adr/0002` est requis, l'ADR précédent n'étant pas modifiable.
- Les types `docs`, `refactor`, `test` et `chore` sont configurés comme **déclencheurs de correctif**, contre le défaut de l'outil qui ne publie que sur `feat`, `fix` et `BREAKING`. Sans cela, les commits `docs(specs):` du dépôt ne produiraient aucune publication là où le README en voit une.
- Premier répertoire `.github/` du dépôt.
- Les trois autres garde-fous de `adr/0001` sont **maintenus** et repris explicitement par `adr/0002` : la description reste une phrase qui porte un constat, les jeux de types et de scopes restent fermés, l'historique antérieur n'est pas réécrit.

## Capabilities

### New Capabilities
- `publication-automatisee`: ce que la publication doit satisfaire quand elle est dérivée de l'historique — l'autorité des types, la correspondance avec les niveaux, ce qui est publié, et ce qui reste sous décision humaine.

### Modified Capabilities
- `publication-depot`: ce qui est publié gagne une clause de dérivation. La capacité décrit aujourd'hui les conditions de publication d'une critique ; elle doit dire que le numéro de version est désormais calculé et non posé.

## Impact

- `.github/workflows/` — création. Aucune CI n'existe à ce jour.
- `.claude-plugin/plugin.json` — le champ `version` passe sous la main de l'outil.
- `CHANGELOG.md` — création, et une question de cohabitation avec `openspec/changes/archive/`, qui est le journal de bord réel du dépôt. Traitée en design.
- `README.md` § Versions — le tableau change de statut : de règle souveraine à description de configuration.
- `adr/0002-release-please.md` — nouvel ADR, supersède `adr/0001`.
- **Aucune dépendance runtime.** release-please est une Action de CI ; la contrainte du dépôt (stdlib seulement, rien à installer pour l'usager) tient.
- La politique de branches, non tranchée au moment d'écrire, devenait un préalable : release-please travaille par PR de release sur une branche par défaut, alors que le dépôt avait poussé 40 commits en direct sur `main`. **Préalable levé** par `adr/0003`, qui tranche la question et exempte nommément la branche que release-please se nomme.
