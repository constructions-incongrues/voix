## Context

La proposition établit le vide — aucune politique de branche décidée, 40 commits poussés en direct — et le chiffre. Ce document dit comment la politique s'installe, et surtout **où elle s'installe** : très peu dans de la prose, beaucoup dans quatre réglages de forge que personne n'a jamais regardés.

**ADR en force.** `adr/` contient deux fichiers. `adr/0002` porte `supersedes: ADR-0001` ; l'ensemble en vigueur se réduit donc à **`adr/0002` seul**. `adr/0001` est du contexte historique et ne contraint plus rien par lui-même — sauf ce que `adr/0002` en a explicitement repris : ses garde-fous 1, 3 et 4, et la décision D5 (aucun outil de vérification des messages avant trois non-conformités sur `main`), maintenue « sous son déclencheur d'origine ». Ce design est écrit contre `adr/0002` et contre lui seul.

**État réel de la forge**, relevé par l'API GitHub sur `constructions-incongrues/voix` :

| Réglage | Valeur constatée | Ce que ça produit |
|---|---|---|
| `allow_merge_commit` | `true` | trois méthodes offertes |
| `allow_rebase_merge` | `true` | → deux méthodes employées sur trois demandes |
| `allow_squash_merge` | `true` | |
| `delete_branch_on_merge` | `false` | **3 branches sur 3 déjà fusionnées subsistent** sur le distant |
| `squash_merge_commit_title` | `COMMIT_OR_PR_TITLE` | le titre du commit dépend du **nombre de commits de la branche** |
| `squash_merge_commit_message` | `COMMIT_MESSAGES` | le corps liste les messages des commits écrasés |

Deux de ces lignes ne sont pas de la configuration inerte, ce sont des décisions prises par défaut :

- `COMMIT_OR_PR_TITLE` signifie : *si la branche n'a qu'un commit, prends son sujet ; sinon, prends le titre de la demande.* Le message qui atteint `main` change donc de source selon un critère que personne n'a choisi. L'exigence « le titre de la demande fait autorité » est **fausse aujourd'hui**, et le serait la moitié du temps.
- `delete_branch_on_merge: false` explique à lui seul les trois branches orphelines. Ce n'est pas un oubli de l'auteur, c'est un réglage.

**Contrainte de méthode.** `REGISTRE.md` exige qu'une prescription de méthode entre par décision. Un réglage de forge est une prescription de méthode qui ne laisse aucune trace dans le dépôt : c'est le pire cas de la règle, et c'est pourquoi chaque réglage retenu ci-dessous est écrit ici avec son motif.

## Goals / Non-Goals

**Goals :**

- Rendre la méthode de fusion **non optionnelle au moment du geste** : une seule méthode disponible, donc une seule employée.
- Rendre le message qui atteint `main` **prévisible**, quel que soit le nombre de commits de la branche.
- Rendre **mécaniques** les deux règles qui, sinon, ne tiennent que par la mémoire : la suppression des branches et l'armement de la protection.
- Écrire dans le dépôt le motif de chaque réglage de forge, puisque la forge n'en garde aucun.

**Non-Goals :**

- Construire le contrôle de conformité des titres. D5 est en force ; son déclencheur n'est pas tiré. Ce design nomme l'instrument à construire, il ne le construit pas.
- Protéger `main` maintenant. Le calcul de la proposition donne le seuil ; l'armement est daté, pas immédiat.
- Réécrire ou regrouper l'historique existant.
- Prescrire l'outillage local de qui contribue — arbres de travail, clones, alias.

## Decisions

### D1 — Une seule méthode offerte par la forge, pas seulement une seule prescrite

`allow_merge_commit: false`, `allow_rebase_merge: false`, `allow_squash_merge: true`.

Trois méthodes sont offertes aujourd'hui, et trois demandes en ont employé deux. Une politique écrite qui laisse les trois boutons en place se fait démentir par le premier geste distrait ; c'est le reproche que `adr/0002` adressait à l'option « corriger le numéro à la main quand il paraît faux » — une règle qu'on applique tant qu'on s'en souvient, puis plus. La forge doit rendre la faute impossible plutôt que déconseillée.

