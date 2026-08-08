---
status: "accepted"
date: 2026-08-08
decision-makers: Tristan Rivoallan
consulted: —
informed: —
---

# Le travail rejoint `main` par écrasement, et la protection est armée par une sentinelle plutôt que par la mémoire

## Context and Problem Statement

`adr/0001` et `adr/0002` se terminent tous deux sur la même phrase : *« La politique de branches reste non tranchée. […] ADR distinct à ouvrir. »* `REGISTRE.md` le dit une troisième fois, en motif de retrait d'`openspec-git-discipline` : *« Ce dépôt n'a jamais tranché sa politique de branches ; il a poussé quarante commits en direct sur `main`. »* Trois documents renvoient à un quatrième qui n'existe pas. C'est celui-ci.

Ce qui a changé, c'est que le vide a commencé à coûter. Mesures prises sur `HEAD` au 2026-08-08 : 45 commits, **0 commit de fusion**, 40 poussés en direct sur `main`, 5 arrivés par demande. Trois demandes de fusion existent et **deux méthodes différentes** les ont fusionnées — #1 par écrasement, #2 et #3 par rebasage. L'historique est linéaire par accident : personne n'a décidé qu'il le serait.

L'état de la forge, relevé par l'API, explique le désordre mieux que la négligence : **les trois méthodes de fusion sont offertes**, `delete_branch_on_merge` est à `false` — d'où **trois branches sur trois demandes fusionnées encore présentes** sur le distant — et `squash_merge_commit_title` vaut `COMMIT_OR_PR_TITLE`, ce qui fait dépendre le message atteignant `main` du nombre de commits de la branche. Aucun de ces réglages n'a été choisi ; tous produisent de la méthode.

Depuis `adr/0002`, une machine a un avis sur la question. release-please suppose une branche par défaut, ouvre ses propres demandes, et **se nomme sa propre branche**. Toute règle écrite sans elle sera fausse à la première publication.

## Decision Drivers

- Faire entrer la politique par décision et non par outil, conformément à la règle que `REGISTRE.md` a déjà fait appliquer une fois.
- Ne pas payer une cérémonie qui ne rend rien tant que le relecteur est l'auteur.
- Ne retenir aucune règle qui ne tienne que par la mémoire — c'est le motif exact par lequel `adr/0002` a écarté son option 2.
- Ne pas laisser un outil dicter la forme du dépôt sans que la trace de cette concession subsiste.
- N'ajouter aucune dépendance runtime.

## Considered Options

1. **Politique écrite, forge réglée, protection différée et armée par une sentinelle mécanique**
2. **Protection de `main` armée immédiatement** — tout changement passe par une demande, dès aujourd'hui
3. **Politique écrite en prose seule** — aucun réglage de forge, aucune sentinelle, la discipline suffit
4. **Refus argumenté** — consigner que le dépôt reste sans politique, à la manière des 8 refus du registre

## Decision Outcome

Chosen option: **« Politique écrite, forge réglée, protection différée et armée par une sentinelle mécanique »**, parce que c'est la seule qui distingue ce qui coûte aujourd'hui de ce qui rendra demain — et qui, pour la partie différée, refuse de s'en remettre à la mémoire de l'auteur.

La décision porte cinq points.

**D1 — `main` est la seule branche de publication, et les branches de travail sont courtes.** Rien d'autre n'est balisé. Une branche fusionnée est supprimée, et la forge s'en charge : `delete_branch_on_merge` passe à `true`. La règle en prose était déjà violée à 100 % au moment de l'écrire — trois branches orphelines sur trois demandes — ce qui est le meilleur argument possible contre sa version prose.

**D2 — Rejoindre `main` se fait par écrasement ; mettre à jour une branche se fait par rebasage.** La forge n'offre plus qu'une méthode : `allow_merge_commit` et `allow_rebase_merge` passent à `false`. Une politique qui laisse trois boutons en place se fait démentir par le premier geste distrait. Désactiver `allow_rebase_merge` n'interdit pas le rebasage : ce réglage ne gouverne que le bouton de la forge, et `git rebase main` reste la méthode prescrite en local.

**D3 — Le titre de la demande devient le message qui fait autorité**, et `squash_merge_commit_title` passe à `PR_TITLE`. Le réglage actuel fait dépendre la source du sujet du nombre de commits de la branche : le message atteignant `main` change d'origine selon un critère que personne n'a choisi. Le titre doit donc satisfaire la capacité `convention-commits` en entier, et porter le type le plus élevé quand la branche mélange les types. `squash_merge_commit_message` reste à `COMMIT_MESSAGES` : le corps conserve les messages écrasés, ce qui rend à `git log` la granularité que le journal de publication perd.

