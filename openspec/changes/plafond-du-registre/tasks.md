## 1. Porter les deux plafonds au registre

- [x] 1.1 Remplacer « Plafond : sept voix » par les deux plafonds — **dix inscrites, sept routables** — avec, pour chacun, ce qu'il protège
- [x] 1.2 Écrire la règle de retrait, désormais distincte selon l'ensemble : une onzième inscrite exige le retrait d'une inscrite, une huitième routable exige le retrait d'une routable, l'inscription restant possible sans routage
- [x] 1.3 Reprendre le motif du plafond de routage **mot pour mot** — il n'a pas changé, et le réécrire donnerait l'impression qu'il a été négocié

## 2. Dire ce qui répond

- [x] 2.1 Porter l'état de chaque inscrite au registre : **écrite / non écrite**, **routable / non routable**. Sept lignes, dont trois sans `SKILL.md` — Federici, Ostrom, Polanyi — et une écrite non routable, Albini
- [x] 2.2 Signaler explicitement les inscrites sans skill comme **non disponibles**, plutôt que de laisser leur ligne ressembler à celle d'une voix qui répond
- [x] 2.3 Vérifier que le compte du registre correspond à ce que `hooks/sentinelle.py` retourne comme voix routables — la source de routage doit dire vrai sur elle-même

## 3. Le README cesse d'annoncer un seul nombre

- [x] 3.1 Le compte en tête de fichier donne **deux nombres** — inscrites et routables — et non le premier seul
- [x] 3.2 Réécrire le motif du plafond : il porte sur le routage, et il est repris tel quel plutôt que reformulé
- [x] 3.3 Remplacer les **deux** mentions du critère de 1.0 « quatre voix sur sept » par le critère qualitatif : aucune inscrite sans skill écrite, et le statut de routage de chacune tranché
- [x] 3.4 Vérifier qu'aucune formulation du README ne présente plus un progrès rapporté à un plafond

## 4. Contrôles d'`adr/0005`

- [x] 4.1 **Contrôle affiné en le passant : il comparait des chiffres, le dépôt écrit ses nombres en toutes lettres.** Il compare désormais les deux formes. Résultat : `7 inscrites · 4 écrites · 3 routables`, conformes dans les deux fichiers et au hook. Deux nombres partout — `REGISTRE.md` et `README.md` donnent le même couple, conforme à ce que retourne le hook
- [x] 4.2 Aucun compte trompeur — aucun document public n'annonce comme disponible une inscrite sans `SKILL.md`
- [x] 4.3 **Code intact** — `git diff` sur `hooks/` est vide pour ce changement
- [x] 4.4 Critère de 1.0 vérifiable — il s'énonce sans dénominateur, et son évaluation ne dépend d'aucun plafond

## 5. Ce qui n'est pas fait, et pourquoi

- [x] 5.1 **Ne pas admettre Glissant.** Il est le motif de ce changement, pas son objet ; son admission passe par les trois conditions, la disjonction croisée et le test d'apport, dans un changement distinct
- [x] 5.2 **Ne pas écrire Federici, Ostrom ni Polanyi.** Le plafond ne les bloquait pas ; rien ne les bloquait
- [x] 5.3 **Ne pas toucher au classement du hook.** La dilution mesurée avait pour cause `.nanopm/`, retirée par `adr/0004`. Réparer maintenant serait corriger une panne dont la cause est partie
- [x] 5.4 **Ne pas trancher le statut d'Albini.** Son exclusion du routage est un état constaté, jamais une décision écrite, et son verdict « modeste » repose sur un échantillon de un. Question ouverte du design, changement distinct
- [x] 5.5 **Ne pas corriger le silence sans marqueur.** Trois convocations `lessig` identiques dans le relevé du jour. Défaut nommé dans quatre dossiers, traité dans aucun