*Point qui paraît contradictoire et ne l'est pas :* désactiver `allow_rebase_merge` n'interdit pas le rebasage. Ce réglage ne gouverne que le bouton « Rebase and merge » de la forge. Mettre à jour sa branche par `git rebase main` reste la méthode prescrite, et se fait en local, hors de portée de ce réglage.

*Alternatives.* **Tout laisser ouvert et écrire la règle en prose** — rejeté : c'est l'état actuel, et il a produit deux méthodes sur trois demandes. **N'autoriser que la fusion classique** — rejeté : produit des commits de fusion, et l'historique linéaire est constaté depuis 45 commits ; en faire une propriété voulue coûte moins que de le perdre.

### D2 — `squash_merge_commit_title: PR_TITLE`, et le corps conserve les messages écrasés

Le réglage actuel, `COMMIT_OR_PR_TITLE`, fait dépendre la source du sujet du nombre de commits de la branche. Puisque le sujet qui atteint `main` est ce que release-please lit pour calculer une version, sa source ne peut pas être une variable cachée. `PR_TITLE` la fixe : **le titre de la demande, toujours, quel que soit le nombre de commits.**

`squash_merge_commit_message` reste à `COMMIT_MESSAGES`. C'est gratuit et ça rend deux choses :

1. Le corps du commit d'écrasement liste les messages des commits de la branche. La granularité que l'écrasement détruit dans le journal de publication survit dans l'historique — les « 2 lignes perdues sur 5 » du calcul de la proposition sont perdues pour le `CHANGELOG.md`, pas pour `git log`.
2. Un pied de page `BREAKING CHANGE:` posé sur un commit intermédiaire remonte dans le corps de l'écrasement, où release-please le lit. Sans ce réglage, il serait purement perdu.

*Effet de bord à connaître, sans conséquence aujourd'hui :* un `BREAKING CHANGE:` remontant par ce chemin déclenche une rupture non voulue. Sous `1.0.0`, la configuration du dépôt ramène toute rupture à un niveau mineur — le README l'écrit — donc le risque est nul jusqu'au franchissement de la 1.0, où il redevient réel en même temps que tous les autres.

*Alternative.* **`PR_BODY` ou message vide** — rejeté : coûte les deux bénéfices ci-dessus et ne rend rien.

### D3 — `delete_branch_on_merge: true` : la suppression cesse d'être un geste

Trois branches sur trois demandes fusionnées subsistent sur le distant. L'exigence « la branche est supprimée après fusion » est donc **violée à 100 % au moment de l'écrire**, ce qui est le meilleur argument possible contre la version prose de cette règle. La forge sait le faire ; le réglage existe ; il est à `false`.

*Contrôle, et pourquoi le contrôle évident est faux.* Sous écrasement, la branche fusionnée **n'est jamais un ancêtre de `main`** : `git branch -r --merged origin/main` ne retourne rien, alors que trois branches orphelines sont présentes. Une vérification écrite avec cette commande passerait toujours, sans rien vérifier. Le contrôle correct croise les demandes fusionnées et les branches distantes :

```
gh pr list --state merged --json headRefName -q '.[].headRefName' \
  | while read b; do git show-ref -q --verify "refs/remotes/origin/$b" && echo "orpheline: $b"; done
```

### D4 — La protection de `main` est écrite maintenant, armée par une sentinelle de contributeurs

Le calcul de la proposition situe le seuil : la protection ne rend rien tant que le relecteur est l'auteur, et coûte ≈ 46 % du temps du dépôt si on l'arme aujourd'hui. Le dénominateur cesse d'être nul au second contributeur.

Le problème n'est donc pas *quoi* décider, c'est **comment le déclencheur se déclenche**. « On l'armera au second contributeur » a exactement la forme que `adr/0002` a rejetée : une règle qui tient par la mémoire. Elle sera oubliée, et elle sera oubliée précisément le jour où quelqu'un d'autre arrive, c'est-à-dire le seul jour où elle comptait.

Décision : **une étape ajoutée au workflow `release-please.yml` existant**, qui compte les auteurs hors robots sur `main` et échoue quand il y en a plus d'un tant qu'aucune protection n'est active. Le déclencheur devient mécanique. Coût : quelques lignes de shell dans un job qui s'exécute déjà à chaque poussée sur `main` ; aucune dépendance, aucune Action supplémentaire, rien chez l'usager.

