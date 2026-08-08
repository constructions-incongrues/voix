## 1. Socle

- [x] 1.1 `git init` et premier commit — rien ne bouge dans `~/.claude/skills/` avant que le dépôt sache revenir en arrière
- [x] 1.2 Créer `voix/` et `REGISTRE.md` avec les sept voix, leurs questions, leur état, et les refus motivés déjà instruits (Gorz, Ellul, Castoriadis, Mumford, Weil, Graeber, Lordon, Kropotkine)
- [x] 1.3 Écrire `install.sh` : une boucle de liens symboliques `voix/<nom>` → `~/.claude/skills/<nom>`, réexécutable sans dommage

## 2. Rétrofit des deux voix existantes

- [x] 2.1 Copier `guy-debord` et `steve-albini` depuis `~/.claude/skills/` vers `voix/`, sans modification, et commiter cet état de référence
- [x] 2.2 Ajouter les quatre sections à `voix/guy-debord/SKILL.md` en extrayant sa table d'inversion (`SKILL.md:47-66`) vers `## Compétence` et `## Signaux` ; formuler `## Question` et `## Trace`
- [x] 2.3 Idem pour `voix/steve-albini/SKILL.md` depuis sa table (`SKILL.md:49-64`)
- [ ] 2.4 Vérifier que les deux voix se chargent et se comportent comme avant le rétrofit, puis seulement remplacer les originaux par les liens

## 3. Lot 1 — Illich

- [ ] 3.1 Écrire `voix/illich/SKILL.md` : question (seuil de contre-productivité et convivialité), compétence (le calcul de vitesse généralisée, appliqué à un outil qui promet du gain de temps), trace (un nombre + un oui/non sur la réparabilité par l'usager)
- [ ] 3.2 Rédiger sa section biographique — dont la récupération de la déscolarisation par la droite libertarienne, nommée et non défendue
- [ ] 3.3 Écrire ses evals de déclenchement sur le modèle de `guy-debord-workspace/optimizer/`

## 4. Lot 1 — Lessig

- [ ] 4.1 Écrire `voix/lessig/SKILL.md` sur le seul axe *code is law* : les quatre modalités (loi, norme, prix, architecture) et la question du recours. Couper explicitement *free culture* (doublon Ostrom) et *dependence corruption* (doublon Albini)
- [ ] 4.2 Déclarer sa position réformiste dans le fichier, avec la mention qu'elle est peut-être ce qui permet au cadre de durer
- [ ] 4.3 Rédiger sa section biographique : défense publique en 2019 des dons anonymes d'Epstein au MIT Media Lab, plainte en diffamation contre le *New York Times* retirée — nommées, non défendues
- [ ] 4.4 Appliquer la contrainte « personne vivante » : raisonnement depuis l'œuvre publiée uniquement
- [ ] 4.5 Écrire ses evals de déclenchement

## 5. Trace

- [ ] 5.1 Ajouter à chaque voix sa règle de marqueur `skillotheque: <voix> — <coût> — <porteur>`, dans la syntaxe de commentaire de l'hôte
- [ ] 5.2 Vérifier `grep -rn "skillotheque:"` sur un projet d'essai : l'inventaire sort complet, sans outil

## 6. Validation — point d'arrêt du changement

- [ ] 6.1 Test de disjonction croisée : soumettre un même artefact aux quatre voix (Debord, Albini, Illich, Lessig) et vérifier que les quatre traces sont distinctes
- [ ] 6.2 Test de silence : sur un corpus d'une vingtaine de tâches ordinaires (une déclaration de TVA, un segfault, un renommage), vérifier que le taux de déclenchement reste sous une tâche sur cinq
- [ ] 6.3 Si 6.1 ou 6.2 échoue, resserrer les questions ou retirer une voix — le lot 2 (Federici, Ostrom, Polanyi) reste bloqué tant que les deux tests ne passent pas
- [ ] 6.4 Trancher la question ouverte du design : Federici en personne ou *Wages for Housework* en courant
