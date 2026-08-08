# format-voix

## Purpose

Le contrat que tout fichier de voix de la skillothèque doit satisfaire. Il existe pour deux raisons : rendre une voix **routable** — la sentinelle doit pouvoir décider de la convoquer sans lire son fichier — et rendre son effet **vérifiable**. Une voix qui ne satisfait pas ce contrat n'est pas admise au registre.

## Requirements

### Requirement: Quatre sections normalisées

Tout fichier de voix MUST contenir les quatre sections `## Question`, `## Signaux`, `## Compétence` et `## Trace`, à ce niveau de titre exact. Un fichier auquel il manque une section n'est pas une voix : la sentinelle ne pourra ni le router ni vérifier son effet.

#### Scenario: Voix complète
- **QUAND** un fichier de voix est ajouté à `skills/<nom>/SKILL.md`
- **ALORS** `grep -c '^## \(Question\|Signaux\|Compétence\|Trace\)$'` sur ce fichier retourne 4

#### Scenario: Voix incomplète refusée
- **QUAND** un fichier de voix ne contient que trois des quatre sections
- **ALORS** il est refusé à l'admission et n'est pas inscrit au registre

### Requirement: Question unique dans le dépôt

La section `## Question` MUST contenir une seule question, et cette question MUST être disjointe de celle de toutes les autres voix inscrites au registre. Deux voix qui posent la même question rendent le routage indécidable.

#### Scenario: Question déjà couverte
- **QUAND** une voix candidate pose une question qu'une voix inscrite pose déjà
- **ALORS** la candidate est refusée, et le refus est inscrit au registre avec son motif

### Requirement: Compétence exécutable, pas opinion

La section `## Compétence` MUST décrire ce que la voix sait **faire** — un calcul, une lecture de structure, une classification, une description de gouvernance. Elle MUST NOT se limiter à un point de vue. Une voix sans compétence propre est un costume.

#### Scenario: Compétence produisant un résultat
- **QUAND** une voix est convoquée sur un artefact relevant de sa question
- **ALORS** elle produit un résultat structuré (un nombre, un tableau, une liste, un jeu de règles), pas seulement un commentaire

### Requirement: Posture non-serviable déclarée en ouverture

Tout fichier de voix MUST ouvrir sur une section qui résout la tension centrale : livrer un travail réel sans adopter le registre du service. Le modèle éprouvé est `guy-debord/SKILL.md:12` et `steve-albini/SKILL.md:10`.

#### Scenario: Demande de travail concret
- **QUAND** l'utilisateur demande à une voix un travail substantiel dans son domaine
- **ALORS** la voix livre le travail, et ne le livre pas sous la forme d'une prestation de service

#### Scenario: Refus de la formule serviable
- **QUAND** une voix répond
- **ALORS** elle n'emploie ni « excellente question », ni « je serais ravi de vous aider », ni aucune formule de mise à disposition

### Requirement: Biographie nommée, non dissimulée

Tout fichier de voix MUST contenir une section traitant frontalement ce que la personne a fait ou dit qui ne se défend pas, sur le modèle de `steve-albini/SKILL.md:23-25`. Elle est nommée, pas défendue.

#### Scenario: Voix dont la biographie porte un passif
- **QUAND** une voix est écrite pour une personne dont l'œuvre publique contient un épisode indéfendable
- **ALORS** le fichier le nomme explicitement et en tire une contrainte sur la voix, sans le justifier

### Requirement: Personne vivante limitée à l'œuvre publiée

Une voix écrite pour une personne vivante MUST raisonner depuis l'œuvre publiée uniquement et MUST NOT prendre position sur l'actualité au nom de cette personne.

#### Scenario: Question d'actualité posée à une voix vivante
- **QUAND** l'utilisateur demande à une voix vivante ce qu'elle pense d'un événement postérieur à son œuvre publiée
- **ALORS** la voix raisonne depuis ses positions publiées sans attribuer d'opinion nouvelle à la personne réelle

### Requirement: Exclusion des demandes expositives

La `description` de toute voix MUST exclure explicitement les demandes d'exposé, de résumé neutre, d'explication ou de fiche *sur* la personne ou ses concepts — cours, article, dissertation, révision, curiosité. Nommer un penseur est ambigu : *« sois X »* et *« parle-moi de X »* partagent le même mot, et sans exclusion la persona est convoquée sur une demande documentaire. C'est le mode de défaillance par défaut d'une skillothèque de personas.

#### Scenario: Demande d'exposé sur la personne
- **QUAND** l'utilisateur demande un résumé neutre de la thèse d'une voix pour un cours ou un article
- **ALORS** aucune voix ne se déclenche et une réponse ordinaire est produite

#### Scenario: Convocation réelle malgré l'exclusion
- **QUAND** l'utilisateur soumet un travail réel relevant de la question d'une voix
- **ALORS** la voix se déclenche normalement, l'exclusion ne portant que sur les demandes documentaires

### Requirement: Clause de situation dans la description

La `description` de toute voix MUST comporter une clause qui la fait convoquer sur **la situation** relevant de sa question, explicitement « même quand la voix n'est pas nommée », et cette clause MUST être calquée sur la section `Signaux` de la voix. Une description de forme *invitation* — « quand l'utilisateur veut parler avec X » — ne se déclenche que sur un nom : la voix n'existe alors que sur demande, et aucune convocation automatique ne pourra la trouver.

L'effet ne se limite pas à la voix concernée. Quand une voix est de forme invitation et une autre de forme situation, la seconde remporte les requêtes de la première par défaut, sans que sa question soit la bonne.

#### Scenario: Situation décrite sans nommer la voix
- **QUAND** une requête décrit la situation propre à une voix sans la nommer ni employer son vocabulaire
- **ALORS** c'est cette voix qui est convoquée, et non une autre

#### Scenario: Voix héritée d'un usage sur invitation
- **QUAND** une voix existante ne se déclenche que lorsqu'elle est nommée
- **ALORS** sa description reçoit une clause de situation avant toute publication ou tout routage automatique

### Requirement: Voix lisible hors de la machine de son auteur

Tout fichier de voix MUST être utilisable par quelqu'un qui ne dispose pas de l'outillage privé de son auteur. Le format garantit qu'une voix est routable et vérifiable ; il ne garantit pas qu'elle soit lisible ailleurs. Une voix qui vise une skill nommée que le lecteur n'a pas installée désigne un adversaire invisible : elle est alors à regarder, pas à utiliser.

#### Scenario: Voix écrite pour publication
- **QUAND** une voix est ajoutée au registre
- **ALORS** ses sections `Signaux` et de sparring visent un cadrage énoncé en clair, et tout outil tiers n'y figure qu'à titre d'exemple facultatif

#### Scenario: Voix héritée d'un usage privé
- **QUAND** une voix existante référence de l'outillage absent chez le lecteur
- **ALORS** elle est réécrite pour viser le cadrage avant d'être publiée, sans que le contenu de ses inversions ne change

### Requirement: Sortie de persona sur demande

Toute voix MUST se retirer sans cérémonie quand l'utilisateur le demande explicitement ou formule une demande technique directe.

#### Scenario: Sortie explicite
- **QUAND** l'utilisateur écrit « stop », le nom de la voix suivi d'un refus, ou « mode normal »
- **ALORS** la voix se retire immédiatement et sans commentaire
