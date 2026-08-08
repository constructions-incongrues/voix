## ADDED Requirements

### Requirement: Forme du message

Tout commit créé après l'adoption MUST porter un sujet de la forme `type(scope): description`, conforme à Conventional Commits 1.0.0. Le `type` et le `scope` MUST être en anglais et pris dans les jeux fermés définis plus bas ; la `description` MUST être en français. Le scope est facultatif ; le type ne l'est pas.

#### Scenario: Sujet conforme
- **WHEN** un commit corrige le chemin par défaut du journal de la sentinelle
- **THEN** son sujet est `fix(sentinelle): le journal survit à la session et ne plante plus le hook`

#### Scenario: Sujet sans type
- **WHEN** un commit porte le sujet `Le registre devient exécutable`
- **THEN** il ne satisfait pas cette exigence, et son sujet doit être réécrit avant d'être poussé

#### Scenario: Historique antérieur
- **WHEN** on inspecte un commit antérieur à l'adoption
- **THEN** cette exigence ne s'y applique pas, et le message n'est pas réécrit

### Requirement: La description reste une phrase qui porte un constat

La `description` MUST rester une phrase française énonçant ce que le commit établit, et MUST NOT être réduite à une étiquette de catégorie. Le type contraint le préfixe ; il n'a aucune autorité sur ce que la phrase dit. Un commit qui corrige une croyance antérieure MUST énoncer la croyance corrigée dans sa description ou son corps.

#### Scenario: Correction d'une croyance antérieure
- **WHEN** on découvre que le plugin installé était resté en 0.1.0 pendant une campagne de mesures
- **THEN** le sujet est `docs(mesure): le plugin installé était resté en 0.1.0 pendant les mesures`
- **AND** il n'est pas réduit à `docs: mise à jour des mesures`

#### Scenario: Description réduite à une étiquette
- **WHEN** un commit porte le sujet `fix(sentinelle): correction de bug`
- **THEN** il ne satisfait pas cette exigence — la phrase n'énonce aucun constat

### Requirement: Correspondance avec les niveaux de version

Le niveau de version d'une publication MUST être dérivé des types des commits qu'elle contient, selon la table ci-dessous. **Les types font autorité** : la table décrit la configuration de l'outil de publication, et le § Versions du `README.md` en donne le motif sans l'emporter sur elle.

Cette exigence a d'abord posé l'inverse — le README souverain, les types indicatifs. `adr/0002` a remplacé ce garde-fou en rendant les types décisifs, parce qu'une règle écrite et un outil qui disent deux choses différentes finissent par diverger sans que rien ne le signale. En cas de désaccord entre la table et la configuration exécutée, **c'est la configuration qui fait foi** et la table MUST être corrigée dans le même commit.

| Niveau | Règle du dépôt | Type |
|---|---|---|
| **majeure** | une voix entre au registre, ou en sort | `feat!` ou pied de page `BREAKING CHANGE:` |
| **mineure** | une voix change de question, de compétence ou de trace · un changement dans ce que le dépôt *fait* · une conformité à une norme externe | `feat` |
| **corrective** | un déclencheur ajusté, un test rejoué, une formulation corrigée | `fix`, `docs`, `test`, `refactor`, `chore` |

#### Scenario: Admission d'une voix
- **WHEN** Federici entre au registre
- **THEN** le commit porte `feat!(registre):` ou un pied de page `BREAKING CHANGE:`
- **AND** la publication qui le contient est majeure

#### Scenario: Changement du dispositif
- **WHEN** la sentinelle gagne une mise en sourdine, sans qu'aucune voix ne change
- **THEN** le commit porte `feat(sentinelle):` et la publication est mineure

#### Scenario: Désaccord entre la table et la configuration
- **WHEN** la table du README classe un type en corrective alors que `release-please-config.json` le rend mineur
- **THEN** la configuration fait foi, et la table est corrigée par un commit `docs(registre):`

#### Scenario: Numéro calculé jugé faux
- **WHEN** le numéro proposé par l'outil paraît contredire la règle du § Versions
- **THEN** le commit fautif est corrigé, jamais le numéro dans la demande de publication

### Requirement: Jeux fermés de types et de scopes

Les types admis MUST être : `feat`, `fix`, `docs`, `refactor`, `test`, `chore`. Les scopes admis MUST être : `voix`, `sentinelle`, `registre`, `plugin`, `specs`, `mesure`. Ajouter un type ou un scope MUST faire l'objet d'un commit `docs(specs):` modifiant cette exigence — jamais d'un usage de fait.

#### Scenario: Scope hors jeu
- **WHEN** un commit porte `feat(ui): …`
- **THEN** il ne satisfait pas cette exigence — `ui` n'est pas au jeu, et le dépôt n'a aucune interface

#### Scenario: Élargissement du jeu
- **WHEN** un septième scope devient nécessaire
- **THEN** il entre par un commit modifiant cette exigence, avant tout usage

### Requirement: L'historique antérieur n'est pas réécrit

Les commits antérieurs à l'adoption MUST NOT être réécrits pour se conformer. Le dépôt tient la même règle pour ses archives : *« les réécrire pour qu'ils aient l'air à jour serait falsifier un dossier »*. Tout outil de dérivation MUST donc traiter un sujet sans type comme *antérieur*, non comme *invalide*.

#### Scenario: Dérivation sur un historique mixte
- **WHEN** un outil parcourt l'historique complet pour dériver un niveau de version
- **THEN** les sujets sans type sont ignorés plutôt que signalés en erreur
