## ADDED Requirements

### Requirement: Le numéro de version est calculé, non posé

Le champ `version` de `.claude-plugin/plugin.json` MUST être écrit par l'outil de publication à partir de l'historique, et MUST NOT être édité à la main dans un commit ordinaire. Une édition manuelle est un contournement de la règle de dérivation, pas un raccourci.

Cette exigence remplace la pratique antérieure, où la version était posée à la main au moment de publier.

#### Scenario: Édition manuelle du champ version
- **QUAND** un commit ordinaire modifie `version` dans `.claude-plugin/plugin.json`
- **ALORS** il ne satisfait pas cette exigence, et le champ doit être laissé à l'outil

#### Scenario: Publication normale
- **QUAND** une demande de publication est fusionnée
- **ALORS** `version` porte le numéro calculé, et le commit qui l'écrit est celui de la publication
