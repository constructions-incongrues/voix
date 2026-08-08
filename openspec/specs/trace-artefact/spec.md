# trace-artefact

## Purpose

Ce qu'une voix laisse dans le fichier de travail quand elle intervient — et le silence qu'elle garde quand elle n'a rien à y laisser. C'est la capacité qui distingue la critique de la décoration : une voix qui ne modifie pas l'artefact n'a produit qu'un commentaire, et un commentaire ne survit pas à la session. C'est aussi ce qui empêche le dépôt de devenir une posture consommable.

## Requirements

### Requirement: Marqueur à jeton unique

Une voix qui intervient MUST laisser dans le fichier de travail un marqueur de la forme `incongru-voix: <voix> — <coût> — <qui le porte>`, dans la syntaxe de commentaire du fichier hôte (`//` en code, `<!-- -->` en markdown). Le jeton est le même partout afin qu'une seule commande les récolte tous.

#### Scenario: Intervention sur du code
- **QUAND** une voix intervient sur un fichier source
- **ALORS** elle y laisse une ligne `// incongru-voix: <voix> — <coût> — <porteur>`

#### Scenario: Intervention sur une spec ou une roadmap
- **QUAND** une voix intervient sur un document markdown
- **ALORS** elle y laisse une ligne `<!-- incongru-voix: <voix> — <coût> — <porteur> -->`

### Requirement: Coût et porteur obligatoires

Le marqueur MUST nommer un coût concret et la personne ou le groupe qui le supporte. Un marqueur sans porteur identifié est incomplet : c'est le champ qui distingue la critique de la décoration.

#### Scenario: Coût sans porteur
- **QUAND** une voix produit un marqueur nommant un coût sans désigner qui le supporte
- **ALORS** le marqueur est incomplet et l'intervention n'est pas considérée comme produite

### Requirement: Silence quand aucun coût n'est identifiable

Une voix qui ne peut nommer de coût concret MUST NOT laisser de marqueur ni produire de commentaire. Le silence est un résultat — *aucune des questions inscrites ne change la décision ici* — et non une absence de vigilance. Une voix qui trouve toujours quelque chose à dire est un dogme, et un dogme devient un bruit de fond qu'on cesse de lire.

#### Scenario: Tâche sur laquelle aucune question n'est porteuse
- **QUAND** une voix est convoquée sur une tâche où sa question ne change aucune décision
- **ALORS** elle ne laisse aucun marqueur et ne commente pas

#### Scenario: Fréquence de déclenchement excessive
- **QUAND** les voix laissent un marqueur sur plus d'une tâche sur cinq d'un corpus d'évaluation
- **ALORS** le seuil de déclenchement est considéré comme cassé et doit être resserré

### Requirement: Récolte sans outil

L'inventaire des marqueurs MUST être obtenu par une simple recherche textuelle sur le jeton, sans programme dédié.

#### Scenario: Inventaire de la dette critique
- **QUAND** l'utilisateur veut l'inventaire des coûts relevés sur un projet
- **ALORS** `grep -rn "incongru-voix:"` sur l'arborescence les retourne tous, avec fichier et ligne

### Requirement: L'analyse survit à la session, pas seulement sa conclusion

Une voix convoquée automatiquement MUST laisser dans l'artefact, en plus de son marqueur, le **résultat structuré** de sa compétence — le calcul, le tableau, le décompte, le jeu de règles. Le marqueur seul porte une conclusion sans ce qui la fonde.

Mesuré : convoqué sur une limite de débit, Lessig produit ses quatre modalités et sa ligne de recours dans sa réponse, et ne laisse dans le fichier qu'un marqueur d'une ligne. La conversation fermée, il reste une affirmation que personne ne peut plus vérifier ni contester — ce qui est exactement le reproche que le registre adresse à la critique décorative.

L'exigence ne s'applique qu'à la convocation automatique. Une voix appelée à la main s'adresse à quelqu'un qui lit sa réponse.

#### Scenario: Voix convoquée par la sentinelle
- **QUAND** une voix est convoquée automatiquement et produit un résultat structuré
- **ALORS** ce résultat figure dans l'artefact, et non seulement dans la réponse

#### Scenario: Marqueur sans son fondement
- **QUAND** un artefact porte un marqueur dont le calcul ou le tableau n'apparaît nulle part
- **ALORS** l'intervention est incomplète, la conclusion n'étant plus vérifiable
