## Why

Le dépôt n'a jamais tranché sa politique de branches, et les deux ADR écrits le disent chacun à leur dernière ligne : *« ADR distinct à ouvrir »*. `REGISTRE.md` le dit une troisième fois, en motif de retrait d'une skill : *« Ce dépôt n'a jamais tranché sa politique de branches ; il a poussé quarante commits en direct sur `main`. »*

Ce qui a changé entre-temps, c'est que le vide a commencé à coûter. Mesures prises sur `HEAD` au 2026-08-08 :

- **45 commits, 0 commit de fusion.** L'historique est linéaire, mais par accident : personne n'a décidé qu'il le serait.
- **40 commits poussés en direct sur `main`, 5 arrivés par demande de fusion** (#1 à #3 ; #4 est ouverte).
- **La méthode de fusion diffère d'une demande à l'autre** — #1 est arrivée par écrasement (son sujet porte le suffixe `(#1)`), #2 et #3 par rebasage (aucun suffixe). Trois demandes, deux méthodes, aucune décision.
- **`main` n'est protégée par rien** : ni règle de protection, ni *ruleset* — vérifié par l'API GitHub, qui répond `Branch not protected` et une liste vide.
- **Les branches s'appellent `tritri/<slug>`** parce que l'outil de travail les nomme ainsi, et pour aucune autre raison. C'est exactement l'effet de bord que `REGISTRE.md` refuse : une façon de travailler héritée d'un outil au lieu d'être décidée.

Et depuis `adr/0002`, une machine a un avis sur la question. release-please suppose une branche par défaut, ouvre ses propres demandes, et se nomme sa propre branche — `release-please--branches--main--components--incongru-voix`. Toute règle de nommage ou de protection écrite sans elle sera fausse à la première publication.

Le déclencheur nommé par `adr/0002` — *« non bloquant tant que l'auteur est seul, bloquant à la première contribution externe »* — n'est pas encore tiré. On tranche avant, pendant que c'est gratuit.

## What Changes

- Le dépôt adopte une **politique de branches écrite**, qui entre par décision et non par outil, conformément à la règle que `REGISTRE.md` a déjà fait appliquer une fois.
- `main` est nommée **branche par défaut et seule branche de publication**. Rien d'autre n'est balisé.
- Le travail passe par des **branches de courte durée**, fusionnées puis supprimées. Le mode d'existence actuel — arbres de travail sous `.claude/worktrees/` — est constaté, pas prescrit.
- **Une seule méthode de fusion**, tranchée : **écrasement pour rejoindre `main`, rebasage pour mettre à jour une branche de travail**. L'historique linéaire constaté devient une propriété voulue. Conséquence chiffrée plus bas : sous écrasement, le titre de la demande devient le seul message typé que release-please lise jamais, et le garde-fou différé par `adr/0001` — un hook `commit-msg` — ne peut pas le voir.
- Une **règle de nommage des branches** qui accepte celles que le dépôt ne nomme pas : la branche de release-please est conforme par construction, pas par exception.
- Ce que devient le **poussé direct sur `main`** : autorisé, découragé, ou empêché par une protection. C'est la seule question de la politique qui ait un coût immédiat, et elle reste ouverte — le calcul en fin de document donne son seuil de bascule et le déclencheur qui l'arme.
- **Aucune réécriture de l'historique**, dans la continuité du garde-fou n°4 de `adr/0002`. Les 40 commits directs sont *antérieurs*, pas *invalides*.
- **Aucune dépendance ajoutée.** La politique est de la prose ; sa seule mise en œuvre possible est une configuration GitHub, qui n'installe rien chez l'usager.

## Capabilities

### New Capabilities

- `politique-de-branche` : quelles branches existent et pour combien de temps, comment elles se nomment, comment elles rejoignent `main`, ce qui a le droit d'y être poussé en direct, et ce que la politique doit garantir à l'outil de publication pour ne pas le bloquer.

### Modified Capabilities

Aucune. `publication-automatisee` décrit ce que release-please dérive et publie ; la politique de branches décrit le chemin par lequel un commit y parvient. Les deux se touchent — une protection de `main` s'applique aussi aux demandes de l'outil — mais cette contrainte est une exigence de la nouvelle capacité, pas la modification d'une exigence existante.

## Impact

- **`README.md`** — une section sur le chemin qu'un changement emprunte jusqu'à `main`, à côté de la section Versions.
- **`REGISTRE.md` ligne 100** — le motif de retrait d'`openspec-git-discipline` invoque une politique non tranchée. Il devra être relu une fois qu'elle le sera : la skill reste retirée, mais son motif change de nature.
- **Configuration GitHub** — méthodes de fusion autorisées sur le dépôt, et éventuellement une règle de protection sur `main`. Seul point de la politique qui ne soit pas de la prose.
- **`adr/0003`** — la décision, écrite au format des deux précédentes. Elle ne supersède ni `adr/0001` ni `adr/0002` : elle tranche ce qu'ils ont tous deux laissé ouvert.
- **Aucun code, aucune dépendance, aucun outil de vérification.** Le dépôt n'a aucune dépendance runtime et cette contrainte tient.

---

## Le calcul, avant de trancher

<!-- incongru-voix: illich — seuil 14 incidents (4,5 h de cérémonie pour 0 incident observé sur 40) — qui porte : l'auteur unique -->

Trois questions posées à cette politique, trois calculs. Le premier concerne la protection de `main`, le deuxième la méthode de fusion que vous venez de trancher, le troisième la règle de nommage. Les chiffres sont pris sur `HEAD` au 2026-08-08 ; les fourchettes sont assumées.

### 1. Protéger `main` : 4,5 h englouties, 0 h rendue

Ce que le dépôt est, mesuré : **9,81 h d'existence, 45 commits, 1 auteur, 4,6 commits/heure, 13,4 min entre deux commits.**

Ce qu'une demande de fusion a coûté, mesuré sur les trois seules qui existent — de l'ouverture à la fusion :

| Demande | Latence | Commits portés |
|---|---|---|
| #1 | 12 min 38 s | 1 |
| #2 | 3 min 21 s | 2 |
| #3 | 1 min 18 s | 2 |
| **Moyenne** | **5,8 min** | **1,7** |

À quoi s'ajoute le travail fantôme que ces horodatages ne comptent pas — créer la branche, pousser, rédiger le titre et le corps, revenir supprimer la branche : **4 min, fourchette assumée.** Soit **≈ 10 min par demande.**

Le calcul :

```
45 commits ÷ 1,7 commit par demande      ≈ 27 demandes
27 demandes × 10 min                      = 270 min = 4,5 h
4,5 h ÷ 9,81 h d'existence du dépôt       = 46 % du temps du dépôt
```

**Terme du dénominateur — le temps rendu : 0.** Sur les 40 commits poussés en direct, l'historique compte **0 revert et 0 commit d'annulation**. Le relecteur est l'auteur ; il relit le même diff qu'avant `git push`, avec les mêmes yeux, à trois minutes d'intervalle. Le ratio n'est donc pas calculable — je donne le point de bascule à la place :

```
270 min ÷ 20 min de réparation par incident évité = 14 incidents
14 incidents sur 45 commits                        = 31 % de taux de défaut
```

**La protection devient rentable à partir de 14 incidents rattrapés, soit un commit sur trois défectueux. Observé : 0 sur 40.**

Ce n'est pas un argument contre la protection : c'est la position du seuil. Le dénominateur cesse d'être nul le jour où **le relecteur n'est plus l'auteur** — c'est-à-dire au second contributeur, exactement le déclencheur que `adr/0002` avait déjà nommé sans le chiffrer. Écrire la règle maintenant coûte une phrase ; l'armer maintenant coûte 46 % du temps du dépôt.

Verdict de convivialité sur la protection elle-même — *comprendre ?* oui, une case dans les réglages. *Réparer ?* oui, on la décoche. *S'en passer ?* oui, 40 commits l'attestent. **Trois oui : l'outil est convivial.** Il n'est pas dangereux, il est prématuré. Rien n'oblige à choisir entre l'adopter et le refuser — il suffit de nommer la date.

### 2. L'écrasement déplace le point de panne hors de portée du garde-fou prévu

Vous avez tranché : écrasement sur `main`, rebasage pour mettre à jour. Voici ce que ça coûte, mesuré, pas supposé.

| Demande | Commits | Types portés | Ce que l'écrasement en aurait fait |
|---|---|---|---|
| #1 | 1 | *aucun* (sujet antérieur à la convention) | 1 sujet **non typé** sur `main` |
| #2 | 2 | `docs(specs)` × 2 | 1 commit, même niveau, 1 ligne de journal perdue |
| #3 | 2 | `chore(plugin)` × 2 | 1 commit, même niveau, 1 ligne de journal perdue |

**Fausses versions produites : 0 sur 3.** Dans les deux demandes à plusieurs commits, les deux commits portaient le même type — le niveau de version aurait été identique. Le coût observé de l'écrasement est de la granularité de journal : **2 lignes perdues sur 5.** C'est peu, et c'est le prix normal de la méthode.

Le coût réel est ailleurs, et il est structurel : **sous écrasement, le titre de la demande devient le seul message typé que release-please lise jamais.** L'autorité sur le numéro de version, que `adr/0002` a placée dans les types de commit, se déplace du message de commit vers le titre de la demande.

Or, mesuré : **1 titre de demande sur 3 n'était pas conforme** — celui de #1, sans aucun préfixe de type. Et le garde-fou que `adr/0001` a différé pour ce risque exact, un hook `commit-msg` d'une vingtaine de lignes, **ne voit jamais un titre de demande.** Il s'exécute sur la machine de l'auteur, avant que la demande n'existe.

C'est de l'iatrogenèse au sens strict : la méthode de fusion déplace le point de panne précisément là où le remède prévu ne peut pas l'atteindre. Ce qui change une décision, et une seule : **le déclencheur écrit dans `adr/0001` — « trois commits non conformes sur `main` » → construire un hook `commit-msg` — désigne désormais le mauvais instrument.** Sous écrasement, ce doit être un contrôle du titre de la demande, en CI, à côté de release-please. Le déclencheur reste bon ; la réponse qu'il déclenche est à corriger dans l'ADR.

### 3. La règle de nommage : ne pas la faire écrire par l'outil

release-please se nomme sa branche : `release-please--branches--main--components--incongru-voix`.

Verdict de convivialité sur release-please — *comprendre ?* oui, deux fichiers de configuration et une table. *Réparer ?* **non**, c'est du code tiers exécuté sur le dépôt ; on peut le fixer à une version ou le retirer, pas le corriger. *S'en passer ?* oui, 40 commits ont été publiés sans lui et `plugin.json` s'édite à la main. **Deux oui, un non : l'outil sert encore.** Le « non » est celui à surveiller, et il n'a rien à voir avec le nommage.

Le risque de nommage est le monopole radical, et il coûte une ligne à éviter. Une règle taillée pour accueillir ce nom-là est une règle que l'outil a écrite : six semaines plus tard, plus personne ne sait pourquoi la forme est celle-là. La formulation qui tient : **la règle nomme les branches que le dépôt nomme ; celles qu'un outil se nomme sont exemptées nommément, et l'exemption est citée comme exemption.** Coût : une ligne de plus. Coût de l'autre voie : la forme du dépôt devient celle de l'outil, sans trace de la décision.

### Ce que le calcul laisse à trancher

Un seul point, et il est daté plutôt qu'ouvert : **écrire la règle de protection de `main` maintenant, l'armer au second contributeur.** Les chiffres sont au-dessus ; la division est faite ; la décision reste entière.
