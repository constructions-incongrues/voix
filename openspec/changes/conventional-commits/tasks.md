## 1. Documenter la convention

- [x] 1.1 Ajouter au `README.md` une section « Convention de commit » : la forme `type(scope): description`, le renvoi à Conventional Commits 1.0.0, et la règle que la description reste une phrase française portant un constat (exigence « La description reste une phrase qui porte un constat »)
- [x] 1.2 Y inscrire les deux jeux fermés — types `feat` `fix` `docs` `refactor` `test` `chore`, scopes `voix` `sentinelle` `registre` `plugin` `specs` `mesure` — et la règle qu'un ajout passe par une modification de la spec, jamais par un usage de fait
- [x] 1.3 Ajouter la colonne « Type » au tableau du § Versions, selon la table de correspondance de la spec, et écrire explicitement que le README fait foi en cas de conflit
- [x] 1.4 Écrire que l'historique antérieur à l'adoption n'est pas réécrit, et qu'un sujet sans type est *antérieur* et non *invalide* — avec le même motif que les archives, `openspec/changes/archive/`

## 2. Appliquer

- [ ] 2.1 Commiter les tâches du groupe 1 en respectant la convention — ce commit est le premier conforme et sert de cas d'usage : `docs(specs): la convention de commit entre au dépôt par décision`
- [ ] 2.2 Vérifier que le commit de 2.1 passe le contrôle de conformité de l'ADR : `git log --format='%s' -1 | grep -E '^(feat|fix|docs|refactor|test|chore)(\([a-z]+\))?!?: '`

## 3. Trancher les questions laissées ouvertes par le changement

- [ ] 3.1 Décider si le correctif de la sentinelle déjà parti en PR #1 est renommé avant fusion — il précède l'adoption, donc rien ne l'y oblige ; le laisser tel quel est cohérent avec la tâche 1.4
- [ ] 3.2 Décider du niveau de version que ce changement lui-même déclenche. Le cas est ambigu selon les règles du dépôt : la convention ne change aucune voix (donc pas majeure) et ne change pas ce que le dépôt *fait* (donc pas clairement mineure), mais elle n'est pas non plus « une formulation corrigée »

## 4. Bilan, après 20 commits conformes

- [ ] 4.1 Mesurer la conformité : `git log --format='%s' <sha-adoption>..HEAD | grep -cvE '^(feat|fix|docs|refactor|test|chore)(\([a-z]+\))?!?: '` doit rendre 0
- [ ] 4.2 Relire les 20 sujets et vérifier qu'aucun ne s'est réduit à une étiquette (le contrôle « non-aplatissement » de l'ADR)
- [ ] 4.3 Mesurer la part de `chore` — au-delà d'un commit sur cinq, ouvrir un ADR successeur ajustant le jeu de types
- [ ] 4.4 Compter les commits non conformes poussés sur `main` — à trois, construire le hook `commit-msg` en stdlib (déclencheur de réouverture de la décision D5)