*Alternatives.* **Créer la protection maintenant avec l'auteur en dérogation** — rejeté : l'armement redevient un geste dont il faut se souvenir (se retirer de la liste), et entre-temps les réglages affichent une branche protégée qui ne l'est pas. **Ne rien mécaniser et faire confiance à l'ADR** — rejeté pour le motif ci-dessus. **Armer la protection tout de suite** — rejeté par le chiffre.

### D5 — L'instrument de conformité est nommé, pas construit

D5 de `adr/0001`, maintenue en force par `adr/0002`, tient : aucun outil de vérification des messages avant trois non-conformités sur `main`. Ce design ne le construit pas et n'avance pas son déclencheur.

Il corrige en revanche **l'instrument que ce déclencheur désigne**. Sous écrasement, le message qui atteint `main` est le titre de la demande ; un hook `commit-msg` s'exécute sur la machine de l'auteur, avant que la demande n'existe, et ne le voit jamais. Le premier candidat devient un job `on: pull_request` vérifiant le titre par la même expression rationnelle que celle déjà écrite au README pour l'auto-contrôle de conformité.

*Mesure à l'appui :* sur les trois demandes existantes, **un titre sur trois n'était pas conforme** — celui de #1, sans préfixe de type. Ce n'est pas un risque théorique, c'est un taux observé de 33 % sur un échantillon de trois.

### D6 — La règle de nommage cite ses exemptions au lieu de s'élargir

`<contributeur>/<slug>` décrit les quatre branches de travail que le dépôt a nommées jusqu'ici ; aucune n'est à renommer. **La règle a été confrontée aux branches réelles avant d'être écrite, et l'a d'abord été à tort** : dans une première rédaction, `main` y était soumise et échouait, et deux branches sur quatre échouaient sur leur suffixe numérique.

Deux précisions en découlent, l'une et l'autre nées de la confrontation :

- **`main` est exclue.** Ce n'est pas une branche de travail ; l'exigence qui en fait la seule branche de publication la nomme déjà et lui donne son statut. Sans cette exclusion, la spec exigeait de `main` une forme que son propre nom interdit.
- **Le slug admet les chiffres** — `^[a-z0-9]+/[a-z0-9]+(-[a-z0-9]+)*$`. L'outillage suffixe les noms qu'il génère (`-c03202`, `-934146`), et une règle démentie par quatre branches sur cinq dès le premier jour ne serait pas une règle. C'est une concession à l'outillage, et elle est écrite comme telle plutôt que découverte au premier refus. La branche que release-please se nomme est exemptée **nommément**, l'outil étant cité.

Le motif est de lisibilité, pas de pureté : une règle assouplie pour accueillir `release-please--branches--main--components--incongru-voix` est une règle dont plus personne, six semaines plus tard, ne peut dire quelle part vient d'une décision et quelle part vient d'une dépendance. L'exemption citée garde cette frontière visible. Coût : une ligne.

*Alternative.* **Un motif générique acceptant les deux formes** — rejeté : la forme de l'outil devient la forme du dépôt, sans trace.

## Risks / Trade-offs

- **Un `feat` écrasé sous un titre `fix` produit une version basse, et rien ne le signale.** → Sans mitigation. C'est le coût que `adr/0002` a accepté explicitement ; l'écrasement en déplace le point d'apparition du message de commit vers le titre de la demande, sans l'aggraver ni le réduire. L'exigence de spec impose au titre de porter le type le plus élevé de la branche ; c'est une discipline, pas un contrôle, jusqu'à ce que D5 se déclenche.
- **Le titre de la demande devient un point de panne unique.** → Il est relu au moment de fusionner, moment où il est encore modifiable — ce qui n'est pas vrai d'un message de commit déjà poussé. Le risque est réel et la fenêtre de correction est meilleure qu'avant.
- **La sentinelle de contributeurs comptera les robots.** → `github-actions[bot]` signe les commits de publication. Le compte doit filtrer les auteurs dont le nom se termine par `[bot]`, sans quoi la protection s'arme à la première publication — c'est-à-dire tout de suite, et à contre-emploi.
- **Quatre réglages de forge sont désormais porteurs de sens, et la forge ne conserve aucun motif.** → Ils sont écrits ici et repris au README. Le risque de dérive silencieuse est réel et connu : `adr/0002` a déjà nommé le même pour la table du README.
- **Le rebasage d'une branche partagée réécrit l'histoire sous les pieds d'un tiers.** → Sans objet tant que l'auteur est unique ; borné ensuite par la règle des branches de courte durée à un seul auteur. À reprendre si une branche à plusieurs mains devient nécessaire.
- **Ce design ajoute une étape de CI, donc du code exécuté sur le dépôt.** → Quelques lignes de shell dans un job existant, lisibles et supprimables. `adr/0002` a déjà accepté la dépendance de processus qu'est une Action ; ceci n'en ajoute pas une seconde.

