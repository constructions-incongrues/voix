## Context

La proposition demande de porter le plafond de sept à dix. La spec en a fait deux plafonds distincts, sur l'argument de Debord : un plafond sur les inscrites rationne des intentions, un plafond sur les routables rationne ce qui parle.

**ADR en force :** `adr/0002`, `0003` et `0004`. `adr/0001` est superséd. Aucun ne parle du registre des voix ; `adr/0005` complétera sans superséder.

**Une correction, avant tout le reste.** La proposition invoque la dilution du routage comme argument central : 12 convocations sur 16 emportées par des fichiers hors du travail, `guy-debord` gagnant 8 fois. Relecture du journal en excluant `.nanopm/` :

| Voix | Convocations sur du travail réel |
|---|---|
| `lessig` | **7** |
| `illich` | 2 |
| `guy-debord` | **1** |

**Les huit victoires de Debord venaient toutes de `.nanopm/`**, dont l'exclusion a été décidée par `adr/0004` quelques heures plus tôt. La dilution mesurée avait une cause unique, et elle est déjà traitée. Ce qui reste — `lessig` à 7 sur 10 — n'est pas un effet de classement mais une collision de vocabulaire : ses termes (`429`, `verrouill`, `blocage`, `interdit de`, `rate limit`) rencontrent la prose technique partout.

Construire un correctif de classement maintenant reviendrait à réparer une panne dont on a déjà retiré la cause.

**Un défaut distinct persiste** et se voit dans le même relevé : trois convocations `lessig (429)` identiques, sur le même jeu de fichiers. Un silence ne laisse pas de marqueur, donc se rejoue. Nommé, non traité ici.

## Goals / Non-Goals

**Goals :**

- Porter le plafond d'inscription à dix sans toucher à ce que le motif d'origine protège.
- Rendre visible l'écart entre ce que le registre déclare et ce qui répond — quinze noms, trois voix.
- Faire porter au routage une condition d'admission que le test d'apport ne couvre pas : ce qu'une voix prend aux autres.
- Corriger un critère de 1.0 qui comptait un progrès contre un plafond.

**Non-Goals :**

- Admettre Glissant. Il est le motif de ce changement, pas son objet.
- Écrire Federici, Ostrom ou Polanyi. Le plafond ne les bloquait pas ; rien ne les bloquait.
- Modifier le classement des candidates dans le hook. Voir D2.
- Traiter le silence sans marqueur. Défaut réel, changement distinct.

## Decisions

### D1 — Deux plafonds, et un seul monte

Inscription à dix, routage à sept. Le second reprend le nombre **et** le motif d'origine sans changement, parce qu'aucune mesure n'a montré qu'il pouvait monter — et que la seule mesure disponible montre l'inverse, à trois voix.

*Alternative.* **Un plafond unique à dix** — rejeté : il lève la borne exactement là où le motif écrit disait qu'il ne fallait pas, et laisse sans borne la seule chose que ce motif protégeait.

### D2 — Le classement du hook n'est pas touché

`candidates.sort(reverse=True)` sur le nombre de termes touchés reste tel quel.

C'est la décision la plus contre-intuitive du dossier, et elle vient de la correction ci-dessus : la dilution invoquée avait pour cause `.nanopm/`, retiré par `adr/0004`. Sur du travail réel, la répartition est 7/2/1 — déséquilibrée, mais par le vocabulaire d'une voix, pas par un défaut d'arbitrage.

Trois correctifs ont été envisagés et écartés :

- **Normaliser le score** (`touches / len(termes)`) — écarté : les trois listes font 11, 12 et 14 termes. La longueur n'explique rien ici, et `lessig`, qui a la plus longue, gagnait *avant* le nettoyage moins souvent que `debord`.
- **Plafonner la surface de termes par voix** — écarté : borne une cause qui n'est pas établie, et rendrait la rédaction d'une voix dépendante d'un quota.
- **Départager par rareté du terme touché** — écarté pour l'instant : plausible, non mesuré, et coûteux à régler.