**D4 — `main` n'est pas protégée maintenant, et le déclencheur qui l'armera est mécanique.** Le calcul est au dossier : à 1,7 commit par demande et ≈ 10 min par demande, le flux obligatoire aurait coûté ≈ 4,5 h sur les 9,81 h d'existence du dépôt, soit 46 % de son temps, pour un temps rendu de zéro — 0 revert et 0 commit d'annulation sur 40 commits directs. Le point de bascule est à 14 incidents rattrapés, soit un commit sur trois défectueux. Le dénominateur cesse d'être nul quand le relecteur n'est plus l'auteur. **Une étape ajoutée au workflow existant compte les auteurs hors robots et échoue s'il y en a plus d'un sans protection active** ; le déclencheur se déclenche donc tout seul.

**D5 — La règle de nommage est `<contributeur>/<slug>`, et les branches qu'un outil se nomme sont exemptées nommément.** release-please est cité comme exemption, l'outil nommé. La règle générale n'est pas élargie pour l'accueillir : une règle assouplie autour d'une forme d'outil est une règle dont plus personne ne peut dire, six semaines plus tard, quelle part vient d'une décision.

**D6 — Un contrôle qui bloque nomme sa règle et sa voie de contestation, et s'adresse à qui peut s'y conformer.** Le jeu fermé de types est aujourd'hui une norme, appliquée par la relecture ; le contrôle de titre le fera migrer vers l'architecture, c'est-à-dire de ce qui se sanctionne après vers ce qui empêche avant, sans notification. Le message d'échec de tout contrôle bloquant doit donc nommer la règle, l'endroit où elle est écrite, et la manière de la contester — exigence à satisfaire au moment de construire l'instrument, jamais après. La sentinelle de D4, elle, reste déclenchée par la poussée vers `main` : sous écrasement, celui qui pousse est celui qui fusionne, donc celui qui peut armer la protection. Déplacée sur les demandes de fusion, elle sanctionnerait un contributeur sans aucun moyen d'obéir.

**Ce que cet ADR ne fait pas.** Il ne supersède ni `adr/0001` ni `adr/0002` : il tranche ce que les deux ont explicitement laissé ouvert, sans revenir sur aucune de leurs décisions. La décision D5 de `adr/0001`, maintenue en force par `adr/0002` — aucun outil de vérification des messages avant trois non-conformités sur `main` — reste intacte, et son déclencheur n'est pas avancé. Cet ADR corrige seulement **l'instrument que ce déclencheur désignera** : sous écrasement, un hook `commit-msg` s'exécute sur la machine de l'auteur, avant que la demande n'existe, et ne voit jamais le message qui atteindra `main`. Le premier candidat devient un contrôle du titre de la demande, en CI.

### Consequences

- Bon, parce que la méthode de fusion cesse de dépendre du geste : une seule est offerte, donc une seule est employée.
- Bon, parce que le message atteignant `main` a désormais une source unique et prévisible, ce qui est la condition pour que le calcul de version d'`adr/0002` repose sur quelque chose de stable.
- Bon, parce que les deux règles qui, sinon, n'auraient tenu que par la mémoire — supprimer la branche, armer la protection — sont mécanisées, l'une par la forge, l'autre par quatre lignes de shell dans un job qui s'exécute déjà.
- Bon, parce que la politique entre par décision et n'ajoute aucune dépendance : de la prose, quatre réglages, une étape de CI.
- Neutre, parce que la protection de `main` est décidée sans être active. C'est une position datée, pas une position molle, et la sentinelle en est la preuve.
- **Mauvais, parce que le point de panne du calcul de version se déplace vers le titre de la demande, et qu'un titre sur trois mesuré n'était pas conforme.** Un `feat` écrasé sous un titre `fix` produit une version basse que rien ne signale. C'est le coût sans mitigation qu'`adr/0002` a accepté ; l'écrasement le déplace sans le réduire, et D5 interdit de construire le contrôle avant que son déclencheur ne soit tiré.
- Mauvais, parce que l'écrasement détruit la granularité du journal de publication. Deux lignes sur cinq auraient disparu du `CHANGELOG.md` sur les trois demandes existantes. Le corps du commit les conserve ; le journal publié, non.
- Mauvais, parce que quatre réglages de forge deviennent porteurs de sens alors que la forge ne conserve aucun motif. Ils sont écrits ici et au README, et c'est un troisième point de dérive silencieuse, après la table de correspondance et `REGISTRE.md`.
- Mauvais, parce que les trois ADR du dépôt portent `consulted: —`. Les règles écrites ici lieront un contributeur qui n'est pas encore au dossier, et aucun message d'échec bien rédigé n'y remédie : la voie de recours reste la pétition auprès d'un décideur unique, ou la sortie par la licence CC BY-SA. C'est un fait de la situation — il n'y avait personne à consulter — et non un fait corrigé par cet ADR.
- Mauvais, parce que la sentinelle de contributeurs est un second instrument maison non testé automatiquement, dans un dépôt qui en comptait déjà un. Le facteur de bus ne s'améliore pas.

