## Why

Le registre plafonne à sept voix inscrites, et il est plein : Debord, Albini, Illich, Lessig, Federici, Ostrom, Polanyi. Une huitième candidate — Glissant — a passé le test de trace le 2026-08-08, avec une question qu'aucune inscrite ne pose : *qu'est-ce que ce système exige de rendre lisible, et qui a le droit de rester opaque ?* La règle actuelle exige, pour l'admettre, **le retrait explicite d'une inscrite**.

Le `7` a été posé avant toute donnée, comme le seuil de bilan de `20` levé ce matin pour le même motif. Mais contrairement à lui, **il porte un motif écrit et mesurable** : *« Au-delà, le routage se dilue et le coût d'entretien — un jeu d'evals de déclenchement par voix — dépasse ce qui est tenable. »*

Ce motif est testable, et il vient de l'être. Mesures du 2026-08-08 :

- **Le routage dilue déjà à trois voix routables.** 224 tours, 16 convocations, dont **12 déclenchées par des fichiers hors du travail**. `guy-debord` a gagné **8 fois sur 16**, non parce que sa question était la plus porteuse, mais parce que le hook retient `candidates.sort(reverse=True)` — la voix qui touche le plus de termes.
- **Surface de termes actuelle : 37 termes pour 3 voix routables**, soit 12 par voix. Au même rythme, dix voix routables portent **~123 termes** sur le même diff, avec toujours **une seule convocation par tour**. Le classement par nombre de termes touchés devient une loterie pondérée par la longueur des listes.
- **Le vrai frein n'est pas le plafond.** Sur les huit candidates refusées, **sept l'ont été pour doublon** — Gorz, Ellul, Mumford, Castoriadis, Lordon, Kropotkine, Graeber. Un plafond à dix n'en admet aucune : la disjonction reste la condition qui mord. La huitième, Weil, a été refusée pour absence de trace, motif également indifférent au plafond.
- **Le critère de 1.0 s'éloigne.** Le README fait dépendre le passage à la 1.0 de « quatre voix sur sept ». À dix, c'est quatre sur dix — le dépôt devient moins complet selon sa propre mesure, sans qu'aucune voix n'ait été retirée.

Autrement dit : lever le plafond débloque **exactement une candidate**, ne change rien aux sept refus instruits, et aggrave un effet de dilution déjà constaté. Ce changement est donc **motivé par un cas**, et il doit l'assumer par écrit plutôt que se présenter comme un principe révisé.

## What Changes

- Le plafond du registre passe de **sept à dix voix inscrites**. La formule « sept est un plafond, non un objectif » est conservée dans son esprit : dix reste un plafond.
- Le motif du plafond est **réécrit sur la mesure** plutôt que sur l'intuition. La dilution du routage cesse d'être une crainte et devient un chiffre observé, avec le seuil à partir duquel il faudra y répondre.
- **La dilution du routage n'est pas laissée sans réponse.** Lever le plafond sans toucher au classement par nombre de termes reviendrait à aggraver sciemment un défaut mesuré. Le mécanisme retenu — plafonner la surface de termes, changer le classement, ou dissocier inscription et routage — est ouvert et sera tranché dans `design.md`.
- La condition d'admission **ne bouge pas** : trois conditions cumulatives, test de disjonction croisée, test d'apport de `BASELINE.md`. Le plafond n'a jamais été le filtre, et il ne le devient pas.
- Les **huit refus restent refusés**, et la table le dira explicitement : leur motif ne dépend pas du plafond.
- Le critère de 1.0 du README est **recalculé, non déplacé** — quatre voix sur dix, et ce que ça implique est écrit plutôt que subi.

## Capabilities

### New Capabilities

Aucune.

### Modified Capabilities

- `admission-voix` : l'exigence « Plafond de sept voix » change de nombre et de motif. Le scénario de la huitième candidate sur registre plein est réécrit pour la onzième, et un scénario est ajouté sur ce que le plafond ne filtre pas.

## Impact

