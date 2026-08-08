---
status: "accepted"
date: 2026-08-08
decision-makers: Tristan Rivoallan
consulted: —
informed: —
---

# Adopter Conventional Commits, sans laisser la convention aplatir les messages

## Context and Problem Statement

Les 41 commits du dépôt sont des phrases françaises descriptives : **0 porte un préfixe de type**, le sujet fait 56 caractères en moyenne. Ces messages portent un argument plutôt qu'une catégorie — *« Contrat du hook Stop vérifié, pas supposé »*, *« Correction : les deux chemins d'installation se cumulent, ils ne s'éclipsent pas »*. Six d'entre eux, soit 15 %, enregistrent la **correction d'une croyance antérieure**.

Cet historique est lisible par un humain et opaque à une machine : aucun niveau de version ne s'en dérive, aucun changelog ne s'en génère, aucun filtre ne s'y applique. Le dépôt versionne pourtant selon trois règles écrites au README, appliquées à la main à chaque publication.

Deux contraintes propres au dépôt pèsent sur le choix. D'abord, **l'axe de version n'est pas le code, c'est le registre des voix** — majeure quand une voix entre ou sort, mineure quand une voix change de question, corrective quand un déclencheur est ajusté. Ensuite, `REGISTRE.md` exige qu'une prescription de méthode entre **par décision**, jamais par effet de bord : la skill `openspec-git-discipline` a été retirée pour ce motif exact.

## Decision Drivers

- Rendre le niveau de version dérivable par une machine, sans déplacer l'autorité hors du README.
- Ne rien retirer à ce que les messages savent déjà dire, en particulier la correction d'une croyance.
- N'ajouter aucune dépendance : le dépôt n'en a aucune et cette contrainte est structurante.
- Faire entrer la convention par une décision tracée, conformément à la règle du dépôt sur l'outillage.
- Ne pas falsifier l'historique existant.

## Considered Options

1. **Conventional Commits 1.0.0, tel quel**
2. **Une convention adaptée au domaine** — des types calqués sur les trois niveaux de version du dépôt
3. **Garder les phrases, ajouter un pied de page machine** — `Registre: mineure` quand la version bouge
4. **Refus argumenté** — écrire la décision de ne pas adopter, comme les 8 refus du registre et les 3 licences écartées

## Decision Outcome

Chosen option: **« Conventional Commits 1.0.0, tel quel »**, parce que c'est la seule option qui produit un historique lisible par un outil que le dépôt n'a pas écrit — et que sa faiblesse principale, l'aplatissement des messages, se corrige par une exigence explicite plutôt qu'en renonçant au standard.

L'adoption est assortie de quatre garde-fous, spécifiés dans la capacité `convention-commits` :

1. **La description reste une phrase qui porte un constat.** La spécification contraint le préfixe, jamais la phrase. `fix(sentinelle): correction de bug` est non conforme au dépôt bien que conforme au standard.
2. **Le README reste souverain.** Une table relie les types aux trois niveaux ; en cas de conflit, la règle écrite l'emporte et la table est corrigée.
3. **Jeux fermés** — six types, six scopes, élargis par modification de la spec et jamais par usage de fait.
4. **Aucune réécriture de l'historique.** Un sujet sans type est *antérieur*, pas *invalide*.

### Consequences

- Bon, parce que le niveau de version devient dérivable d'une machine, ce qui n'était possible d'aucune manière auparavant.
- Bon, parce que la convention entre par une décision écrite et tracée — ce que le dépôt exige de toute prescription de méthode, et qu'il avait fait respecter en retirant `openspec-git-discipline`.
- Bon, parce qu'aucune dépendance n'est ajoutée : la convention est de la prose, comme le reste.
- Neutre, parce que deux conventions coexisteront dans l'historique. C'est assumé et documenté, à l'image des archives que le dépôt refuse de réécrire.
- **Mauvais, parce que la classe de commit la plus caractéristique du dépôt — la correction d'une croyance antérieure, 15 % de l'historique — n'a pas de type propre.** Elle tombera en `docs` ou `fix`. Le garde-fou n°1 préserve le constat dans la phrase, mais la finesse de classement est perdue, et aucune mitigation ne la rend.
- Mauvais, parce que `chore` est un fourre-tout et le deviendra ici comme ailleurs. Sa part est à mesurer.
- Mauvais, parce que la table de correspondance devient un point de dérive silencieuse de plus, à côté de `REGISTRE.md` qui l'est déjà pour le routage.

