## ADDED Requirements

### Requirement: `main` est la seule branche de publication

`main` MUST être la branche par défaut du dépôt et la seule depuis laquelle une publication est produite. Aucune autre branche MUST être balisée, et aucun autre nom MUST porter d'état publié. Toute branche autre que `main` MUST être considérée comme temporaire, quelle que soit sa durée réelle d'existence.

#### Scenario: Publication déclenchée
- **WHEN** un commit arrive sur `main`
- **THEN** la CI de publication s'exécute et peut ouvrir une demande de publication

#### Scenario: Commit sur une branche de travail
- **WHEN** un commit arrive sur `tritri/politique-de-branche`
- **THEN** aucune balise n'est posée et aucun numéro de version n'est calculé

#### Scenario: Branche de longue durée
- **WHEN** quelqu'un propose une branche `develop` ou `next` vivant en parallèle de `main`
- **THEN** elle ne satisfait pas cette exigence — le dépôt n'a qu'une ligne publiable

### Requirement: Les branches de travail sont de courte durée et supprimées après fusion

Une branche de travail MUST être supprimée une fois fusionnée, sur le dépôt distant comme en local. Elle MUST NOT survivre à la demande qui l'a portée. La politique MUST NOT prescrire par quel mécanisme la branche existe sur la machine de l'auteur : les arbres de travail sous `.claude/worktrees/` sont un usage constaté, non une exigence.

#### Scenario: Après fusion
- **WHEN** une demande de fusion est fusionnée
- **THEN** sa branche est supprimée du distant par la forge, sans geste de l'auteur
- **AND** `git branch -r` ne la montre plus après `git fetch --prune`

#### Scenario: Branche fusionnée encore présente
- **WHEN** une branche portée par une demande déjà fusionnée existe encore sur le distant
- **THEN** cette exigence n'est pas satisfaite, et la branche est supprimée
- **AND** le contrôle MUST NOT reposer sur `git branch -r --merged` : sous écrasement, la branche n'est jamais un ancêtre de `main`, et la commande n'en retourne aucune alors même que trois subsistent

#### Scenario: Choix du mécanisme local
- **WHEN** un contributeur travaille dans un clone simple plutôt que dans un arbre de travail
- **THEN** il satisfait cette exigence — le mécanisme local n'est pas prescrit

### Requirement: Nommage des branches, et exemption nommée des branches d'outil

Une **branche de travail** que le dépôt nomme MUST porter la forme `<contributeur>/<slug>`, où `<contributeur>` est l'identifiant du contributeur et `<slug>` une suite de segments en minuscules séparés par des tirets, chaque segment étant fait de lettres, de chiffres, ou des deux — soit `^[a-z0-9]+/[a-z0-9]+(-[a-z0-9]+)*$`. Les chiffres sont admis parce que l'outillage de travail suffixe les noms qu'il génère, et qu'une règle démentie par quatre branches sur cinq dès le premier jour ne serait pas une règle.

`main` MUST être exclue de cette forme. Elle n'est pas une branche de travail : l'exigence « `main` est la seule branche de publication » la nomme et lui donne son statut.

Une branche qu'**un outil se nomme lui-même** MUST être exemptée de cette forme, et l'exemption MUST citer l'outil concerné. La règle générale MUST NOT être élargie pour accueillir la forme d'un outil : l'exemption s'écrit comme une exemption, afin qu'un lecteur puisse dire quelle partie de la règle vient d'une décision et quelle partie vient d'une dépendance.

Outils exemptés à ce jour : **release-please**, qui nomme sa branche `release-please--branches--<base>--components--<composant>`.

#### Scenario: Branche de travail nommée par le dépôt
- **WHEN** l'auteur ouvre une branche pour la politique de branche
- **THEN** elle s'appelle `tritri/politique-de-branche`

#### Scenario: Suffixe généré par l'outillage
- **WHEN** l'outillage nomme `tritri/nouvelle-politique-branche-c03202`
- **THEN** elle est conforme — le segment `c03202` est admis

#### Scenario: `main`
- **WHEN** on confronte `main` à la forme `<contributeur>/<slug>`
- **THEN** elle n'y est pas soumise, étant exclue nommément

#### Scenario: Branche nommée par release-please
- **WHEN** release-please pousse `release-please--branches--main--components--incongru-voix`
- **THEN** elle est conforme au titre de l'exemption, sans que la règle générale ait été modifiée

#### Scenario: Élargissement de la règle générale pour un outil
- **WHEN** quelqu'un propose d'assouplir `<contributeur>/<slug>` afin que la branche de release-please y entre
- **THEN** cela ne satisfait pas cette exigence — l'exemption est nommée, la règle n'est pas diluée

#### Scenario: Nouvel outil nommant ses branches
- **WHEN** un second outil se met à nommer ses propres branches
- **THEN** il entre dans la liste des exemptions par un commit modifiant cette exigence, avant tout usage