### Confirmation

- **Méthode unique** — `gh api repos/:owner/:repo` rend `allow_merge_commit: false`, `allow_rebase_merge: false`, `allow_squash_merge: true`, `delete_branch_on_merge: true`, `squash_merge_commit_title: "PR_TITLE"`.
- **Linéarité** — `git log --merges --oneline` sur `main` ne retourne aucune ligne.
- **Aucune branche orpheline** — le croisement des demandes fusionnées et des branches distantes est vide. Le contrôle **ne peut pas** s'écrire avec `git branch -r --merged` : sous écrasement, une branche fusionnée n'est jamais un ancêtre de `main`, et la commande passe toujours sans rien vérifier.
- **Sentinelle armée** — sur un dépôt à deux contributeurs hors robots et sans protection active, le workflow échoue.
- **Titres conformes** — au premier bilan, relecture des titres des demandes fusionnées depuis l'adoption ; au-delà de trois non conformes, le déclencheur de D5 est tiré et l'instrument à construire est le contrôle de titre en CI.

## Pros and Cons of the Options

### Politique écrite, forge réglée, protection différée et armée par une sentinelle

- Bon, parce qu'elle sépare ce qui coûte aujourd'hui de ce qui rendra demain, sur un chiffre plutôt que sur une intuition.
- Bon, parce que ce qui est différé ne dépend pas de la mémoire de qui l'a différé.
- Bon, parce que l'essentiel se fait par des réglages existants, sans rien écrire.
- Neutre, parce qu'elle laisse `main` ouverte pendant une durée que personne ne connaît.
- Mauvais, parce qu'elle ajoute une étape de CI maison, donc une chose de plus à entretenir.

### Protection de `main` armée immédiatement

- Bon, parce que la politique serait entière et vérifiable dès aujourd'hui, sans état transitoire.
- Bon, parce qu'aucune sentinelle ne serait nécessaire.
- Mauvais, parce qu'elle coûte ≈ 46 % du temps du dépôt pour un temps rendu mesuré à zéro.
- Mauvais, parce qu'une cérémonie sans contrepartie s'abandonne, et qu'une règle abandonnée est pire qu'une règle absente.

### Politique écrite en prose seule

- Bon, parce qu'elle ne touche à rien et se relit d'un seul endroit.
- Bon, parce qu'elle n'ajoute aucune ligne exécutable au dépôt.
- Mauvais, parce que la prose est déjà démentie par les faits : trois branches orphelines sur trois, deux méthodes de fusion sur trois demandes.
- Mauvais, parce qu'elle laisse en place les réglages qui produisent la faute, en se contentant de la déconseiller.

### Refus argumenté

- Bon, parce que c'est la forme que le dépôt maîtrise le mieux, et qu'elle ne coûte rien.
- Bon, parce que rien n'oblige un dépôt à auteur unique à se doter d'un flux.
- Mauvais, parce que trois documents renvoient déjà à cet ADR : le refus les laisserait tous les trois en suspens.
- Mauvais, parce qu'il ne corrige aucun des réglages qui produisent aujourd'hui de la méthode sans décision.

## More Information

Mesures à l'appui, prises sur `HEAD` au 2026-08-08 : 9,81 h d'existence, 45 commits, 1 auteur, 4,6 commits/heure. Les trois demandes de fusion ont duré 12 min 38 s, 3 min 21 s et 1 min 18 s de l'ouverture à la fusion, pour 1, 2 et 2 commits. Sur ces trois demandes, un titre ne portait aucun préfixe de type.

La méthode de fusion — écrasement pour `main`, rebasage pour mettre à jour — a été tranchée par l'auteur en cours de rédaction ; le reste de cet ADR en tire les conséquences plutôt que de la rouvrir. Le coût de l'écrasement a été chiffré après coup, dans `openspec/changes/politique-de-branche/proposal.md`, où le calcul complet est consigné avec le marqueur de la voix qui l'a produit.

L'option 2 restera disponible sans nouvel ADR le jour où la sentinelle se déclenchera : elle est la suite prévue de cette décision, non son alternative écartée pour toujours.

Réexamen prévu : au déclenchement de la sentinelle de contributeurs, ou à la première version fausse produite par un titre de demande mal typé.
