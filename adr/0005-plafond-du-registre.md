---
status: "accepted"
date: 2026-08-08
decision-makers: Tristan Rivoallan
consulted: —
informed: —
---

# Le registre gagne trois sièges et n'en gagne aucun au routage, parce que le plafond comptait des intentions

## Context and Problem Statement

Le registre plafonne à sept voix inscrites et il est plein. Une huitième candidate, Glissant, a passé le test de trace le 2026-08-08 avec une question qu'aucune inscrite ne pose — *qu'est-ce que ce système exige de rendre lisible, et qui a le droit de rester opaque ?* La règle en vigueur exige, pour l'admettre, le retrait explicite d'une inscrite.

Le `7` a été posé avant toute donnée. Mais contrairement au seuil de bilan levé le même jour, **il porte un motif écrit et mesurable** : *« Au-delà, le routage se dilue et le coût d'entretien dépasse ce qui est tenable. »*

Le compte, fait au moment d'écrire :

| | |
|---|---|
| noms au registre | **15** — 7 inscrites, 8 refusées |
| skills écrites | 4 |
| voix qui se convoquent seules | **3** |
| part du registre qui répond | **20 %** |

Quatre-vingts pour cent du registre est un catalogue. Le plafond rationnait donc, pour l'essentiel, des intentions — et le motif qu'il invoquait ne portait que sur la part qui parle.

**Le compte de la 1.0 aggravait la confusion.** Le README fait dépendre le passage à la 1.0 de « quatre voix sur sept ». Un plafond employé comme dénominateur *est* un objectif, quoi qu'on écrive à côté. Et à dix, « quatre sur dix » aurait fait reculer la 1.0 de trois crans sans qu'une ligne de code ne change.

**Une correction, faite en cours de rédaction et conservée.** La proposition de ce changement invoquait la dilution comme argument central : 12 convocations sur 16 emportées par des fichiers hors du travail, `guy-debord` gagnant 8 fois. Relecture du journal en excluant `.nanopm/` : `lessig` 7, `illich` 2, `guy-debord` **1**. **Les huit victoires de Debord venaient toutes de `.nanopm/`**, dont `adr/0004` a décidé l'exclusion quelques heures plus tôt. La dilution mesurée avait une cause unique, déjà traitée.

## Decision Drivers

- Ne pas lever une borne exactement là où son motif écrit disait de ne pas la lever.
- Ne pas construire un correctif pour une panne dont la cause a été retirée.
- Cesser de mesurer un progrès contre un plafond.
- Rendre visible l'écart entre ce que le registre déclare et ce qui répond.
- Ne toucher à aucun code.

## Considered Options

1. **Deux plafonds — dix inscrites, sept routables**
2. **Un plafond unique à dix**
3. **Statu quo à sept, et retrait d'Albini pour faire place**
4. **Supprimer le plafond**

## Decision Outcome

Chosen option: **« Deux plafonds — dix inscrites, sept routables »**, parce que c'est la seule qui donne les trois sièges demandés sans lever la borne que le motif d'origine protégeait, et parce qu'elle nomme enfin la distinction que le registre pratiquait sans l'écrire.

**D1 — Inscription à dix, routage à sept.** Le plafond de routage reprend le nombre et le motif d'origine sans changement. Aucune mesure n'a montré qu'il pouvait monter ; la seule disponible montre l'inverse, à trois voix.

**D2 — Le classement du hook n'est pas touché.** `candidates.sort(reverse=True)` sur le nombre de termes touchés reste tel quel. Trois correctifs ont été envisagés — normaliser le score, plafonner la surface de termes, départager par rareté — et tous écartés : les trois listes font 11, 12 et 14 termes, la longueur n'explique rien, et la cause réelle du déséquilibre a déjà été retirée. **La réponse retenue est une mesure, pas un mécanisme** : toute admission au routage porte désormais l'effet de la voix sur la sélection des convocations, exigence que le test d'apport ne couvrait pas.

**D3 — Le registre distingue ce qu'il déclare de ce qui répond.** Chaque inscrite porte son état — écrite ou non, routable ou non — et une inscription sans `SKILL.md` est signalée indisponible. Aucun compte public ne l'annonce comme une voix du dépôt.

**D4 — Le critère de 1.0 cesse d'employer le plafond comme dénominateur.** Il devient qualitatif : **aucune inscrite sans skill écrite, et le statut de routage de chacune tranché.** C'est plus exigeant que « quatre sur sept », et c'est voulu.

### Consequences

