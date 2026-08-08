## 1. Configurer release-please

- [x] 1.1 Créer `release-please-config.json` : `release-type: simple`, et `extra-files` pointant `.claude-plugin/plugin.json` sur le champ `version` (décision D5)
- [x] 1.2 Y déclarer `changelog-sections` de sorte que `docs`, `refactor`, `test` et `chore` soient visibles et déclenchent un correctif — contre le défaut de l'outil, qui ne publie que sur `feat`, `fix` et `BREAKING` (décision D2, exigence « Les types correctifs du dépôt déclenchent une publication »)
- [x] 1.3 Créer `.release-please-manifest.json` initialisé à la version courante, `0.4.1`
- [x] 1.5 Activer `bump-minor-pre-major` — sous `1.0.0`, une rupture produit un mineur. Empêche qu'une 1.0 soit atteinte par accumulation mécanique, ce que le README récuse explicitement. Ne supersède pas `adr/0002`, qui n'affirme aucune correspondance normative : c'est un raffinement de sa configuration
- [x] 1.4 Créer `.github/workflows/release-please.yml` — premier `.github/` du dépôt, à déclarer comme tel dans le message de commit

## 2. Écrire ce que la dérivation ne voit pas

- [x] 2.1 Ajouter en tête du `CHANGELOG.md` généré une ligne renvoyant à `openspec/changes/archive/` : ce fichier est un index des publications, pas le journal de bord du dépôt (décision D4)
- [x] 2.2 Amender le § Versions du `README.md` : le tableau devient la **description de la configuration** de l'outil et cesse d'être la règle souveraine. Retirer la phrase « Ce tableau fait foi, pas la colonne de droite », qui devient fausse
- [x] 2.3 Ajouter à la section « Convention de commit » la règle qui protège l'autorité des types : *si le numéro calculé paraît faux, on corrige le commit fautif, jamais le numéro dans la demande de publication* (décision D3)
- [x] 2.4 Écrire au README la limite acceptée : un `feat` posé là où il fallait `feat!` produit une version fausse et rien ne le signale (exigence « Ce que la dérivation ne sait pas voir »)

## 3. Première publication

*Non exécutable localement : exige que le workflow tourne sur GitHub. À reprendre après publication de la branche.*

- [x] 3.1 Vérifier que la demande de publication ouverte propose un numéro dérivé de l'historique, et **non `1.0.0`**. Constaté : elle a proposé `0.4.2` sur deux commits `docs`, puis **recalculé `0.5.0`** quand `feat(sentinelle)` a atterri sur `main`. La dérivation suit l'historique, ce que cette tâche voulait voir. **Le contrôle de `bump-minor-pre-major` reste à faire** : la plage `v0.4.1..v0.5.0` ne contient aucun commit de rupture, et un `feat` ordinaire aurait donné `0.5.0` avec ou sans l'option. Le premier `feat!` sera le vrai contrôle
- [x] 3.2 Vérifier qu'aucune balise n'est posée et que `plugin.json` n'est pas modifié sur `main` tant que la demande n'est pas fusionnée (exigence « La publication reste soumise à une décision humaine »). Constaté sur la demande #4 restée ouverte : aucune balise, `plugin.json` et le manifeste à `0.4.1`
- [x] 3.3 Fusionner, puis vérifier que `plugin.json` porte le numéro calculé et que la balise existe. Constaté après fusion de #4 : `plugin.json` et `.release-please-manifest.json` à **`0.5.0`**, balise `v0.5.0` posée, `CHANGELOG.md` créé
- [ ] 3.4 Décider si le correctif du journal de la sentinelle — fusionné avant l'adoption, sujet sans type, donc invisible à l'outil — doit être mentionné à la main dans les notes de cette première publication. Constaté : il est **absent du `CHANGELOG.md` généré**, conséquence directe du garde-fou n°4 d'`adr/0002`. La décision reste entière

## 4. Contrôles de l'ADR

- [x] 4.1 Cohérence règle/outil : la table du README et `release-please-config.json` listent les mêmes types pour les mêmes niveaux
- [x] 4.2 Numéro jamais corrigé à la main : `git log -p -- .claude-plugin/plugin.json` ne montre que des commits de publication touchant `version`
- [x] 4.3 Ouvrir un ADR sur la politique de branches — release-please suppose une branche par défaut et des demandes de publication, le dépôt pousse en direct. Fait : [`adr/0003-politique-de-branche.md`](../../../adr/0003-politique-de-branche.md), accepté sans superséder `adr/0002`, qu'il complète sur ce que celui-ci avait laissé ouvert
