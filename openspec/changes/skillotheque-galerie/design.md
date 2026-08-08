## Context

Deux voix existent et fonctionnent (`~/.claude/skills/guy-debord/`, `~/.claude/skills/steve-albini/`), écrites à la main, hors de tout dépôt. Elles ont convergé spontanément vers une structure commune — une section « la tension à résoudre d'abord », une table d'inversion du lexique adverse, une section « ce qui casse la persona » — sans que ce format soit nommé. Ce changement le nomme et le rend routable.

Contraintes réelles :

- Une skill est un `SKILL.md` avec frontmatter `name` + `description`. La `description` est le déclencheur ; le corps est la charge utile.
- Le dépôt n'est pas sous git (`Is a git repository: false`). Sans versionnage, un rétrofit raté sur Debord ou Albini est une perte sèche.
- L'outillage de validation existe déjà : `guy-debord-workspace/optimizer/` — evals de déclenchement, quatre itérations d'amélioration pour **une** voix. C'est le coût unitaire réel d'une persona.
- `ponytail` fournit le modèle de la trace (`// ponytail:` posé dans le code, récolté par `/ponytail-debt`) et la preuve qu'une position peut être active sans être invitée.

## Goals / Non-Goals

**Goals**

- Un format de voix dont la sentinelle pourra se servir sans parser de la prose.
- Une règle d'admission exécutable, pas une intention — un test qui échoue quand deux voix font doublon.
- Un rétrofit de Debord et Albini sans les casser.
- Le lot 1 (Illich, Lessig) écrit et éprouvé.

**Non-Goals**

- La sentinelle. Le format est conçu pour elle, elle n'est pas construite ici.
- Toute forme de distribution ou de publication.
- Un outil. Rien dans ce changement ne justifie d'écrire un programme : `grep` et `ln -s` suffisent, et une skillothèque qui a besoin d'un build system a déjà perdu.

## Decisions

### D1 — Le dépôt est la source ; installation par lien symbolique

`skillotheque/voix/<nom>/SKILL.md` ← lié depuis `~/.claude/skills/<nom>`.

Une édition dans le dépôt est immédiatement active, sans étape de synchronisation. *Alternative écartée :* un script de copie — il introduit deux exemplaires d'un même fichier, donc une dérive, donc un jour une voix corrigée dans le dépôt et périmée dans `~/.claude`. `install.sh` est une boucle de trois lignes, réexécutable.

### D2 — Les quatre champs sont des sections markdown à titre normalisé, pas du frontmatter

```
## Question       une phrase, unique dans le dépôt
## Signaux        à quoi on reconnaît que la question est porteuse ici
## Compétence     ce que la voix sait FAIRE
## Trace          ce qu'elle laisse dans l'artefact
```

*Alternatives écartées :* des clés YAML personnalisées dans le frontmatter (un chargeur strict peut les rejeter, et le format de skill ne les documente pas) ; un fichier de métadonnées séparé par voix (deux fichiers à tenir synchrones — la dérive, encore). Des titres normalisés sont lisibles par un humain, chargés avec la skill, et extractibles par `grep -A3 '^## Question'`.

### D3 — `REGISTRE.md` est tenu à la main

Un tableau : voix, question, signaux, état, refus motivés. Sept lignes. C'est le fichier que la sentinelle lira — elle n'aura jamais besoin d'ouvrir les voix pour router.

*Alternative écartée :* le générer depuis les sections. Un build step pour sept lignes est exactement le genre de dette qu'un dépôt qui prêche la contre-productivité ne peut pas se permettre d'accumuler. Le registre diverge des fichiers ? Le test de disjonction (D6) le détecte.

### D4 — Une trace, un seul jeton, récolté par `grep`

```
// skillotheque: <voix> — <coût> — <qui le porte>          en code
<!-- skillotheque: <voix> — <coût> — <qui le porte> -->    en markdown
```

Même jeton, syntaxe de commentaire de l'hôte — les artefacts visés sont autant des specs et des roadmaps que du code. La récolte est `grep -rn "skillotheque:"`, pas un outil.

Le champ `<coût>` est ce qui distingue la critique de la décoration : une voix qui ne sait pas nommer un coût et son porteur n'a rien produit.

### D5 — La posture non-serviable est reprise telle quelle de l'existant

`guy-debord/SKILL.md:12` et `steve-albini/SKILL.md:10` résolvent déjà la tension centrale — *une persona qui refuse de faire quoi que ce soit est inutile ; un « assistant serviable » avec une peau de Debord est une fraude*. Chaque voix ouvre sur cette section. Le format est éprouvé, on ne le réinvente pas.