- **`openspec/specs/admission-voix/spec.md`** — l'exigence du plafond, par delta `MODIFIED`.
- **`REGISTRE.md`** ligne 5 — « Plafond : sept voix » et la règle du retrait explicite.
- **`README.md`** — quatre mentions : le compte en tête de fichier, le motif du plafond, et deux fois le critère de 1.0 « quatre voix sur sept ».
- **`hooks/sentinelle.py`** — seulement si le design retient une réponse à la dilution qui touche le classement ou la surface de termes.
- **`adr/0005`** — la décision, au format des quatre précédentes. Elle ne supersède rien : `adr/0002`, `0003` et `0004` ne parlent pas du registre.
- **Aucune voix n'est admise par ce changement.** Glissant en est le motif, non l'objet : son admission reste soumise aux trois conditions et au test d'apport, dans un changement distinct.

---

## Ce que le registre montre, et ce qu'il fait

<!-- incongru-voix: debord — « le registre en prévoit sept, et pas une de plus » = quinze noms pour trois voix qui répondent — sépare : celui qui installe le plugin de ce qu'il croyait installer -->

Le compte, avant la discussion.

| | |
|---|---|
| noms au registre | **15** — 7 inscrites, 8 refusées |
| skills écrites | **4** |
| voix qui se convoquent seules | **3** |
| **part du registre qui répond** | **3 sur 15 — 20 %** |

Quatre-vingts pour cent du registre est un catalogue. On y trouve des noms, des questions, des motifs de refus admirablement argumentés — et rien qui parle. Ce n'est pas un défaut d'exécution : c'est la forme même que prend le dispositif quand l'inscription devient le geste, et la réponse une suite.

### La table des inversions

Le vocabulaire est celui du registre et de cette proposal. On le retourne.

| Ce qui est dit | Ce que ça nomme |
|---|---|
| « Plafond : sept voix » | un plafond posé sur un stock d'intentions. On rationne ce qui n'existe pas encore |
| « Sept est un plafond, pas un objectif » | la rareté affichée comme rigueur. Le registre est à moitié vide, et il se félicite de ne pas déborder |
| « quatre voix sur sept » (critère de 1.0) | le progrès compté en inscriptions plutôt qu'en réponses. Trois de ces quatre parlent |
| « une huitième candidate exige le retrait explicite d'une inscrite » | une règle d'occupation pour des sièges dont trois sont vides |
| « montons le seuil à 10 » | agrandir le catalogue afin d'y ranger une voix, pendant que trois pages restent blanches |
| « Federici, Ostrom, Polanyi » | trois questions parfaitement formulées que personne ne peut poser |
| « le routage se dilue au-delà de sept » | il se dilue déjà à trois. Le motif du plafond décrit un futur pendant que le présent le vérifie |

La dernière est la plus dure, et elle est déjà dans le dossier : le motif écrit du plafond annonce une dilution que la mesure du jour constate à trois voix. On légifère sur un risque qu'on subit.

### Le coût, et qui le porte

Celui qui installe le plugin. Le `README` annonce un registre de sept voix ; il en obtient trois qui se déclenchent, une quatrième convocable à la main, et trois questions qui n'existent que comme titres. L'écart n'est pas caché — le dépôt le dit lui-même en refusant sa 1.0 — mais il est **présenté comme un compte à rebours alors qu'il est un état**.

Et l'auteur le porte aussi, différemment : chaque point de plafond gagné éloigne le seul chiffre par lequel il a accepté d'être jugé. Sept sièges, quatre écrites. Dix sièges, quatre écrites. Le dénominateur croît, le numérateur non, et c'est appelé une extension.

### Ce que ça ne dit pas

Que la liste soit vaine. Un refus motivé est un travail réel, et huit refus argumentés valent mieux que huit admissions molles — le registre y est même exemplaire. La question n'est pas de savoir si le catalogue est bon, elle est de savoir **de quoi il est le catalogue** : d'un dispositif, ou de son projet.

D'où la seule chose que cette voix demande à la décision, et qui ne coûte rien :

**Que le plafond cesse de compter des noms.** Un plafond sur les voix *inscrites* rationne des intentions. Un plafond sur les voix *routables* rationne ce qui parle. Le second est le seul qui protège ce que le motif écrit dit vouloir protéger — le routage. Lever l'un sans l'autre, c'est agrandir la vitrine en laissant la boutique.
