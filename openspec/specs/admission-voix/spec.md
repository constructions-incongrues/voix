# admission-voix

## Purpose

La règle qui décide qu'une voix candidate entre au registre ou en est écartée, et le test qui rend cette règle exécutable plutôt que déclarative. Elle existe pour empêcher la skillothèque de devenir une friperie : un dépôt où chaque nouvelle voix ajoute une opinion de plus sur une question déjà posée n'a plus rien à router et ne se maintient plus.

## Requirements

### Requirement: Trois conditions cumulatives d'admission

Une voix candidate MUST satisfaire **quatre** conditions cumulatives pour entrer : une question disjointe de toutes les questions inscrites, une compétence exécutable, une trace vérifiable dans l'artefact, et **un apport mesuré contre le défaut**. Une seule condition manquante suffit à refuser.

La quatrième a été établie en dernier alors qu'elle aurait dû être la première. Elle se mesure par le protocole d'apport — un artefact réel, deux bras, la même consigne mot pour mot, la seule différence étant l'emploi de la voix. Une voix dont le modèle sans elle produit déjà le travail n'entre pas, et si elle est déjà inscrite, elle **MUST NOT être convoquée automatiquement** : elle coûterait un tour à l'utilisateur pour un apport nul, et c'est ainsi qu'un dispositif se fait éteindre.

#### Scenario: Candidate apportant une opinion supplémentaire
- **QUAND** une candidate pose une question déjà couverte par une voix inscrite
- **ALORS** elle est refusée, quelle que soit la qualité de sa voix

#### Scenario: Candidate sans trace
- **QUAND** une candidate ne peut nommer ce qu'elle laisse dans l'artefact
- **ALORS** elle est refusée, car elle ne pourrait alimenter ni le routage ni la vérification

#### Scenario: Candidate dont le défaut fait déjà le travail
- **QUAND** le bras sans voix produit déjà l'analyse que la candidate propose
- **ALORS** elle est refusée, son apport n'étant pas établi

#### Scenario: Voix inscrite dont l'apport n'est pas mesuré
- **QUAND** une voix déjà au registre n'a pas passé le protocole d'apport
- **ALORS** elle reste convocable à la main et n'est pas routée automatiquement


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

### Requirement: Mesure du déclenchement indépendante du harnais

Le taux de déclenchement d'une voix MUST être mesuré par observation directe du premier appel de l'outil `Skill`, et non par le score agrégé d'un harnais d'évaluation externe. Le harnais `skill-creator` installe une copie temporaire nommée `<voix>-skill-<hash>` et vérifie que le nom appelé contient ce hash : il suppose que la voix testée n'est pas déjà installée. Quand elle l'est, le modèle appelle la vraie voix, et tout déclenchement réussi est compté comme un échec — un score qui ressemble à une demi-réussite alors que rien n'a été mesuré.

#### Scenario: Score de harnais avec voix installée
- **QUAND** un harnais rapporte un taux de déclenchement nul sur des requêtes positives évidentes
- **ALORS** le résultat est traité comme invalide et la mesure est refaite après décrochage des voix installées, ou par observation directe

### Requirement: La convocation réelle fait foi, pas l'introspection

Une observation sur le comportement des voix MUST reposer sur une **convocation réelle** — l'appel d'outil effectivement émis — et NON sur une réponse du modèle décrivant ce qu'il croit avoir à disposition. Interroger le modèle sur ses propres skills disponibles produit une réponse plausible et incomplète : il sous-déclare, sans le signaler.

C'est le second mode de mesure trompeur rencontré, après le harnais d'évaluation externe. Les deux partagent la même faiblesse : ils rapportent quelque chose qui ressemble à une mesure. Une conclusion tirée d'une seule introspection a été publiée puis démentie par une convocation unique.

#### Scenario: Question sur ce qui est chargé
- **QUAND** il faut établir quelles voix sont disponibles ou laquelle répond
- **ALORS** la constatation se fait sur l'appel d'outil observé, et une réponse déclarative du modèle ne suffit pas à conclure

## Notes

Le seuil de silence et la trace laissée dans l'artefact relèvent de `trace-artefact`. Le contrat de forme d'un fichier de voix relève de `format-voix`.
