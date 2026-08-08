## ADDED Requirements

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

## MODIFIED Requirements

### Requirement: Exclusion des demandes expositives

La `description` d'une voix qui porte des **amorces nommées** — des formulations citant la personne, ses concepts ou ses titres pour provoquer le déclenchement — MUST exclure explicitement les demandes d'exposé, de résumé neutre, d'explication ou de fiche *sur* la personne ou ses concepts. Une voix dont la description n'en porte pas MUST NOT dépenser de caractères sur cette clause.

La cause du faux positif a été identifiée par mesure, et ce n'est pas une ambiguïté de fond entre *« sois X »* et *« parle-moi de X »* : c'est la répétition du nom hors contexte qui le rend saillant. Une description brève et descriptive ne produit pas ce défaut — deux cas expositifs distincts restent silencieux sans aucune clause. Prescrire le remède sans nommer la maladie ferait dépenser des caractères contre un problème qu'on ne reproduit plus.

#### Scenario: Description portant des amorces nommées
- **QUAND** une `description` cite la personne ou ses concepts pour déclencher
- **ALORS** elle porte la clause d'exclusion, et un cas expositif reste silencieux

#### Scenario: Description brève sans amorce nommée
- **QUAND** une `description` se borne à dire ce que la voix fait et quand l'employer
- **ALORS** aucune clause d'exclusion n'est exigée, et l'absence de faux positif est vérifiée par au moins un cas expositif
