## ADDED Requirements

### Requirement: Détection sur l'artefact produit, pas sur la requête

La sentinelle MUST examiner le **travail non commité** — le diff plus les fichiers neufs — et NON la requête de l'utilisateur ni le transcript. Mesuré : les voix se déclenchent déjà d'elles-mêmes quand l'utilisateur formule une critique, et jamais quand la matière est dans le travail produit. Regarder la requête reviendrait à surveiller le seul endroit qui n'en a pas besoin.

Le hook ne reçoit aucune liste de fichiers écrits pendant le tour, et rien ne permet de la reconstituer sans instantané préalable. L'unité est donc le travail non commité, et le motif MUST NOT affirmer que le tour a écrit ces lignes : c'est le contenu qui est en question, pas son auteur.

#### Scenario: Travail ordinaire portant un artefact critiquable
- **QUAND** un tour se termine alors que le travail non commité relève de la question d'une voix inscrite
- **ALORS** la sentinelle l'examine, alors même que la requête ne contenait aucune critique

#### Scenario: Rien en cours
- **QUAND** un tour se termine sans aucun travail non commité
- **ALORS** la sentinelle ne fait rien

### Requirement: Aucun appel de modèle depuis le hook

La sentinelle MUST chercher les `Signaux` du registre dans le diff par correspondance textuelle, et MUST NOT engager d'appel de modèle depuis le hook. Sans correspondance, elle s'arrête sans rien coûter ; avec correspondance, elle pose la question au modèle en cours par le motif du blocage.

Mesuré : un aller-retour de modèle depuis un hook coûte 9 à 13 secondes de latence bloquante, et le hook est synchrone. Cette attente tomberait précisément sur les tours porteurs, c'est-à-dire ceux où l'utilisateur attend une réponse. Un dispositif qui se paie en attente aux moments intéressants sera éteint, et un dispositif éteint ne mesure plus rien.

#### Scenario: Diff sans aucun signal
- **QUAND** le diff ne contient aucun signal du registre
- **ALORS** la sentinelle s'arrête, sans coût ni latence

#### Scenario: Diff avec signaux
- **QUAND** le diff contient des signaux
- **ALORS** la sentinelle interrompt la fin de tour et pose la question au modèle en cours, sans appel de modèle supplémentaire

#### Scenario: Registre approximatif
- **QUAND** les `Signaux` d'une voix sont formulés trop vaguement pour discriminer
- **ALORS** c'est un défaut de fonctionnement de la sentinelle, et non une imprécision de documentation

### Requirement: La question posée est celle du seuil de silence

La sentinelle MUST demander *laquelle des questions inscrites est porteuse ici, et si sa réponse changerait la décision*. Elle MUST NOT demander si la chose examinée est capitaliste : la question est indécidable, sa réponse est toujours oui, et elle produit le dogme.

La seconde clause est décisive et distincte de la première. Une question peut être porteuse sans que sa réponse ne change rien — Illich a presque toujours quelque chose à dire d'un outil, Lessig d'un défaut imposé. Sans ce second filtre, le seuil d'un tour sur cinq est intenable.

#### Scenario: Question porteuse sans effet sur la décision
- **QUAND** une question inscrite s'applique mais que sa réponse ne changerait rien à ce qui a été écrit
- **ALORS** la sentinelle se tait

### Requirement: Convocation, jamais critique

Sur détection, la sentinelle MUST convoquer la voix porteuse et MUST NOT produire elle-même d'analyse. C'est la voix qui applique sa compétence et pose sa trace.

La convocation est le seul mécanisme mesuré comme fonctionnel : forcée, elle produit la compétence déclarée et une trace bien formée sur les quatre voix. Une analyse produite par la sentinelle serait un second chemin non éprouvé, et contournerait les voix — c'est-à-dire le dépôt entier.

#### Scenario: Voix porteuse identifiée
- **QUAND** la sentinelle identifie une voix porteuse
- **ALORS** elle nomme cette voix et laisse la voix produire l'analyse et la trace

### Requirement: Une seule convocation par tour

La sentinelle MUST NOT convoquer plus d'une voix par tour. Deux voix porteuses, la plus saillante est retenue et l'autre attend le tour suivant.

Un dispositif qui convoque trois voix d'affilée sera éteint le jour même, et un dispositif éteint ne mesure plus rien.

#### Scenario: Plusieurs voix porteuses
- **QUAND** le diff relève des questions de deux voix ou plus
- **ALORS** une seule est convoquée

### Requirement: Aucune convocation sur une voix déjà tracée

La sentinelle MUST NOT convoquer une voix dont le marqueur figure déjà dans le diff examiné. Un hook de fin de tour capable de bloquer peut bloquer sans fin ; le marqueur `incongru-voix: <voix>` sert de témoin et coûte une recherche textuelle déjà effectuée.

#### Scenario: Voix ayant déjà laissé sa trace
- **QUAND** le diff contient déjà le marqueur d'une voix
- **ALORS** cette voix n'est pas convoquée de nouveau

### Requirement: Réussite mesurée sur l'artefact, pas sur le déclenchement

La réussite de la sentinelle MUST être établie par le protocole d'apport — deux bras, même consigne, un artefact réel — et non par le fait qu'elle se soit déclenchée. Le critère est qu'après convocation, le fichier contienne une trace **et** un contenu que le bras sans voix ne produit pas.

Une sentinelle qui se déclenche correctement mais dont la voix n'apporte rien a coûté un tour à l'utilisateur pour rien. C'est ainsi qu'un dispositif se fait éteindre.

#### Scenario: Convocation réussie
- **QUAND** la sentinelle convoque une voix sur un artefact
- **ALORS** l'artefact porte ensuite un marqueur de trace et un contenu absent du bras baseline

### Requirement: Contrat du hook vérifié avant usage

Le contrat d'entrée et de sortie du hook MUST être établi par exécution d'un hook jetable avant que la logique de sentinelle ne soit écrite. Ce qu'il reçoit, ce qu'il doit rendre pour interrompre la fin de tour, et si le motif est réinjecté de façon exploitable.

Trois conclusions fausses ont été publiées le 8 août, toutes tirées de suppositions raisonnables sur un mécanisme non vérifié.

#### Scenario: Mécanisme supposé
- **QUAND** la conception repose sur un comportement de hook non observé
- **ALORS** ce comportement est vérifié empiriquement avant que quoi que ce soit ne soit construit dessus
