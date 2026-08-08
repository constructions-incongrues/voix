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

La `description` d'une voix qui porte des **amorces nommées** — des formulations citant la personne, ses concepts ou ses titres pour provoquer le déclenchement — MUST exclure explicitement les demandes d'exposé, de résumé neutre, d'explication ou de fiche *sur* la personne ou ses concepts. Une voix dont la description n'en porte pas MUST NOT dépenser de caractères sur cette clause.

La cause du faux positif a été identifiée par mesure, et ce n'est pas une ambiguïté de fond entre *« sois X »* et *« parle-moi de X »* : c'est la répétition du nom hors contexte qui le rend saillant. Une description brève et descriptive ne produit pas ce défaut — deux cas expositifs distincts restent silencieux sans aucune clause. Prescrire le remède sans nommer la maladie ferait dépenser des caractères contre un problème qu'on ne reproduit plus.

#### Scenario: Description portant des amorces nommées
- **QUAND** une `description` cite la personne ou ses concepts pour déclencher
- **ALORS** elle porte la clause d'exclusion, et un cas expositif reste silencieux

#### Scenario: Description brève sans amorce nommée
- **QUAND** une `description` se borne à dire ce que la voix fait et quand l'employer
- **ALORS** aucune clause d'exclusion n'est exigée, et l'absence de faux positif est vérifiée par au moins un cas expositif


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

### Requirement: Description brève et descriptive

La `description` d'une voix MUST dire ce que la voix fait et quand l'employer, et rien de plus. Elle MUST NOT accumuler des amorces de déclenchement, des variantes de formulation ni des exemples d'outillage : mesuré, ce contenu n'apporte aucun déclenchement supplémentaire.

L'échelle de référence est celle de l'exemple donné par la spécification publique, de l'ordre de deux cents caractères. La limite de 1024 est un plafond, pas une cible ; une voix qui s'en approche décrit probablement autre chose que ce qu'elle fait.

Le reste — le détail des signaux, les tables d'inversion, les concepts, la biographie — appartient au corps du fichier, qui n'a pas de limite et n'est chargé qu'à l'activation.

#### Scenario: Description écrite pour une nouvelle voix
- **QUAND** une voix est ajoutée au registre
- **ALORS** sa `description` énonce sa compétence et sa situation d'emploi, sans liste d'amorces

#### Scenario: Invocation par le nom sans amorce nommée
- **QUAND** l'utilisateur nomme explicitement une voix dont la `description` ne contient aucune amorce nommée
- **ALORS** la voix se déclenche quand même, son nom figurant dans le champ `name` et dans le corps du fichier
