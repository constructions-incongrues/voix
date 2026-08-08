## 1. Régler la forge

Quatre champs, une requête. Ces valeurs vivent hors du dépôt et n'y laissent aucune trace : leur motif est écrit dans `adr/0003` D1–D3, et la tâche 4.2 les reprend au README.

- [ ] 1.1 Passer `allow_merge_commit` et `allow_rebase_merge` à `false`, `allow_squash_merge` restant à `true` — une seule méthode offerte, donc une seule employée
- [ ] 1.2 Passer `delete_branch_on_merge` à `true` — la suppression cesse d'être un geste dont il faut se souvenir
- [ ] 1.3 Passer `squash_merge_commit_title` à `PR_TITLE` — le sujet atteignant `main` cesse de dépendre du nombre de commits de la branche
- [ ] 1.4 Vérifier que `squash_merge_commit_message` vaut toujours `COMMIT_MESSAGES` — le corps conserve les messages écrasés, et un pied de page `BREAKING CHANGE:` intermédiaire y survit
- [ ] 1.5 Contrôler le résultat : `gh api repos/:owner/:repo` rend les cinq valeurs attendues

## 2. Nettoyer les branches orphelines

Trois branches portées par des demandes déjà fusionnées subsistent sur le distant, `delete_branch_on_merge` ayant été à `false`. La tâche 1.2 empêche les suivantes ; celle-ci solde les existantes.

- [ ] 2.1 Supprimer `origin/tritri/nanopm-product-934146` (demande #1, fusionnée)
- [ ] 2.2 Supprimer `origin/tritri/conventional-commits` (demande #2, fusionnée)
- [ ] 2.3 Supprimer `origin/tritri/release-please` (demande #3, fusionnée)
- [ ] 2.4 Contrôler qu'aucune orpheline ne subsiste, en croisant les demandes fusionnées et les branches distantes — **et non par `git branch -r --merged`**, qui sous écrasement ne retourne jamais rien puisque la branche fusionnée n'est jamais un ancêtre de `main`

## 3. Sentinelle de contributeurs

Rend mécanique le déclencheur d'`adr/0003` D4 : sans elle, « on armera la protection au second contributeur » est une règle qui tient par la mémoire, et qui sera oubliée le jour précis où elle compte.

- [x] 3.1 Ajouter au workflow `release-please.yml` une étape comptant les auteurs de `main` **hors robots** — les noms se terminant par `[bot]` sont exclus, sans quoi la sentinelle se déclenche à la première publication et à contre-emploi
- [x] 3.2 Faire échouer l'étape quand le compte dépasse 1 et qu'aucune protection n'est active sur `main`
- [x] 3.3 Rédiger le message d'échec de sorte qu'il nomme la règle, cite `adr/0003` D4, et indique qui peut armer la protection — exigence de la spec, à satisfaire dès la première version et non par un ajustement ultérieur
- [x] 3.4 Laisser le déclencheur sur `on: push: branches: [main]` — déplacé sur `pull_request`, il sanctionnerait un contributeur qui n'a aucun moyen d'obéir
- [x] 3.5 Vérifier l'étape sur un compte simulé à deux auteurs sans protection : elle échoue, et son message est lisible par quelqu'un qui découvre le dépôt

## 4. Écrire la politique au README

- [x] 4.1 Ajouter une section sur le chemin qu'un changement emprunte jusqu'à `main` : branche courte, écrasement pour rejoindre, rebasage pour mettre à jour, suppression après fusion
- [x] 4.2 Y consigner les cinq réglages de forge avec leur motif — la forge n'en conserve aucun, et c'est un troisième point de dérive silencieuse après la table de correspondance et `REGISTRE.md`
- [x] 4.3 Écrire la règle de nommage `<contributeur>/<slug>`, et l'exemption des branches qu'un outil se nomme — release-please cité nommément, la règle générale non élargie
- [x] 4.4 Écrire que le titre de la demande est le message qui fait autorité, et qu'il porte le type le plus élevé quand la branche mélange les types
- [x] 4.5 Écrire l'asymétrie de dérogation à la protection de `main` avec son motif : elle est légitime, et non écrite elle se lit comme un oubli

## 5. Mettre à jour `REGISTRE.md`

- [x] 5.1 Reprendre la ligne 100 : le motif de retrait d'`openspec-git-discipline` invoque une politique non tranchée. Elle l'est. La skill reste retirée, pour un motif qui devient « ce dépôt a tranché autrement », et la ligne doit le dire en citant `adr/0003`

## 6. Contrôles de l'ADR

Les critères de confirmation d'`adr/0003`, rejoués une fois l'ensemble posé.

- [ ] 6.1 Méthode unique — les cinq champs de forge ont les valeurs attendues
- [ ] 6.2 Linéarité — `git log --merges --oneline` sur `main` ne retourne aucune ligne
- [ ] 6.3 Aucune branche orpheline — le croisement demandes fusionnées / branches distantes est vide
- [ ] 6.4 Sentinelle armée — sur un dépôt simulé à deux contributeurs hors robots et sans protection, le workflow échoue
- [ ] 6.5 Titres conformes — relire les titres des demandes fusionnées depuis l'adoption, et compter les non conformes

## 7. Ce qui n'est pas fait, et pourquoi

Ces lignes ne sont pas des tâches en attente : ce sont des décisions de ne pas agir, consignées pour qu'on ne les prenne pas pour des oublis.

- [x] 7.1 **Ne pas construire le contrôle de titre en CI.** D5 est en force et son déclencheur — trois messages non conformes sur `main` — n'est pas tiré. `adr/0003` en corrige l'instrument sans avancer la date
- [x] 7.2 **Ne pas protéger `main`.** Le calcul la chiffre à ≈ 46 % du temps du dépôt pour un temps rendu nul. La sentinelle de la section 3 est ce qui remplace la mémoire
- [x] 7.3 **Ne pas réécrire l'historique.** Les 40 commits directs sont antérieurs, pas invalides
- [x] 7.4 **Ne pas contrôler la table des réglages de forge.** Question ouverte du design, prématurée tant que la seule personne pouvant les modifier est celle qui les a posées