### D6 — Test de disjonction croisée : le critère d'admission opérationnel

Soumettre un même artefact aux N voix. **Si deux voix produisent la même trace, la disjonction a échoué et l'une des deux sort.** Falsifiable, sans framework, exécutable à la main en une session.

C'est ce qui transforme la règle d'admission d'une déclaration d'intention en un test. Deuxième critère, repris de l'existant : les evals de déclenchement, sur le modèle de `guy-debord-workspace/optimizer/`.

### D7 — Personnes vivantes : s'en tenir à l'œuvre publiée

Deux des sept sont vivants — **Federici** (née en 1942) et **Lessig** (né en 1961). Debord, Albini, Illich, Ostrom et Polanyi sont morts.

Règle : toute voix porte une section *« ce qu'il faut savoir et ne pas dissimuler »*, sur le modèle de `steve-albini/SKILL.md:23-25` qui traite frontalement ce qu'Albini a renié. Pour une personne vivante, contrainte supplémentaire : la voix raisonne depuis l'œuvre publiée et ne prend jamais position sur l'actualité au nom de la personne.

Pour Lessig, la section porte sur sa défense publique en 2019 des dons anonymes d'Epstein au MIT Media Lab, puis sa plainte en diffamation contre le *New York Times*, retirée. Elle est nommée, pas défendue. Dans un dépôt dont Albini est la conscience financière, c'est un rappel utile de ce que vaut la sophistication juridique devant la question simple *qui paie*.

### D8 — Lessig entre déclaré réformiste

Il est le seul non-anticapitaliste de la liste, admis sur le seul axe *code is law* — ses axes *free culture* et *dependence corruption* sont coupés pour doublon avec Ostrom et Albini. Son fichier déclare qu'il tient la position qui répare le système, et que cette position est peut-être ce qui permet au système de durer. Non déclarée, elle est la sortie de secours qu'un utilisateur sous pression attrapera toujours.

## Risks / Trade-offs

| Risque | Atténuation |
|---|---|
| Une voix dégénère en costume — du style sans compétence | Le champ `Trace` est obligatoire et vérifié par D6. Une voix sans trace n'entre pas. |
| Sept voix = sept jeux d'evals, coût d'entretien réel | Lot 1 de **deux** voix. Les cinq autres ne s'écrivent qu'après validation du format sur le cas le plus serré. |
| Le dogme : la voix trouve toujours quelque chose à dire | Le coût nommé de D4. Pas de coût identifiable → pas de trace → la voix se tait. Le silence devient un résultat, pas une absence. |
| Lessig légitime la sortie réformiste | D8 : déclaré dans son propre fichier. |
| Rétrofit destructeur sur Debord/Albini, sans git pour revenir | `git init` avant toute modification. Ordre imposé : copier dans le dépôt, vérifier, *puis* remplacer par un lien. |
| Le dépôt devient une posture consommable — la récupération | La trace est la contre-mesure structurelle : une voix qui ne modifie pas l'artefact échoue son propre test. La question de la publication reste ouverte et différée. |

## Migration Plan

1. `git init`. Rien ne bouge avant.
2. Structure : `voix/`, `REGISTRE.md`, `install.sh`.
3. **Rétrofit** : copier Debord et Albini dans `voix/`, ajouter les quatre sections en extrayant leurs tables d'inversion existantes (`guy-debord/SKILL.md:47-66`, `steve-albini/SKILL.md:49-64`) vers `Compétence` et `Signaux`. Vérifier le chargement. Puis seulement remplacer les originaux par des liens.
4. **Lot 1** : Illich, Lessig.
5. **Test de disjonction croisée sur les quatre.** Point d'arrêt : si deux voix produisent la même trace, corriger avant d'aller plus loin.
6. Lot 2 (Federici, Ostrom, Polanyi) — hors de ce changement, conditionné à l'étape 5.

**Rollback** : supprimer les liens, restaurer les fichiers depuis le dépôt. Les originaux ne sont jamais détruits, seulement remplacés après vérification.

## Open Questions

- ~~**Federici : la personne ou le courant ?**~~ **Tranché le 2026-08-08 : la personne**, sous la règle D7. *Wages for Housework* (Federici, Dalla Costa, Fortunati) gardait la compétence et perdait la voix — donc ce qui fait tenir une position sous la contradiction.
- **La distribution.** Différée depuis la proposition, pour la raison qui y est écrite.
- **La sentinelle lira-t-elle `REGISTRE.md` seul ?** Conçu pour, mais c'est le changement suivant qui le vérifiera.
