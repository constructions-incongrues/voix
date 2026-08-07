## ADDED Requirements

### Requirement: Marqueur à jeton unique

Une voix qui intervient MUST laisser dans le fichier de travail un marqueur de la forme `skillotheque: <voix> — <coût> — <qui le porte>`, dans la syntaxe de commentaire du fichier hôte (`//` en code, `<!-- -->` en markdown). Le jeton est le même partout afin qu'une seule commande les récolte tous.

#### Scenario: Intervention sur du code
- **QUAND** une voix intervient sur un fichier source
- **ALORS** elle y laisse une ligne `// skillotheque: <voix> — <coût> — <porteur>`

#### Scenario: Intervention sur une spec ou une roadmap
- **QUAND** une voix intervient sur un document markdown
- **ALORS** elle y laisse une ligne `<!-- skillotheque: <voix> — <coût> — <porteur> -->`

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
- **ALORS** `grep -rn "skillotheque:"` sur l'arborescence les retourne tous, avec fichier et ligne