### Requirement: Une seule méthode de fusion, et une seule méthode de mise à jour

Rejoindre `main` MUST se faire par **écrasement** (*squash*). Mettre à jour une branche de travail depuis `main` MUST se faire par **rebasage**. Le dépôt MUST NOT autoriser d'autre méthode de fusion dans sa configuration, afin que la méthode ne dépende pas du geste de celui qui fusionne.

L'historique de `main` MUST donc rester linéaire, et cette linéarité devient une propriété voulue plutôt qu'un état constaté.

#### Scenario: Fusion d'une demande
- **WHEN** une demande de fusion portant trois commits est acceptée
- **THEN** un seul commit arrive sur `main`

#### Scenario: Mise à jour d'une branche en retard
- **WHEN** `main` a avancé depuis l'ouverture de la branche
- **THEN** la branche est rebasée sur `main`, et aucun commit de fusion n'apparaît

#### Scenario: Linéarité vérifiable
- **WHEN** on exécute `git log --merges --oneline` sur `main`
- **THEN** la commande ne retourne aucune ligne

#### Scenario: Méthode laissée au choix
- **WHEN** la configuration du dépôt autorise à la fois l'écrasement et la fusion classique
- **THEN** cette exigence n'est pas satisfaite — deux méthodes disponibles produisent deux méthodes employées

### Requirement: Sous écrasement, le titre de la demande est le message qui fait autorité

L'écrasement remplace les messages des commits d'une branche par le titre de la demande de fusion. Ce titre MUST donc satisfaire la capacité `convention-commits` en entier : forme `type(scope): description`, jeux fermés, et description portant un constat plutôt qu'une étiquette.

Quand une branche porte des commits de types différents, le titre MUST porter le type produisant le niveau de version le plus élevé parmi eux. Un `feat` écrasé sous un titre `fix` produit une version fausse que rien ne signale — c'est le coût sans mitigation que `adr/0002` a accepté, et l'écrasement en déplace le point d'apparition.

Le déclencheur de la décision D5 — aucun outil de vérification des messages jusqu'à trois messages non conformes sur `main` —, maintenu en force par `adr/0002`, MUST viser un contrôle du **titre de la demande**, exécuté en CI. Un hook `commit-msg` MUST NOT être retenu comme réponse à ce déclencheur : il s'exécute sur la machine de l'auteur, avant que la demande n'existe, et ne voit donc jamais le message qui atteindra `main`.

#### Scenario: Titre conforme
- **WHEN** une branche corrige le chemin du journal de la sentinelle
- **THEN** le titre de sa demande est `fix(sentinelle): le journal survit à la session et ne plante plus le hook`

#### Scenario: Titre sans type
- **WHEN** une demande porte le titre `Le journal de la sentinelle survit à la session`
- **THEN** elle ne satisfait pas cette exigence — écrasée, elle poserait sur `main` un sujet invisible à l'outil de publication

#### Scenario: Branche portant plusieurs types
- **WHEN** une branche contient un `fix(sentinelle)` et un `feat(sentinelle)`
- **THEN** le titre de la demande porte `feat(sentinelle)`, qui est le niveau le plus élevé des deux

#### Scenario: Réponse au déclencheur de non-conformité
- **WHEN** trois messages non conformes sont arrivés sur `main`
- **THEN** l'instrument construit contrôle les titres de demande en CI, et non les messages de commit en local

### Requirement: Le poussé direct sur `main` est autorisé tant que le relecteur serait l'auteur

Le poussé direct sur `main` MUST rester autorisé aussi longtemps que le dépôt n'a qu'un seul contributeur, et `main` MUST NOT être protégée avant ce terme. Motif chiffré, consigné dans la proposition : la cérémonie coûte environ 4,5 h sur les 9,81 h d'existence du dépôt, et ne rend rien tant que le relecteur est l'auteur — 0 revert et 0 commit d'annulation sur 40 commits poussés en direct.

La protection MUST être armée **avant la première fusion d'un second contributeur**, ce moment étant le seul où le dénominateur cesse d'être nul. Une fois armée, elle MUST exiger une demande de fusion pour tout changement de `main`, et MUST laisser fusionnable la demande ouverte par release-please.

#### Scenario: Auteur unique
- **WHEN** `git shortlog -sn` ne retourne qu'un contributeur
- **THEN** le poussé direct sur `main` est conforme, et l'absence de protection aussi

#### Scenario: Arrivée d'un second contributeur
- **WHEN** un second contributeur ouvre sa première demande de fusion
- **THEN** la protection de `main` est activée avant que cette demande ne soit fusionnée

#### Scenario: Protection armée et publication
- **WHEN** `main` est protégée et release-please ouvre sa demande de publication
- **THEN** cette demande reste fusionnable par un humain, la protection ne la bloquant pas

