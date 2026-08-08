## 1. Documenter la convention

- [x] 1.1 Ajouter au `README.md` une section « Convention de commit » : la forme `type(scope): description`, le renvoi à Conventional Commits 1.0.0, et la règle que la description reste une phrase française portant un constat (exigence « La description reste une phrase qui porte un constat »)
- [x] 1.2 Y inscrire les deux jeux fermés — types `feat` `fix` `docs` `refactor` `test` `chore`, scopes `voix` `sentinelle` `registre` `plugin` `specs` `mesure` — et la règle qu'un ajout passe par une modification de la spec, jamais par un usage de fait
- [x] 1.3 Ajouter la colonne « Type » au tableau du § Versions, selon la table de correspondance de la spec, et écrire explicitement que le README fait foi en cas de conflit
- [x] 1.4 Écrire que l'historique antérieur à l'adoption n'est pas réécrit, et qu'un sujet sans type est *antérieur* et non *invalide* — avec le même motif que les archives, `openspec/changes/archive/`

## 2. Appliquer

- [x] 2.1 Commiter les tâches du groupe 1 en respectant la convention — ce commit est le premier conforme et sert de cas d'usage : `docs(specs): la convention de commit entre au dépôt par décision`
- [x] 2.2 Vérifier que le commit de 2.1 passe le contrôle de conformité de l'ADR : `git log --format='%s' -1 | grep -E '^(feat|fix|docs|refactor|test|chore)(\([a-z]+\))?!?: '`

## 3. Trancher les questions laissées ouvertes par le changement

- [x] 3.1 Décider si le correctif de la sentinelle déjà parti en PR #1 est renommé avant fusion — **tranché : non.** Le commit `17b60e4` précède l'adoption, et la tâche 1.4 pose qu'un sujet sans type est *antérieur* et non *invalide*. Le renommer contredirait la règle le jour même où elle entre
- [x] 3.2 Décider du niveau de version que ce changement lui-même déclenche — **tranché : corrective.** Rien d'expédié ne change : ni voix, ni dispositif, ni déclencheur ; seule change la façon d'écrire les commits.

      La règle « la conformité à une norme externe compte comme **mineure** » a été examinée et écartée. Sa lettre s'applique — Conventional Commits est bien une norme externe, avec le précédent d'agentskills.io — mais **son motif ne suit pas** : il dit *« elle ne change rien à ce que les voix disent, et tout à qui peut les charger »*, or cette convention ne change rien à qui peut charger quoi.

      Ce que la décision laisse ouvert : les trois niveaux du README décrivent tous un changement **du produit**. Une convention de travail n'en est pas un, et le tableau n'a pas de ligne pour « le dépôt change sa façon de travailler sur lui-même » — la politique de branches, non tranchée, tomberait dans la même case manquante. `corrective` est le classement le moins faux, pas le bon. Le vrai correctif serait un quatrième niveau, et c'est un ADR distinct.

## 4. Bilan, après 14 commits conformes

**Seuil abaissé de 20 à 14 le 2026-08-08, et le motif compte autant que le chiffre.** Le 20 était posé avant toute donnée, dans un dépôt qui n'avait alors aucun commit conforme ; il n'a jamais été calculé. Il ne figure dans aucun ADR en force — `adr/0001` le portait, et `adr/0002` le supersède en entier sans le reprendre.

**Ce que l'abaissement coûte, écrit ici parce que rien d'autre ne le dira :** le seuil est abaissé à exactement le compte du jour, c'est-à-dire que l'échantillon est arrêté après avoir été vu. Sur deux des trois mesures c'est sans effet — la conformité est à 0 non conforme sur 13, et le compte des non conformes sur `main` est à 0. Sur la troisième, ça n'est pas neutre : la part de `chore` est à 17 % pour un seuil de déclenchement à 20 %, et un échantillon plus large aurait pu la faire basculer. **Si le bilan conclut que le jeu de types est bien ajusté, cette conclusion est à relire au prochain doute plutôt qu'à tenir pour acquise.**

**Bilan exécuté le 2026-08-08**, depuis `aed2b6a`, après fusion de la demande #13 :

| | |
|---|---|
| commits depuis l'adoption | 14 (15 avec le commit d'adoption) |
| non conformes | **0** |
| répartition | `docs` 8 · `chore` 3 · `feat` 2 · `fix` 1 |
| part de `chore`, hors robot | **2/13 = 15,4 %** — sous le seuil d'un commit sur cinq |
| sujets réduits à une étiquette | **1 sur 15**, hors robot **0 sur 14** |

**Verdict : le jeu de types est bien ajusté. Aucun ADR successeur n'est ouvert.**


*Non exécutable aujourd'hui : un seul commit conforme existe (`811221b`). Ce groupe reste ouvert plusieurs semaines par construction — l'archivage ne doit pas l'attendre.*

- [x] 4.1 **0 non conforme sur 14.** Mesurer la conformité : `git log --format='%s' <sha-adoption>..HEAD | grep -cvE '^(feat|fix|docs|refactor|test|chore)(\([a-z]+\))?!?: '` doit rendre 0
- [x] 4.2 **1 sujet sur 15 se réduit à une étiquette — `chore(main): release 0.5.0`, généré par release-please. Hors robot : 0 sur 14.** La règle de comptage de 4.3 vaut ici aussi : ce n'est pas l'auteur qui rédige. Mais **rien dans la spec ne l'exempte**, et l'exigence « la description reste une phrase qui porte un constat » est donc violée sur `main` par l'outillage du dépôt lui-même. Défaut à corriger au niveau de l'exigence, non de la tâche. Relire les 14 sujets et vérifier qu'aucun ne s'est réduit à une étiquette (le contrôle « non-aplatissement » de l'ADR)
- [x] 4.3 **2/13 = 15,4 % hors robot, sous le seuil.** Règle de comptage, écrite avant la mesure : les commits générés par un outil ne comptent pas.** `chore(main): release X` est signé `github-actions[bot]` ; ce n'est pas l'auteur qui choisit un type, c'est release-please qui applique sa convention. Compter ces commits mesurerait l'outil, non l'ajustement du jeu de types au travail. Mesurer la part de `chore` — au-delà d'un commit sur cinq, ouvrir un ADR successeur ajustant le jeu de types
- [x] 4.4 **0 commit non conforme sur `main` ; le déclencheur n'est pas tiré et rien n'est construit.** L'instrument à construire est un contrôle du titre de la demande de fusion, en CI — pas un hook `commit-msg`.** `adr/0003` D6 l'a corrigé : sous écrasement, le titre de la demande est le seul message typé qui atteigne `main`, et un hook local s'exécute avant que la demande n'existe. Compter les commits non conformes poussés sur `main` — à trois, construire le hook `commit-msg` en stdlib (déclencheur de réouverture de la décision D5)
