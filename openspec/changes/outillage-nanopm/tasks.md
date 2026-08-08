## 1. Soustraire `.nanopm/` au dépôt

Une ligne, sous la catégorie que le `.gitignore` tient déjà — *outillage régénérable, non couvert par la licence du dépôt*. Aucun mécanisme n'est ajouté : `git ls-files --others --exclude-standard` applique `.gitignore`, donc ignorer suffit à soustraire au routage.

- [x] 1.1 Ajouter `.nanopm/` au `.gitignore`, dans le bloc existant, avec sa ligne de motif à côté de celles de `.claude/` et `.serena/`
- [x] 1.2 Contrôler que `git ls-files --others --exclude-standard` ne retourne plus aucun chemin sous `.nanopm/`
- [x] 1.3 Vérifier qu'**aucune ligne n'a été ajoutée au hook** pour obtenir ce résultat — c'est le critère qui distingue cette solution de celle qui a été écartée

## 2. Retirer le code mort du hook

`travail_en_cours()` saute `nom.startswith(".serena/")` après un `git ls-files --others --exclude-standard` qui applique déjà `.gitignore`, où `.serena/` figure. La ligne ne filtre rien depuis que cette entrée existe.

- [x] 2.1 Supprimer le saut `.serena/` en dur de `hooks/sentinelle.py`
- [x] 2.2 Contrôler par sonde qu'un fichier déposé dans `.serena/` reste absent de la sortie de `git ls-files --others --exclude-standard` après suppression
- [x] 2.3 Contrôler qu'un fichier neuf **écrit par l'auteur** et non ignoré reste bien examiné — l'exclusion vise l'état des outils, pas les fichiers neufs, et c'est le scénario que la spec protège

## 3. Consigner le refus

Un refus non inscrit est un refus qu'on reprendra par la même porte. Le tableau porte le nom, le statut, **ce que l'outil prescrivait**, et ce qui rouvrirait la question.

- [x] 3.1 Ajouter la ligne `nanopm` au tableau d'outillage de `REGISTRE.md` : non admis, avec ce qu'il prescrit — trois couches, sections calquées sur des phases, types de page, arêtes typées, journal append-only — et non pas seulement qu'il a été écarté
- [x] 3.2 Y inscrire le déclencheur de réouverture d'`adr/0004` : la chaîne Define exécutée pour de bon, produisant des pages lues au moins une fois dans un travail réel
- [x] 3.3 Reformuler la règle d'outillage de `REGISTRE.md` pour qu'elle renvoie à la capacité `admission-outillage` et cesse de nommer `.agents/skills/` — c'est ce périmètre qui a laissé passer le cas

## 4. Contrôles d'`adr/0004`

- [x] 4.1 Non-admission effective — aucun chemin `.nanopm/` dans `git ls-files --others --exclude-standard`
- [x] 4.2 Aucune liste d'exclusion dans le code — `hooks/sentinelle.py` ne contient plus de saut de chemin en dur
- [x] 4.3 Refus consigné — le tableau porte `nanopm`, son statut, sa prescription et son déclencheur de réouverture
- [x] 4.4 Routage rendu au travail — sur le journal postérieur, aucune convocation déclenchée par un fichier `.nanopm/` **de ce dépôt**. Ce contrôle ne couvre pas les autres projets et ne le prétend pas

## 5. Ce qui n'est pas fait, et pourquoi

Décisions de ne pas agir, consignées pour qu'on ne les prenne pas plus tard pour des oublis.

- [x] 5.1 **Ne pas désinstaller la skill `nanopm`.** Le dépôt décide de ce qu'il versionne, pas de ce que l'auteur exécute. Le refus porte sur l'appartenance des artefacts
- [x] 5.2 **Ne pas supprimer le répertoire du disque.** La skill le recrée à la prochaine invocation ; supprimer donnerait l'illusion d'un règlement
- [x] 5.3 **Ne pas traiter les autres dépôts.** Onze des douze convocations mesurées viennent d'ailleurs. Ce changement est un précédent, pas un remède, et `adr/0004` l'écrit comme conséquence mauvaise
- [x] 5.4 **Ne pas corriger le silence sans marqueur.** Un « non porteuse » ne laisse pas de trace et se rejoue au tour suivant — d'où six convocations quasi identiques de `guy-debord`. Défaut réel, nommé dans `adr/0004`, relevant d'un changement distinct
- [x] 5.5 **Ne pas déplacer la liste d'exclusion dans `REGISTRE.md`.** Envisagé puis écarté : elle dupliquerait `.gitignore` en s'en écartant au premier oubli, et demanderait du code de lecture pour refaire ce que git fait déjà
