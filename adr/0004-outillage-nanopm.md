---
status: "accepted"
date: 2026-08-08
decision-makers: Tristan Rivoallan
consulted: —
informed: —
---

# `nanopm` n'entre pas au dépôt, et l'exclusion de routage passe par le `.gitignore` qui existait déjà

## Context and Problem Statement

`REGISTRE.md` porte une règle écrite après incident : *« une skill n'entre dans `.agents/skills/` que par décision, jamais par effet de bord d'une installation. »* Elle a coûté son inscription à `openspec-git-discipline`, arrivée par le `skills.txt` d'un schéma sans que personne ne la choisisse.

Le 2026-08-08 à 13:04:05, `.nanopm/` est apparu dans l'arbre de travail parce qu'une commande a été tapée. Quatre fichiers, 28 ko : un schéma de 15 533 octets décrivant trois couches, des sections calquées sur des phases, des types de page, des arêtes typées, une provenance obligatoire et un journal append-only — pour un index de 90 octets, zéro page, un verrou de 0 octet et un horodatage de lint passé sur rien.

C'est la catégorie même que la règle vise. Mais la règle **nomme un répertoire**, et `.nanopm/` s'est posé à la racine. La lettre ne l'atteint pas. Ce n'est pas une mauvaise règle : c'est une règle dont le périmètre a été écrit à partir du seul cas alors connu.

**Le coût de routage, mesuré — et la mesure a dû être corrigée en cours de rédaction.** Le journal de la sentinelle du 2026-08-08 compte 224 tours et 16 convocations, dont **12 déclenchées par des fichiers `.nanopm/`** ; `guy-debord` y est convoqué 8 fois, **8 fois sur `.nanopm/`**, dont 6 sur des jeux de fichiers quasi identiques. Le terme de routage est `baseline` ; `NANOPM-WIKI.md` le contient, pèse 15 ko, et le hook retient la voix qui touche le plus de termes. L'échafaudage n'a pas glissé dans le routage : il l'a remporté.

Mais ce journal est **global à la machine, non propre à ce dépôt**. Vérification faite, onze de ces douze convocations portent sur des chemins qui n'existent pas ici — `src/web/frontend/…`, `docs/architecture/adr/015-…`, `.nanopm/search.db`. Elles viennent d'un autre dépôt, où `.nanopm/` était installé depuis le matin. **Une seule est attribuable à ce dépôt : celle de 13:04:57, cinquante-deux secondes après la création du répertoire.**

Le phénomène est donc plus large que ce dépôt, et ce que ce dépôt peut en corriger est plus étroit que le chiffre ne le laissait croire.

**Un dernier constat décide du moyen.** Le `.gitignore` du dépôt porte déjà une catégorie et un motif par entrée :

```
# Outillage régénérable, non couvert par la licence du dépôt
.claude/    .serena/    __pycache__/
```

Et `travail_en_cours()` obtient les fichiers neufs par `git ls-files --others --exclude-standard`, qui applique `.gitignore`. La ligne `nom.startswith(".serena/")` du hook est donc **du code mort** — vérifié par sonde : un fichier déposé dans `.serena/` n'apparaît pas dans la sortie.

## Decision Drivers

- Ne pas laisser une méthode entrer par la voie du défaut, qui est celle par laquelle une skill est déjà entrée une fois.
- Réparer le périmètre de la règle sans l'affaiblir : ce qui déclenche, c'est ce qui est prescrit, non l'endroit où ça se pose.
- Ne rien ajouter au dispositif : le dépôt a un mécanisme d'exclusion, il n'en veut pas un second.
- Laisser une trace exploitable — un refus non consigné est un refus qu'on reprendra.
- Ne pas confondre la valeur d'un outil avec l'appartenance de ses artefacts au dépôt.

## Considered Options

1. **Non-admission, `.gitignore`, et ligne au tableau d'outillage**
2. **Admission par ADR** — les artefacts entrent au dépôt et la méthode est adoptée
3. **Supprimer les fichiers** — sans inscription au tableau
4. **Statu quo** — laisser non commité et non tranché

## Decision Outcome

