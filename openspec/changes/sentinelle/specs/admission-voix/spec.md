## MODIFIED Requirements

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