#### Scenario: Protection armée prématurément
- **WHEN** `main` est protégée alors que le dépôt n'a qu'un contributeur
- **THEN** cette exigence n'est pas satisfaite — le coût est payé sans contrepartie, et le calcul est au dossier

### Requirement: Tout contrôle qui bloque nomme sa règle et sa voie de contestation

Un contrôle automatique qui empêche un changement d'aboutir MUST, dans son message d'échec, nommer la règle appliquée, l'endroit du dépôt où elle est écrite, et la voie par laquelle elle se conteste. Une contrainte inscrite dans l'outillage s'applique avant le fait, sans notification et sans exception ; le message d'échec est le seul endroit où la personne contrainte peut apprendre qu'une règle vient de lui être opposée.

Cette exigence MUST être satisfaite au moment où l'instrument est construit, et MUST NOT être différée à un ajustement ultérieur.

#### Scenario: Contrôle de titre refusant une demande
- **WHEN** le contrôle de titre en CI refuse `Ajout du support des greffons`
- **THEN** son message nomme l'exigence de forme, cite le chemin de la spec `convention-commits`, et indique que le jeu de types s'élargit par modification de cette spec

#### Scenario: Message d'échec muet
- **WHEN** un contrôle échoue en affichant seulement `title check failed`
- **THEN** cette exigence n'est pas satisfaite — la personne contrainte ignore quelle règle s'applique et comment la contester

#### Scenario: Migration d'une norme vers l'outillage
- **WHEN** une règle jusque-là tenue par la relecture humaine devient vérifiée par un contrôle bloquant
- **THEN** le contrôle porte sa règle et sa voie de contestation dès sa première version

### Requirement: La sentinelle de contributeurs s'adresse à qui peut s'y conformer

La sentinelle de contributeurs MUST se déclencher sur la poussée vers `main`, et MUST NOT être déplacée vers un déclencheur de demande de fusion. Sous écrasement, celui qui pousse sur `main` est celui qui fusionne, c'est-à-dire la personne qui détient les droits d'armer la protection. Déclenchée sur une demande, la sentinelle ferait échouer le travail d'un contributeur qui n'a aucun moyen d'obéir.

L'asymétrie entre qui peut déroger à la protection de `main` et qui ne le peut pas MUST être écrite au `README.md` avec son motif, plutôt que découverte en s'y heurtant.

#### Scenario: Déclencheur conservé
- **WHEN** un second contributeur hors robot apparaît et qu'aucune protection n'est active
- **THEN** l'échec survient sur la poussée vers `main`, donc auprès de qui peut armer la protection

#### Scenario: Déclencheur déplacé
- **WHEN** la sentinelle est déplacée sur `pull_request`
- **THEN** cette exigence n'est pas satisfaite — elle sanctionnerait la demande du nouveau venu, qui n'a ni les droits d'administration ni la main sur le workflow

#### Scenario: Asymétrie de dérogation
- **WHEN** un contributeur cherche à savoir qui peut contourner la protection de `main`
- **THEN** il le lit au `README.md`, avec le motif, sans avoir à l'essayer

### Requirement: L'historique antérieur à la politique n'est pas réécrit

Les 40 commits poussés en direct sur `main` avant l'adoption MUST NOT être réécrits, ni regroupés, ni rejoués derrière une demande de fusion rétroactive. Le dépôt tient la même règle pour ses archives et pour ses messages de commit : un état antérieur est *antérieur*, non *invalide*.

#### Scenario: Historique mixte
- **WHEN** on inspecte `main` et qu'on y trouve 40 commits directs suivis de commits écrasés
- **THEN** les deux régimes coexistent, et aucun n'est corrigé pour ressembler à l'autre

#### Scenario: Proposition de réécriture
- **WHEN** quelqu'un propose de rejouer l'historique pour qu'il paraisse conforme à la politique
- **THEN** cela ne satisfait pas cette exigence

### Requirement: La politique entre par décision, et n'ajoute aucune dépendance

Cette politique MUST être adoptée par un ADR versionné au dépôt, conformément à la règle de `REGISTRE.md` selon laquelle une prescription de méthode entre par décision et non par effet de bord. Elle MUST NOT ajouter de dépendance runtime : sa seule mise en œuvre non textuelle est la configuration du dépôt sur sa forge.

#### Scenario: Adoption
- **WHEN** la politique est adoptée
- **THEN** un ADR la consigne dans `adr/`, avec ses options écartées et son coût

#### Scenario: Politique héritée d'un outil
- **WHEN** un outil installé prescrit un flux de travail non consigné par un ADR
- **THEN** cette exigence n'est pas satisfaite — c'est le motif exact du retrait d'`openspec-git-discipline`

#### Scenario: Mise en œuvre
- **WHEN** on inventorie ce que la politique installe
- **THEN** on ne trouve que de la prose et des réglages de forge, et rien chez l'usager