- Bon, parce que les trois sièges demandés sont donnés sans lever la borne qui protégeait le routage.
- Bon, parce que la distinction inscrite/routable était déjà pratiquée — Albini est inscrit et non routable depuis `BASELINE.md` — sans jamais avoir été écrite. Le registre dit maintenant ce qu'il fait.
- Bon, parce qu'aucune ligne de code n'est touchée. C'est de la prose et une exigence de spec.
- Bon, parce que le critère de 1.0 cesse de pouvoir être satisfait en déplaçant une borne.
- Neutre, parce que rien n'oblige à employer les trois sièges gagnés.
- **Mauvais, parce que ce changement réaffirme qu'un plafond n'est pas un objectif au moment précis où il le lève pour loger une candidate.** La contradiction est réelle, elle n'est pas mitigée, et elle est le prix du cas Glissant. Un lecteur qui n'aurait que cet ADR conclurait que le dépôt rationne ce qui l'arrange.
- Mauvais, parce que ne pas toucher au classement peut se révéler faux à sept voix routables. Le déclencheur est l'exigence de mesure à l'admission, ce qui expose à découvrir le problème une admission trop tard.
- Mauvais, parce que la correction qui fonde D2 repose sur un journal **global à la machine**, mêlant plusieurs dépôts — le biais exact qu'`adr/0004` a dû corriger la même journée. La répartition 7/2/1 vaut pour l'usage de l'auteur, non pour ce dépôt seul. Non mitigé.
- Mauvais, parce que durcir le critère de 1.0 éloigne la 1.0 alors que rien dans le dispositif ne s'est dégradé.

### Confirmation

- **Deux nombres partout** — `REGISTRE.md` et `README.md` donnent le couple inscrites/routables, et il correspond à ce que `hooks/sentinelle.py` retourne comme voix routables.
- **Aucun compte trompeur** — aucun document public n'annonce comme disponible une inscrite sans `SKILL.md`.
- **Code intact** — `git diff` sur `hooks/` est vide pour ce changement.
- **Critère de 1.0 vérifiable** — il s'énonce sans dénominateur, et son évaluation ne dépend d'aucun plafond.

## Pros and Cons of the Options

### Deux plafonds — dix inscrites, sept routables

- Bon, parce qu'il sépare deux bornes qui protégeaient deux choses et n'en avaient qu'une.
- Bon, parce qu'il écrit une pratique déjà en vigueur au lieu d'en inventer une.
- Neutre, parce qu'il ajoute un nombre à retenir.
- Mauvais, parce qu'il lève une borne pour un cas, et le dit sans pouvoir s'en défendre.

### Un plafond unique à dix

- Bon, parce qu'il est simple et qu'il donne ce qui était demandé.
- Mauvais, parce qu'il lève la borne exactement là où le motif écrit disait de ne pas la lever.
- Mauvais, parce qu'il laisse sans borne la seule chose que ce motif protégeait.

### Statu quo à sept, et retrait d'Albini

- Bon, parce que c'est la règle en vigueur appliquée telle quelle, sans rien changer.
- Bon, parce qu'Albini a une mesure contre lui et Glissant une table pour lui.
- Mauvais, parce que le verdict « modeste » d'Albini repose sur **un seul artefact** : un term sheet. Retirer une voix sur un échantillon de un serait moins rigoureux que le test qui l'a produit.
- Mauvais, parce qu'il traite comme une décision ce qui n'a jamais été instruit.

### Supprimer le plafond

- Bon, parce qu'il n'y aurait plus de nombre arbitraire à défendre.
- Mauvais, parce que la contrainte de rareté est ce qui a produit huit refus motivés, c'est-à-dire l'essentiel de la valeur du registre.
- Mauvais, parce que le coût d'entretien — un jeu d'evals par voix — est réel et croît linéairement.

## More Information

Mesures à l'appui, prises le 2026-08-08 : 7 inscrites, 8 refusées, 4 skills écrites, 3 voix routables. Sur les huit refus, **sept sont des doublons** — Gorz, Ellul, Mumford, Castoriadis, Lordon, Kropotkine, Graeber — qu'un plafond à dix n'admet pas davantage. Le huitième, Weil, a été refusé pour absence de trace, motif également indifférent au plafond. **Lever le plafond débloque exactement une candidate.**

Le compte du registre — quinze noms, trois voix, 20 % — a été produit par la voix `guy-debord`, convoquée par la sentinelle sur la proposition de ce changement. Il est conservé dans `proposal.md` avec sa table d'inversions.

L'admission de Glissant n'est **pas** décidée ici. Elle reste soumise aux trois conditions, au test de disjonction croisée et au test d'apport, dans un changement distinct.

Réexamen prévu : à la première admission au routage, dont l'exigence de mesure dira si le classement tient à sept voix.
