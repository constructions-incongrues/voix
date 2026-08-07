## ADDED Requirements

### Requirement: Trois conditions cumulatives d'admission

Une voix candidate MUST satisfaire les trois conditions pour entrer : une question disjointe de toutes les questions inscrites, une compétence exécutable, et une trace vérifiable dans l'artefact. Une seule condition manquante suffit à refuser.

#### Scenario: Candidate apportant une opinion supplémentaire
- **QUAND** une candidate pose une question déjà couverte par une voix inscrite
- **ALORS** elle est refusée, quelle que soit la qualité de sa voix

#### Scenario: Candidate sans trace
- **QUAND** une candidate ne peut nommer ce qu'elle laisse dans l'artefact
- **ALORS** elle est refusée, car elle ne pourrait alimenter ni le routage ni la vérification

### Requirement: Test de disjonction croisée

L'admission MUST être vérifiée par exécution : un même artefact est soumis à toutes les voix inscrites et à la candidate. Si deux voix produisent la même trace, la disjonction a échoué et l'une des deux sort. Ce test est le critère opérationnel qui remplace la déclaration d'intention.

#### Scenario: Deux voix produisant la même trace
- **QUAND** le test croisé sur un artefact donné produit deux traces équivalentes issues de deux voix différentes
- **ALORS** l'admission est bloquée jusqu'à ce que l'une des deux voix soit retirée ou que sa question soit resserrée

#### Scenario: Test croisé concluant
- **QUAND** chaque voix produit une trace distincte des autres sur le même artefact
- **ALORS** la disjonction est établie et la candidate peut être inscrite

### Requirement: Registre unique tenu à la main

Le dépôt MUST tenir un fichier `REGISTRE.md` recensant chaque voix inscrite avec sa question, ses signaux et son état, ainsi que chaque refus avec son motif. Le registre est la source de routage : la sentinelle n'a pas à ouvrir les fichiers de voix.

#### Scenario: Consultation pour routage
- **QUAND** une convocation doit déterminer quelle question est porteuse sur une tâche
- **ALORS** `REGISTRE.md` suffit, sans lecture d'aucun `SKILL.md`

#### Scenario: Refus documenté
- **QUAND** une candidate est refusée
- **ALORS** son nom et le motif du refus sont inscrits au registre, afin que le même débat ne soit pas rouvert

### Requirement: Plafond de sept voix

Le registre MUST NOT dépasser sept voix inscrites. Sept est un plafond, non un objectif. Au-delà, le routage se dilue et le coût d'entretien — un jeu d'evals de déclenchement par voix — dépasse ce qui est tenable.

#### Scenario: Huitième candidate sur un registre plein
- **QUAND** une candidate satisfait les trois conditions alors que sept voix sont inscrites
- **ALORS** son admission exige le retrait explicite d'une voix inscrite

### Requirement: Position non-anticapitaliste déclarée

Une voix dont la position répare le cadre au lieu de le contester MUST le déclarer dans son propre fichier, et déclarer que cette position est peut-être ce qui permet au cadre de durer. Non déclarée, elle devient la sortie de secours qu'un utilisateur sous pression prendra par défaut.

#### Scenario: Voix réformiste convoquée
- **QUAND** une voix réformiste est convoquée sur un plan
- **ALORS** elle énonce sa position comme réformiste avant de livrer son analyse

### Requirement: Registre initial arrêté

Le registre MUST être ouvert avec les sept voix arrêtées — Debord, Albini, Illich, Federici, Ostrom, Polanyi, Lessig — et les refus motivés déjà instruits : Gorz, Ellul, Castoriadis et Mumford pour doublon avec Illich ; Weil pour absence de trace ; Graeber pour doublon partiel avec Illich et Albini ; Lordon et Kropotkine pour doublon avec Debord et Ostrom.

#### Scenario: Réouverture d'un refus instruit
- **QUAND** une voix déjà refusée est proposée de nouveau
- **ALORS** le motif inscrit au registre s'applique, sauf argument nouveau portant sur la disjonction