Chosen option: **« Non-admission, `.gitignore`, et ligne au tableau d'outillage »**, parce que c'est la seule qui tranche sans rien construire — le dépôt s'était déjà donné cette troisième voie pour `.claude/`, un répertoire dont il se sert tous les jours et qu'il ne versionne pas.

La décision porte quatre points.

**D1 — `.nanopm/` est classé méthode prescrite.** Le test est celui de la capacité `admission-outillage` : un outil qui impose un ordre, des phases, des artefacts obligatoires ou un vocabulaire relève de cette catégorie. 15 533 octets de schéma ne rendent pas une capacité possible ; ils disent comment travailler.

Le contre-argument mérite d'être écrit plutôt qu'écarté : la session du 2026-08-08 a produit des mesures réelles — couverture de routage à 50 % sur les commits, six termes manquants à `lessig`, la part des convocations qui changent une décision. Cette valeur est réelle. **Elle n'a rien dû aux artefacts installés :** zéro page a été lue, parce que zéro page existait. Les 15 533 octets n'ont contribué à aucune ligne du résultat, qui est venu de la conversation et de la lecture du dépôt — disponibles sans rien poser dans l'arbre de travail.

**D2 — Les artefacts n'entrent pas au dépôt.** `.nanopm/` rejoint le `.gitignore` sous la catégorie existante, avec son motif. Le tableau d'outillage de `REGISTRE.md` porte la ligne : non admis, avec ce qu'il prescrivait et ce qui rouvrirait la question. Ce n'est ni supprimer ni commiter, et **ce n'est pas une interdiction d'usage** : le dépôt décide de ce qu'il versionne, pas de ce que l'auteur exécute.

**D3 — L'exclusion de routage passe par `.gitignore`, et le hook perd une ligne.** Aucun code d'exclusion n'est écrit : ignorer `.nanopm/` suffit à le soustraire à `--exclude-standard`. La ligne `.serena/` en dur est supprimée, étant morte depuis que l'entrée `.gitignore` existe — la garder laisserait croire que le hook tient sa propre liste. Une liste dans `REGISTRE.md`, un instant envisagée, est écartée : elle dupliquerait `.gitignore` en s'en écartant au premier oubli.

La distinction retenue n'est pas *suivi / non suivi* — un fichier neuf écrit par l'auteur reste examiné, et c'est voulu. Elle est *à vous / régénérable*, et `.gitignore` la porte déjà.

**D4 — La règle d'admission de l'outillage devient une capacité.** Elle cesse d'être un paragraphe de `REGISTRE.md` et cesse de nommer un répertoire. Six exigences, dont celle qui a manqué ici : le coût de routage d'un outil se chiffre avant sa décision.

### Consequences

- Bon, parce que la décision est prise avant que l'oubli ne la prenne, et que la voie du défaut — laisser non commité jusqu'à ce que ça se règle tout seul — est explicitement fermée.
- Bon, parce qu'aucun mécanisme n'est ajouté : une ligne de `.gitignore` remplace la liste d'exclusion qu'il aurait fallu écrire, lire et tenir.
- Bon, parce que le hook maigrit d'une ligne au lieu d'en gagner une, et qu'une ligne de code mort disparaît avec son illusion.
- Bon, parce que la règle d'admission cesse de dépendre d'un chemin, ce qui est précisément par quoi ce cas lui a échappé.
- Neutre, parce que l'outil reste installé et utilisable. Ce qui est refusé, c'est l'appartenance de ses artefacts au dépôt.
- **Mauvais, parce que le `.gitignore` ne corrige que ce dépôt.** Onze des douze convocations mesurées viennent d'un autre projet, où le même échafaudage est installé et où rien n'est décidé. La décision est un précédent, pas un remède ; l'affirmer autrement serait mentir sur la portée d'une ligne.
- Mauvais, parce qu'ignorer rend invisible. Un outil qui prescrit et qu'on ne voit plus prescrit toujours. La ligne au tableau est la seule trace, et elle vaut ce que vaut la discipline de la lire.
- Mauvais, parce que la skill recrée les fichiers à chaque invocation. `.gitignore` ne l'empêche pas, il l'ignore ; il reste 28 ko sur le disque et un répertoire qui se reconstitue.
- Mauvais, parce que le refus est prononcé **sans que la chaîne Define ait jamais tourné**. On écarte une méthode sur son appareil plutôt que sur son produit. C'est assumé et daté : le motif inscrit doit dire ce qui rouvrirait la question, faute de quoi le refus se durcit tout seul.
- Mauvais, parce que `--exclude-standard` dépend du `.gitignore` du clone. Un contributeur aux exclusions locales différentes verrait un routage différent. La sentinelle n'a jamais prétendu être reproductible d'une machine à l'autre ; à reprendre si elle devient bloquante en CI.

