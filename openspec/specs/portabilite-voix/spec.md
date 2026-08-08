# portabilite-voix

## Purpose

Ce qu'il faut à une voix pour être utilisable par quelqu'un d'autre que son auteur. Une voix mise au point sur une machine finit par viser l'outillage de cette machine ; publiée telle quelle, elle désigne un adversaire que le lecteur n'a pas installé et devient une chose à regarder plutôt qu'à employer.

## Requirements

### Requirement: Cible généralisée, inversion inchangée

Une table d'inversion MUST viser un **cadrage** — la formule et la posture qu'elle attaque — et non une skill nommée. Le contenu de l'inversion MUST rester inchangé : c'est sa précision qui fait sa force. Seul change ce qui prononce la formule.

#### Scenario: Sparring lu sans l'outillage de l'auteur
- **QUAND** un lecteur qui n'a installé aucun outillage tiers lit la section de sparring d'une voix
- **ALORS** il comprend quelle posture est attaquée et peut s'en servir, sans avoir à identifier un outil qu'il ne possède pas

#### Scenario: Formule attaquée mot pour mot
- **QUAND** une table d'inversion traite une formule comme « fais quelque chose que les gens veulent »
- **ALORS** l'entrée correspondante conserve son argument intégral, la généralisation ne portant que sur l'émetteur de la formule

### Requirement: Outillage tiers cité en exemple, jamais en dépendance

Toute mention d'un outil, d'une skill ou d'un produit tiers dans un fichier de voix MUST être formulée comme un exemple facultatif. Une voix MUST NOT exiger la présence d'un outil tiers pour être utilisable.

#### Scenario: Voix utilisée sans l'outil cité
- **QUAND** une voix est convoquée sur une machine où l'outillage qu'elle cite n'existe pas
- **ALORS** elle produit son analyse et sa trace normalement, sans référence non résolue

### Requirement: Extension additive des déclencheurs

Une réécriture de portabilité MUST étendre la `description` d'une voix sans en retirer d'amorce de déclenchement existante. Les déclencheurs sont des artefacts réglés par itérations successives ; une suppression détruit un travail coûteux à retrouver, alors qu'un ajout ne peut pas faire cesser un déclenchement qui fonctionnait.

#### Scenario: Réécriture d'une description réglée
- **QUAND** la `description` d'une voix est modifiée pour la portabilité
- **ALORS** toutes les amorces présentes avant la modification y figurent encore

### Requirement: Renvois internes vérifiés après renommage

Une réécriture qui renomme une section MUST vérifier que les renvois internes du fichier pointent encore vers une section existante. La section `Compétence` désigne l'instrument de travail de la voix par son titre ; un renvoi cassé prive la voix de son outil.

#### Scenario: Section renommée
- **QUAND** un titre de section est modifié
- **ALORS** tout renvoi de la forme « la section **X** » résout vers un titre présent dans le fichier

### Requirement: Non-régression prouvée avant publication

Une réécriture de portabilité MUST être suivie d'un rejeu du test de disjonction et du test de silence, avec des résultats datés de cette exécution. Une régression MUST bloquer la publication.

#### Scenario: Rejeu concluant
- **QUAND** les voix ont été réécrites et les deux tests rejoués sans régression
- **ALORS** la publication peut se poursuivre

#### Scenario: Rejeu en échec
- **QUAND** un contrôle positif cesse de déclencher, ou qu'un cas ordinaire se met à déclencher
- **ALORS** la publication est bloquée jusqu'à correction et nouveau rejeu

#### Scenario: Échec antérieur à la réécriture
- **QUAND** un contrôle positif échoue et qu'il n'avait jamais été éprouvé auparavant
- **ALORS** l'échec est vérifié contre la version antérieure avant d'être qualifié de régression, et corrigé dans tous les cas
