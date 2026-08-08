# paquet-plugin

## Purpose

Ce que le dépôt doit satisfaire pour être chargé comme plugin — et la ligne qui sépare un manifeste auto-hébergé, où personne ne s'intercale, d'une inscription dans un index tiers, où la critique est agrégée, classée et recommandée. Le format plugin n'est pas une vitrine : c'est le seul véhicule qui transporte des hooks, et la sentinelle est un hook.

## Requirements

### Requirement: Skills à l'emplacement attendu du chargeur

Les voix MUST se trouver dans `skills/<nom>/SKILL.md` à la racine du dépôt. C'est l'emplacement où un chargeur de plugins les cherche ; ailleurs, elles ne sont pas chargées. Le dépôt MUST NOT maintenir une seconde copie des voix à un autre emplacement : deux exemplaires du même fichier divergent.

#### Scenario: Plugin chargé
- **QUAND** le dépôt est installé comme plugin
- **ALORS** chaque voix du registre apparaît dans les skills disponibles

#### Scenario: Emplacement unique
- **QUAND** on cherche le fichier d'une voix
- **ALORS** il existe à un seul emplacement dans le dépôt

### Requirement: Le manifeste ne déclare jamais `hooks/hooks.json`

`plugin.json` MUST NOT déclarer de clé `hooks` pointant vers `./hooks/hooks.json`. Ce fichier est **chargé automatiquement** par convention ; le déclarer produit un doublon qui fait échouer le chargement de **tous** les hooks du plugin, avec le message *« Duplicate hooks file detected »*.

La clé `hooks` ne sert qu'à référencer des fichiers de hooks **supplémentaires**, portant un autre nom. Un plugin tiers qui la déclare le fait avec un nom non standard ; recopier son manifeste en gardant le nom standard produit exactement cette collision.

Elle MUST NOT non plus référencer un fichier absent : une référence morte empêche le chargement du plugin entier.

#### Scenario: Hook au nom standard
- **QUAND** le dépôt porte ses hooks dans `hooks/hooks.json`
- **ALORS** `plugin.json` ne comporte aucune clé `hooks`, et le fichier est chargé

#### Scenario: Manifeste sans hook
- **QUAND** le dépôt ne contient aucun hook
- **ALORS** `plugin.json` ne comporte pas de clé `hooks`, et le plugin se charge

### Requirement: Manifeste auto-hébergé

`marketplace.json` MUST déclarer le dépôt lui-même comme source (`"source": "./"`). L'utilisateur désigne le dépôt et l'installe ; aucun intermédiaire ne s'intercale entre celui qui écrit les voix et celui qui les emploie.

#### Scenario: Installation en direct
- **QUAND** un utilisateur veut installer les voix comme plugin
- **ALORS** il ajoute ce dépôt comme place de marché et installe depuis lui, sans passer par un index tiers

### Requirement: Refus motivé de l'inscription dans un index tiers

Le dépôt MUST NOT être inscrit dans un index de plugins agrégé par un tiers, et ce refus MUST être écrit et motivé dans le `README.md`. Un index agrège, classe et recommande : il place la critique dans une liste où elle est comparée, notée et adoptée par commodité. C'est là qu'opère la récupération, et non dans le fait d'être installable.

Cette position est révisable, mais elle MUST alors l'être par une décision explicite, jamais par commodité d'installation.

#### Scenario: Lecteur cherchant pourquoi le plugin est introuvable ailleurs
- **QUAND** quelqu'un cherche le plugin dans un index de plugins
- **ALORS** il ne l'y trouve pas, et le README du dépôt explique ce choix et sa raison

### Requirement: Second chemin d'installation préservé

Le dépôt MUST rester installable par clone et liens symboliques, sans passer par le format plugin. Les voix sont des fichiers markdown : elles servent à tout agent qui charge des skills, et le format plugin n'est propre qu'à l'un d'eux.

#### Scenario: Agent sans support des plugins
- **QUAND** un utilisateur emploie un agent qui charge des skills mais ignore les plugins
- **ALORS** `install.sh` installe les voix et elles fonctionnent

### Requirement: Réparation des liens devenus morts

`install.sh` MUST retirer les liens qu'il a lui-même posés et qui pointent désormais vers un chemin inexistant de ce dépôt, avant d'en poser de nouveaux. Un lien mort ne produit aucune erreur : la voix cesse simplement d'exister, et la panne est indiagnosticable.

Le garde-fou existant MUST être conservé : un vrai dossier n'est jamais écrasé, seulement signalé.

#### Scenario: Installation antérieure à un renommage
- **QUAND** `install.sh` est relancé après un changement d'arborescence du dépôt
- **ALORS** les liens devenus morts sont retirés et remplacés, sans intervention manuelle

#### Scenario: Vrai dossier présent
- **QUAND** un vrai dossier occupe l'emplacement d'une voix
- **ALORS** `install.sh` le signale et ne le touche pas

### Requirement: Version signifiante

Le dépôt MUST porter une version, et le `README.md` MUST dire ce qu'elle compte : une voix qui entre ou sort du registre pour la majeure, un changement de question, de compétence ou de trace pour la mineure, un ajustement de déclencheur ou de formulation pour la corrective. Une version qui ne compte rien n'informe personne.

#### Scenario: Voix retirée du registre
- **QUAND** une voix sort du registre après un échec au test de disjonction
- **ALORS** la version majeure est incrémentée