## Migration Plan

1. **Régler la forge** — `allow_merge_commit: false`, `allow_rebase_merge: false`, `delete_branch_on_merge: true`, `squash_merge_commit_title: PR_TITLE`. Quatre champs, une requête `gh api -X PATCH`.
2. **Supprimer les trois branches orphelines** — `tritri/nanopm-product-934146`, `tritri/conventional-commits`, `tritri/release-please`, toutes portées par des demandes fusionnées.
3. **Ajouter la sentinelle de contributeurs** au workflow `release-please.yml`, robots exclus du compte.
4. **Écrire la section README** — le chemin d'un changement jusqu'à `main`, la règle de nommage et son exemption citée, et les quatre réglages avec leur motif.
5. **Relire `REGISTRE.md` ligne 100** — le motif de retrait d'`openspec-git-discipline` invoque une politique non tranchée. Elle l'est ; la skill reste retirée, mais pour un motif qui devient « ce dépôt a tranché autrement », et la ligne doit le dire.

**Rollback.** Les étapes 1 et 3 se défont en une requête et une suppression de bloc. La politique elle-même est de la prose : rien à désinstaller, rien à migrer, aucun état à reprendre.

## Les quatre modalités, et qui peut faire appel

<!-- incongru-voix: lessig — le jeu fermé de types migre de la norme vers l'architecture au déclenchement de D5 — recours: aucun tant que le message d'échec ne nomme ni la règle ni la voie -->

Cinq contraintes de ce changement s'appliqueront à quelqu'un qui n'a signé aucun de ces ADR. Le tableau les remplit ; la ligne qui compte est la dernière de chaque bloc.

| Contrainte | loi | norme | prix du contournement | architecture | **recours** |
|---|---|---|---|---|---|
| **C1** — une seule méthode de fusion offerte | `adr/0003` D2 | néant | nul pour qui a les droits d'écriture ; sans objet pour qui ne les a pas | totale sur le bouton | **ADR successeur**, voie écrite et déjà exercée deux fois |
| **C2** — suppression de la branche à la fusion | `adr/0003` D1 | néant | nul | totale, sans notification | **« Restore branch »**, un clic, sans limite de temps ; la copie locale subsiste |
| **C3** — jeu fermé de types et de scopes dans le titre | `adr/0002`, spec `convention-commits` | réelle : la relecture au moment de fusionner | nul pour se conformer | **aucune aujourd'hui** — D5 interdit de construire le contrôle | **modification de la spec**, explicitement prévue, « jamais par usage de fait » |
| **C4** — sentinelle de contributeurs | `adr/0003` D4 | néant | retirer l'étape | totale : le workflow échoue | **aucun pour le nouveau venu** ; il n'a ni les droits d'admin ni la main sur le workflow |
| **C5** — protection de `main`, une fois armée | `adr/0003` D4 | néant | nul : ouvrir une demande | totale sur le poussé direct | **dérogation**, à la main du propriétaire seul, sans procédure écrite |

**Ce qui va bien, et qu'il faut dire avant le reste.** Quatre de ces cinq contraintes ont une voie de recours documentée, ce qui est rare. Le dépôt s'est doté d'une procédure d'amendement écrite — l'ADR successeur, avec sa règle d'immuabilité — et il l'a déjà employée. La licence est CC BY-SA 4.0 : la sortie est un droit, pas une tolérance, et quiconque conteste la politique peut emporter le dépôt entier. C'est le recours le plus fort qui existe, et il est concédé par écrit.

