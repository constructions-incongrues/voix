## Why

`REGISTRE.md` porte une règle, écrite après un incident et appliquée une fois : *« une skill n'entre dans `.agents/skills/` que par décision, jamais par effet de bord d'une installation. »* Elle a coûté son inscription à `openspec-git-discipline`, arrivée par le `skills.txt` d'un schéma, sans que personne ne l'ait choisie.

Le 2026-08-08, un second cas s'est présenté — et il est passé à côté de la règle, non parce qu'elle est mauvaise, mais parce qu'elle nomme un répertoire.

`.nanopm/` est apparu dans l'arbre de travail parce qu'une commande a été tapée. Mesuré :

| | |
|---|---|
| fichiers | 4 |
| `NANOPM-WIKI.md` | **15 533 octets** de schéma : trois couches, sections calquées sur des phases, types de page, arêtes typées, provenance, journal append-only |
| `wiki/index.md` | 90 octets — un titre et l'interdiction de l'écrire à la main |
| `wiki/.last-lint` | un horodatage. Un lint a passé sur zéro page |
| `wiki/.lock` | 0 octet. Un verrou sur rien |
| **pages** | **0** |

C'est une méthode produit entière — ce qu'il faut définir, dans quel ordre, sous quelle forme, avec quel vocabulaire. Exactement la catégorie que la règle vise. Mais `.agents/skills/` ne la contient pas : elle s'est posée à la racine du dépôt, et **la lettre de la règle ne l'atteint pas.**

Le coût n'est pas théorique. Le journal de la sentinelle du même jour, 202 tours :

- **16 convocations**, dont **12 — 75 % — déclenchées par des fichiers `.nanopm/`** qui ne font pas partie du travail.
- **8 convocations de `guy-debord`, toutes sur `.nanopm/`**, dont six sur des jeux de fichiers quasi identiques. Le terme de routage est `baseline` ; `NANOPM-WIKI.md` le contient, pèse 15 ko, et le classement du hook retient la voix qui touche le plus de termes. L'échafaudage ne s'est pas glissé dans le routage — il l'a remporté, seize fois.

Enfin, un constat qui décide du périmètre : **aucune des dix capacités du dépôt ne couvre l'admission de l'outillage.** `admission-voix` spécifie l'entrée d'une voix — trois conditions, disjonction croisée, plafond de sept. L'entrée d'un outil, elle, ne tient qu'à un paragraphe de `REGISTRE.md`. La règle qui a fait retirer une skill n'est pas une exigence ; c'est de la prose.

## What Changes

- Le dépôt **tranche le cas `.nanopm/`** : il entre par décision, ou il ne reste pas. Le statu quo — le garder non commité parce que personne ne s'en occupe — est écarté, parce que c'est la voie du défaut et que le dépôt en a retiré une skill pour l'avoir prise.
- La règle d'admission de l'outillage **cesse d'être de la prose** et devient une capacité spécifiée, avec ses conditions et ses scénarios.
- Son périmètre **cesse de nommer un répertoire**. Ce qui déclenche la règle est *ce que la chose prescrit*, non *l'endroit où elle se pose* : `.agents/skills/`, la racine, ou ailleurs.
- Une **exclusion de routage** est décidée pour ce que la sentinelle examine. `travail_en_cours()` inclut délibérément les fichiers non suivis — *« souvent le plus intéressant »*, dit le commentaire — et n'exclut que `.serena/`, en dur. La décision porte sur la règle générale, pas sur une seconde exception au cas par cas.
- Le tableau d'outillage de `REGISTRE.md` gagne sa ligne, quel que soit le verdict. **Un refus se consigne comme une admission** — le dépôt compte huit refus de voix et trois licences écartées, chacun motivé.

## Capabilities

### New Capabilities

- `admission-outillage` : à quelles conditions un outil entre au dépôt, ce qui distingue une capacité apportée d'une méthode prescrite, ce que la trace doit contenir quel que soit le verdict, et ce que le dispositif de convocation a le droit de lire.

### Modified Capabilities

Aucune. `admission-voix` porte l'entrée d'une voix critique et ses quatre conditions ; elles sont écrites pour des voix et ne s'appliquent pas à un outil — `REGISTRE.md` le dit déjà. Les deux capacités se ressemblent et ne se recouvrent pas.

## Impact

- **`REGISTRE.md`** — la règle d'outillage renvoie à la capacité plutôt que de la porter seule, et le tableau gagne la ligne `nanopm`.
- **`hooks/sentinelle.py`** — l'exclusion de routage, si elle est décidée. Aujourd'hui `.serena/` est en dur ; une règle générale la remplacerait.
- **`.gitignore`** — le dépôt n'en a pas pour `.nanopm/`. Selon le verdict, c'est là que ça se règle.
- **`adr/0004`** — la décision, au format des trois précédentes.
- **Aucune dépendance ajoutée**, quel que soit le verdict. Refuser ne coûte rien ; admettre coûte 28 ko de schéma et un répertoire d'état.