### Confirmation

Trois contrôles, au premier bilan (20 commits conformes) :

- **Conformité** — `git log --format='%s' | grep -cvE '^(feat|fix|docs|refactor|test|chore)(\([a-z]+\))?!?: '` rend 0 sur les commits postérieurs à l'adoption.
- **Non-aplatissement** — aucun sujet ne se réduit à une étiquette ; relecture manuelle des 20.
- **Part de `chore`** — au-delà d'un commit sur cinq, le jeu de types est mal ajusté et cet ADR doit être révisé par un ADR successeur.

## Pros and Cons of the Options

### Conventional Commits 1.0.0, tel quel

Le standard public, sans modification.

- Bon, parce qu'il est lisible par des outils que le dépôt n'a pas écrits, et par des lecteurs qui ne connaissent pas le dépôt.
- Bon, parce qu'il ne demande aucune invention et aucune maintenance de format.
- Neutre, parce que son bénéfice phare — le semver automatique depuis `feat`/`fix` — ne s'applique qu'indirectement ici, l'axe de version étant le registre.
- Mauvais, parce qu'il n'a aucune catégorie pour la correction d'une croyance.
- Mauvais, parce que sa pente naturelle est l'étiquette (`fix: divers`), qu'il faut contrer par une exigence propre au dépôt.

### Une convention adaptée au domaine

Des types tirés des trois niveaux : `voix:`, `dispositif:`, `mesure:`.

- Bon, parce qu'elle épouse exactement l'axe de version du dépôt, sans table de correspondance.
- Bon, parce qu'un type `mesure:` nommerait précisément les 15 % que le standard perd.
- Mauvais, parce qu'aucun outil existant ne la lit : il faudrait écrire le parseur, donc l'entretenir.
- Mauvais, parce qu'elle ressemble à Conventional Commits sans en être — le pire des deux pour un lecteur extérieur.

### Garder les phrases, ajouter un pied de page machine

Sujet inchangé, plus `Registre: mineure` quand la version bouge.

- Bon, parce qu'il ne touche à rien de ce que les messages savent dire.
- Bon, parce que le pied de page porte directement le niveau de version, sans table intermédiaire ni interprétation.
- Neutre, parce qu'il reste une invention locale, même minimale.
- Mauvais, parce qu'il n'offre ni filtrage par type ni compatibilité avec l'outillage existant.
- Mauvais, parce qu'un champ facultatif posé à la main est oublié, et qu'un oubli y est silencieux.

### Refus argumenté

Écrire la décision de ne pas adopter.

- Bon, parce que c'est la forme que le dépôt maîtrise le mieux — 8 refus de voix, 3 licences écartées, chacun motivé.
- Bon, parce qu'il ne coûte rien et ne dégrade rien.
- Mauvais, parce qu'il laisse le problème entier : l'historique reste opaque à toute machine.
- Mauvais, parce qu'il conserve un travail de versionnement entièrement manuel, sans filet.

## More Information

Mesures à l'appui, prises sur `HEAD` au 2026-08-08 : 41 commits, 0 préfixe de type, 56 caractères de sujet moyen, 6 commits de correction de croyance identifiés par recherche sur *précision · correction · révision · vérifié · non-régression · faille*.

L'option 3 était la recommandation issue de l'analyse ; l'auteur a tranché pour l'option 1. Le désaccord est consigné ici parce que le dépôt tient que les motifs se publient — l'option 3 reste disponible **en complément** si la table de correspondance s'avère insuffisante à lever une ambiguïté.

Aucun outil de vérification n'est ajouté. Déclencheur de réouverture : **trois commits non conformes poussés sur `main`**, signe que la discipline seule ne suffit plus ; le premier candidat est un hook `commit-msg` d'une vingtaine de lignes en stdlib, sans dépendance.

La politique de branches reste non tranchée et interagira avec cette décision le jour où un changelog sera généré par branche. Elle relève d'un ADR distinct.

Réexamen prévu : au premier bilan, après 20 commits conformes.
