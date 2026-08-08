## ADDED Requirements

### Requirement: Ce qui déclenche la règle est ce que l'outil prescrit, non l'endroit où il se pose

L'admission d'un outil MUST être décidée selon **ce qu'il prescrit sur la façon de travailler**, et MUST NOT dépendre du répertoire où ses fichiers atterrissent. La règle antérieure de `REGISTRE.md` nommait `.agents/skills/` ; elle est ainsi passée à côté d'un outil qui s'installe à la racine du dépôt.

Un outil MUST être soumis à cette capacité dès lors qu'il pose, dans l'arbre de travail, des fichiers qui décrivent un ordre de travail, un vocabulaire imposé, des gabarits de production ou des phases — quel que soit leur emplacement, et qu'ils soient suivis par git ou non.

#### Scenario: Outil posé hors du répertoire nommé par la règle antérieure
- **QUAND** un outil crée `.nanopm/` à la racine du dépôt, contenant un schéma de méthode produit
- **ALORS** il est soumis à cette capacité, l'emplacement étant sans effet

#### Scenario: Outil sans prescription
- **QUAND** un outil ajoute une commande de formatage sans imposer d'ordre de travail
- **ALORS** cette capacité ne s'applique pas — il n'y a rien à décider

#### Scenario: Règle invoquée sur un chemin
- **QUAND** quelqu'un justifie l'admission d'un outil par le fait que ses fichiers ne sont pas dans `.agents/skills/`
- **ALORS** cet argument ne satisfait pas cette exigence

### Requirement: Une capacité apportée n'est pas une méthode prescrite

L'admission MUST distinguer deux catégories, et le motif écrit MUST dire laquelle s'applique :

- **Capacité apportée** — l'outil rend possible quelque chose que le dépôt voulait déjà faire, sans dire comment travailler. Admissible.
- **Méthode prescrite** — l'outil impose un ordre, des phases, des artefacts obligatoires ou un vocabulaire. Admissible **seulement** par décision explicite, car adopter la méthode est le vrai objet du choix.

Le doute MUST être tranché en faveur de la seconde catégorie : un outil qu'on ne sait pas classer prescrit probablement quelque chose qu'on n'a pas regardé.

#### Scenario: Capacité apportée
- **QUAND** une skill fournit des gabarits d'ADR pour un artefact que le schéma réclame déjà
- **ALORS** elle est classée capacité apportée, et son admission ne demande pas d'ADR

#### Scenario: Méthode prescrite
- **QUAND** une skill pose que tout changement d'état doit passer par `main` avant que la phase suivante n'en dépende
- **ALORS** elle est classée méthode prescrite, et n'entre que par décision

#### Scenario: Classement douteux
- **QUAND** un outil paraît n'apporter qu'une capacité mais installe des gabarits, des sections et un ordre de phases
- **ALORS** il est classé méthode prescrite

### Requirement: Un outil entre par décision tracée, et l'indécision n'est pas un état

Un outil relevant de la catégorie « méthode prescrite » MUST faire l'objet d'un ADR avant d'être commité au dépôt. La ligne correspondante du tableau d'outillage de `REGISTRE.md` MUST être écrite dans le même changement.

Laisser les fichiers d'un tel outil **non commités et non tranchés** MUST être traité comme un défaut et non comme une position d'attente : c'est la voie du défaut, celle-là même par laquelle une skill est entrée sans que personne ne la choisisse.

#### Scenario: Outil admis
- **QUAND** un outil de méthode est retenu
- **ALORS** un ADR consigne la décision, ses options écartées et son coût
- **ET** le tableau de `REGISTRE.md` gagne sa ligne dans le même changement

#### Scenario: Fichiers laissés en suspens
- **QUAND** les fichiers d'un outil de méthode restent non commités et non tranchés d'une session à l'autre
- **ALORS** cette exigence n'est pas satisfaite

#### Scenario: Outil commité avant décision
- **QUAND** un outil de méthode est commité sans ADR
- **ALORS** cette exigence n'est pas satisfaite, quel que soit son intérêt

### Requirement: Un refus se consigne comme une admission

Le refus d'un outil MUST être inscrit au tableau d'outillage avec son motif, au même titre qu'une admission. Un outil retiré ou écarté sans trace MUST être considéré comme non traité : rien n'empêche alors qu'il revienne par la même porte.

Le motif MUST nommer ce que l'outil prescrivait, et non seulement qu'il a été écarté.

#### Scenario: Refus motivé
- **QUAND** un outil est écarté
- **ALORS** le tableau porte son nom, son statut et ce qu'il prescrivait

#### Scenario: Suppression silencieuse
- **QUAND** les fichiers d'un outil sont supprimés sans que le tableau ne le mentionne
- **ALORS** cette exigence n'est pas satisfaite — le dépôt a oublié une décision qu'il avait prise

#### Scenario: Motif sans contenu
- **QUAND** le tableau porte « retirée — non retenue »
- **ALORS** cette exigence n'est pas satisfaite : le motif ne nomme pas la prescription

### Requirement: Ce que la sentinelle examine est déclaré là où le dépôt déclare son outillage régénérable

Les chemins que la sentinelle exclut de son examen MUST être déclarés au `.gitignore`, sous la catégorie que le dépôt y tient déjà — *outillage régénérable, non couvert par la licence du dépôt* — et chaque entrée MUST porter son motif. Le hook les obtient sans code d'exclusion : `git ls-files --others --exclude-standard` applique `.gitignore`.

Aucune liste d'exclusion MUST être écrite en dur dans le hook. Une exclusion codée en dur est une décision de routage qui n'apparaît nulle part où les décisions se lisent, et qui diverge de `.gitignore` au premier oubli.

Une exclusion MUST viser une catégorie — l'état d'un outil installé — et MUST NOT être ajoutée cas par cas au fil des collisions.

#### Scenario: Exclusion déclarée
- **QUAND** un répertoire d'état d'outil doit cesser de déclencher des convocations
- **ALORS** il est inscrit au `.gitignore` sous la catégorie existante, avec son motif
- **ET** aucune ligne n'est ajoutée au hook

#### Scenario: Exclusion en dur devenue redondante
- **QUAND** le hook saute un chemin que `.gitignore` couvre déjà
- **ALORS** cette ligne est du code mort et MUST être supprimée — la garder laisserait croire que le hook tient sa propre liste

#### Scenario: Exclusion en dur
- **QUAND** un chemin est ajouté à une liste d'exclusion dans le code du hook
- **ALORS** cette exigence n'est pas satisfaite

#### Scenario: Fichier neuf appartenant au travail
- **QUAND** un fichier non suivi vient d'être écrit par l'auteur dans le cadre du travail en cours
- **ALORS** il reste examiné — l'exclusion vise l'état des outils, non les fichiers neufs

### Requirement: Le coût de routage d'un outil est mesuré avant sa décision

L'ADR d'admission MUST porter la part des convocations de la sentinelle déclenchées par les fichiers de l'outil, mesurée sur le journal. Un outil qui capte le routage prive le travail réel des voix, et ce coût MUST être chiffré plutôt que supposé.

#### Scenario: Mesure au dossier
- **QUAND** un outil de méthode est soumis à décision
- **ALORS** l'ADR porte le nombre de convocations qu'il a déclenchées et leur part du total sur la période observée

#### Scenario: Décision sans mesure
- **QUAND** l'ADR ne porte aucun chiffre de routage alors que le journal en contient
- **ALORS** cette exigence n'est pas satisfaite