La réponse retenue est la mesure, pas le mécanisme : **toute admission au routage porte désormais l'effet de la voix sur la sélection**, exigence de la spec. Si sept voix routables produisent un déséquilibre mesuré, le correctif se choisira alors sur des chiffres plutôt que sur une crainte.

### D3 — Le registre distingue ce qu'il déclare de ce qui répond

Chaque inscrite porte son état : écrite ou non, routable ou non. Une inscription sans `SKILL.md` est signalée comme indisponible.

Le motif est le compte que Debord a laissé au dossier : **quinze noms, trois voix, 20 %**. L'écart n'est pas un secret — le dépôt refuse sa 1.0 pour cette raison — mais il est présenté comme un compte à rebours alors qu'il est un état. Le registre est la source de routage ; il doit dire ce qui route.

### D4 — Le critère de 1.0 cesse d'employer le plafond comme dénominateur

« Quatre voix sur sept » compte un progrès contre une borne, ce qui contredit directement « sept est un plafond, pas un objectif ». Un plafond qui sert de dénominateur *est* un objectif, quoi qu'on écrive à côté.

Le critère devient qualitatif et vérifiable : **aucune inscrite sans skill écrite, et le statut de routage de chacune tranché** — Albini compris, dont l'exclusion est aujourd'hui un état de fait mesuré et non une décision écrite.

C'est plus exigeant que l'ancien critère, et c'est voulu : à dix inscrites, « quatre sur dix » aurait fait reculer la 1.0 de trois crans sans qu'aucune ligne de code ne change.

*Alternative.* **Garder un ratio, sur les routables** — rejeté : même vice, autre dénominateur.

## Risks / Trade-offs

- **Deux plafonds valent deux fois plus d'occasions de se tromper de nombre.** → Ils bornent deux ensembles nommés différemment dans le registre, et D3 rend l'appartenance visible.
- **Ne pas toucher au classement peut se révéler faux à sept voix routables.** → Assumé, et daté : l'exigence de mesure à l'admission est le déclencheur. Le risque est de découvrir le problème une admission trop tard.
- **La correction de D2 repose sur un journal global à la machine**, qui mêle plusieurs dépôts — le même biais qu'`adr/0004` a dû corriger. → Les convocations retenues ici portent sur des chemins de plusieurs projets ; la répartition 7/2/1 vaut pour l'usage de l'auteur, non pour ce dépôt seul. Non mitigé.
- **Durcir le critère de 1.0 éloigne la 1.0.** → C'est le but. Un critère qui se satisfait en levant un plafond ne mesurait rien.
- **Rien n'oblige à employer les trois sièges gagnés.** → Un plafond n'est pas un objectif, et ce changement le réaffirme au moment même où il le lève. La contradiction est réelle et elle est le prix du cas Glissant.

## Migration Plan

1. **`openspec/specs/admission-voix/spec.md`** — l'exigence du plafond, par delta `REMOVED` + `ADDED`.
2. **`REGISTRE.md`** — la ligne du plafond ; l'état écrit/routable de chaque inscrite ; la règle du retrait explicite, désormais distincte selon l'ensemble concerné.
3. **`README.md`** — le compte en tête de fichier donne deux nombres ; le motif du plafond est réécrit ; les deux mentions du critère de 1.0 sont remplacées par le critère qualitatif.
4. **`adr/0005`** — la décision et son coût.
5. **Contrôle** — le registre et le README donnent le même couple de nombres, et il correspond à ce que `hooks/sentinelle.py` retourne comme voix routables.

**Rollback.** De la prose et une exigence de spec. Aucun code n'est touché — c'est la propriété la plus utile de ce changement.

## Open Questions

- **Albini.** Son exclusion du routage est un état constaté depuis `BASELINE.md`, jamais une décision écrite. D4 exige que le statut de chaque inscrite soit tranché ; celui d'Albini ne l'est pas. À trancher dans un changement distinct — le retirer, le maintenir inscrit non routable, ou rejouer son test d'apport sur un second artefact, son verdict « modeste » reposant sur un échantillon de un.
- **Le silence sans marqueur.** Trois convocations `lessig` identiques dans le relevé. Défaut nommé dans trois dossiers, traité dans aucun.