### Confirmation

- **Non-admission effective** — `git ls-files --others --exclude-standard` ne retourne aucun chemin sous `.nanopm/`.
- **Aucune liste d'exclusion dans le code** — `hooks/sentinelle.py` ne contient plus de saut de chemin en dur.
- **Refus consigné** — le tableau d'outillage de `REGISTRE.md` porte `nanopm`, son statut, ce qu'il prescrivait et le déclencheur de réouverture.
- **Routage rendu au travail** — sur le journal postérieur à cette décision, aucune convocation déclenchée par un fichier `.nanopm/` **de ce dépôt**. Les autres projets ne sont pas couverts et ce contrôle ne prétend pas les couvrir.

## Pros and Cons of the Options

### Non-admission, `.gitignore`, et ligne au tableau

- Bon, parce qu'elle emploie une catégorie que le dépôt s'était déjà donnée, avec son motif écrit.
- Bon, parce qu'elle ne coûte qu'une ligne et en supprime une autre.
- Bon, parce qu'elle sépare proprement l'usage d'un outil et l'appartenance de ses artefacts.
- Neutre, parce qu'elle laisse le répertoire sur le disque.
- Mauvais, parce qu'elle range hors de vue une chose qu'on a jugée, et qu'un rangement se prend pour un oubli six semaines plus tard.

### Admission par ADR

- Bon, parce qu'elle laisserait une chance à une méthode qu'on n'a pas essayée.
- Bon, parce que la trace serait maximale : la méthode adoptée, écrite, opposable.
- Mauvais, parce qu'elle ferait entrer 28 ko de schéma d'un fournisseur, sous une licence qui n'est pas celle du dépôt, pour zéro page de contenu.
- Mauvais, parce qu'adopter la méthode est le vrai objet du choix, et que rien dans l'usage constaté ne l'a encore demandée.

### Supprimer les fichiers

- Bon, parce que c'est immédiat et que rien n'est perdu — il n'y a rien dedans.
- Mauvais, parce que la skill les recrée à la prochaine invocation.
- Mauvais, parce qu'une suppression sans inscription viole l'exigence « un refus se consigne » : le dépôt oublierait une décision qu'il a prise, et rien n'empêcherait le retour par la même porte.

### Statu quo

- Bon, parce qu'il ne coûte rien aujourd'hui.
- Mauvais, parce que c'est exactement la voie par laquelle `openspec-git-discipline` est entrée, et que le dépôt a écrit une règle pour ne plus la prendre.
- Mauvais, parce que l'indécision laisse le routage capturé, sans que personne ait décidé de le payer.

## More Information

Mesures à l'appui, prises le 2026-08-08 : journal de la sentinelle, 224 tours, 16 convocations, 12 déclenchées par `.nanopm/` — dont **11 dans un autre dépôt** et une seule ici, cinquante-deux secondes après la création du répertoire. `guy-debord` convoqué 8 fois, 8 fois sur `.nanopm/`, dont 6 sur des jeux de fichiers quasi identiques ; ces répétitions tiennent à ce qu'un silence ne laisse pas de marqueur et se rejoue au tour suivant — défaut distinct, non traité ici.

La correction de portée a été faite en cours de rédaction : la première version de cet ADR attribuait les douze convocations à ce dépôt. Elle est consignée plutôt qu'effacée, le dépôt tenant que la correction d'une croyance est ce qu'un historique doit savoir dire.

Cet ADR ne supersède rien. `adr/0002` et `adr/0003` sont en force et ne parlent pas d'outillage.

Déclencheur de réouverture : **la chaîne Define exécutée pour de bon, produisant des pages lues au moins une fois dans un travail réel.** Le refus porte sur un appareil vide ; il ne survivrait pas à un contenu utilisé.