**C3 est le point dur, et il est différé.** Aujourd'hui, le jeu fermé de types est une norme : rien ne l'applique, la relecture humaine s'en charge, et un titre non conforme passe. Le jour où le déclencheur de D5 sera tiré, le contrôle de titre en CI le fera **migrer de la norme vers l'architecture** — de ce qui se sanctionne après vers ce qui empêche avant. À ce moment-là, un contributeur verra une CI rouge sans savoir quelle règle s'applique, où elle est écrite, ni comment la contester. La spec prévoit l'élargissement du jeu par modification ; elle ne prévoit nulle part que la personne contrainte en soit informée.

Ce n'est pas un procès d'intention : c'est la propriété ordinaire du code comme régulation. Il empêche sans notifier. La réparation coûte une ligne dans un message d'échec, et elle doit être exigée maintenant, pendant que l'instrument n'existe pas — écrite après coup, elle ne le sera pas.

**C4 est bien adressée, mais par accident du déclencheur.** La sentinelle s'exécute `on: push: branches: [main]`. Sous écrasement, celui qui pousse sur `main` est celui qui fusionne, c'est-à-dire le propriétaire — donc la personne qui peut effectivement armer la protection. La sanction atteint qui peut s'y conformer, ce qui est la condition minimale d'une contrainte légitime. Mais cette propriété tient au seul choix du déclencheur : **déplacer la sentinelle sur `pull_request` la ferait échouer sur la demande du nouveau venu**, c'est-à-dire sanctionner quelqu'un qui n'a aucun moyen d'obéir. Le déclencheur cesse alors d'être un détail d'implémentation et devient une garantie à conserver.

**C5 : l'asymétrie est légitime et n'est pas écrite.** Le propriétaire peut se placer en dérogation, un contributeur ne le peut pas. C'est normal pour un dépôt qui a un propriétaire, et il n'y a rien à corriger sur le fond. Mais une asymétrie non écrite se lit comme un oubli, et une asymétrie écrite se lit comme une constitution. Elle doit figurer au README avec son motif, sans quoi le premier contributeur la découvrira en s'y heurtant.

**Ce que cette analyse ne répare pas, et qu'il faut dire.** Ma conclusion est confortable pour celui qui détient déjà le pouvoir : deux messages d'erreur mieux rédigés, une phrase au README, et la politique devient défendable. C'est le propre de la position réformiste, et c'est le moment de signaler qu'elle arrive commodément. La question qu'elle contourne est ailleurs : **les trois ADR du dépôt portent `decision-makers: Tristan Rivoallan` et `consulted: —`.** Personne n'a jamais été consulté, parce qu'il n'y avait personne — c'est un fait, pas un reproche. Mais les règles écrites ici lieront quelqu'un qui n'existe pas encore au dossier, et aucun message d'échec bien rédigé ne change cela. Si le dépôt veut y répondre, c'est le champ `consulted:` qui doit cesser d'être un tiret, et ce n'est pas une question d'architecture.

**Deux exigences en découlent**, ajoutées à la spec : le message d'échec de tout contrôle nomme la règle et la voie de contestation, et la sentinelle reste déclenchée par la poussée sur `main`.

## Open Questions

- **La correction d'instrument de D5 relève-t-elle d'`adr/0003` ou d'une supersession d'`adr/0002` ?** `adr/0002` maintient D5 « sous son déclencheur d'origine » sans nommer d'instrument ; le hook `commit-msg` est nommé dans la prose d'`adr/0001`, qui est superséd et ne contraint plus. La lecture retenue ici est qu'`adr/0003` tranche une question laissée ouverte et précise un instrument devenu inadéquat, **sans superséder `adr/0002`**. L'étape ADR confirmera ou corrigera cette lecture — c'est elle qui décide, pas ce document.
- **Faut-il un contrôle de la table des réglages de forge ?** Quatre valeurs vivent hors du dépôt et peuvent changer sans commit. Un contrôle les comparerait à une liste versionnée. Coût non chiffré ici, et prématuré tant que la seule personne qui peut les modifier est celle qui les a posées — même structure d'argument que pour la protection de `main`, et probablement le même déclencheur.
