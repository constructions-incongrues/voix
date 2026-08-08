## Context

Ce qui est établi par la mesure, et qui commande tout le reste :

```
requête où l'utilisateur amorce la critique     4/4 déclenchent
demande de travail ordinaire                    0/4 déclenchent
convocation forcée                              4/4 produisent compétence + trace
```

La machinerie fonctionne. Ce qui manque est l'appel. Et la matière critiquable est dans **ce qui vient d'être écrit**, pas dans ce qui a été demandé — établi par le cas de la page d'accueil, où le modèle nu répond à « relis cette page » en ajoutant un bouton d'inscription.

Ce qui existe sur la machine :

- `Stop` est un événement de hook supporté, et l'utilisateur en a déjà un configuré (`serena-hooks cleanup`). Forme confirmée : `{matcher, hooks: [{type: "command", command, timeout}]}`.
- Un plugin déclare ses hooks par `"hooks": "./hooks/<fichier>.json"` dans `plugin.json`. `install.sh` ne peut pas en poser — c'est la raison d'être du change `plugin-claude-code`.
- `REGISTRE.md` porte une section `Signaux` par voix, écrite dès le premier jour pour être la source de routage.

### Contrat du hook `Stop` — observé le 2026-08-08, pas supposé

Établi sur un hook jetable avant toute écriture, conformément à D7. **Mécanisme externe : à revérifier si le comportement change.**

Reçu sur l'entrée standard :

```json
{ "session_id": "…", "transcript_path": "…/<id>.jsonl", "cwd": "…",
  "prompt_id": "…", "permission_mode": "default", "hook_event_name": "Stop",
  "stop_hook_active": false, "last_assistant_message": "…",
  "background_tasks": [], "session_crons": [] }
```

Pour interrompre la fin de tour, rendre sur la sortie standard, code 0 :

```json
{ "decision": "block", "reason": "<texte réinjecté au modèle>" }
```

**Vérifié :** le motif est réinjecté *et exploitable*. Un motif demandant au modèle d'écrire un mot précis a produit ce mot, mot pour mot. La convocation de D4 est donc possible.

Deux conséquences que la conception n'avait pas anticipées :

- **`stop_hook_active` est un garde-fou de boucle fourni par le harnais.** À `true` au second passage, il permet au hook de laisser terminer. D5 inventait un garde-fou par marqueur ; celui-ci est gratuit et plus fiable. Les deux se cumulent — le premier empêche la boucle immédiate, le second empêche de reconvoquer la même voix d'un tour à l'autre.
- **Le hook ne reçoit aucune liste de fichiers modifiés.** Il reçoit `cwd`. La sentinelle doit donc calculer le diff elle-même, ce qui rend D1 nécessaire et non plus seulement préférable.

## Goals / Non-Goals

**Goals**

- Une voix convoquée sur un artefact réel, sans que l'utilisateur l'ait demandé.
- Un coût nul sur les tours où rien n'est porteur.
- Un critère d'acceptation qui ne soit pas « la sentinelle a parlé » mais « la trace est dans le fichier et dit ce que le défaut ne disait pas ».
- Un dispositif qu'on n'ait pas envie d'éteindre.

**Non-Goals**

- Que la sentinelle critique. Elle route, elle ne juge pas.
- Le lot 2, la couche lexicale, le doublon d'installation.

## Decisions

### D1 — `Stop`, et le diff comme matière

```
             quand           ce qu'elle voit        coût
UserPrompt   avant           la requête             nul, et aveugle à l'artefact
PreToolUse   avant l'écrit   l'intention            un appel par outil
PostToolUse  après l'écrit   une édition            un appel par édition, coupe une chaîne
Stop         fin de tour     LE TRAVAIL FINI        un appel par tour       ← retenu
```

Et la matière n'est pas la conversation mais **le diff du tour**. Dans un dépôt git, `git diff` ; sinon, les fichiers écrits. C'est précis, ça ne demande aucune lecture de transcript, et c'est exactement l'objet que la mesure désigne.

*Alternative écartée :* lire le transcript pour comprendre le contexte. Plus riche, plus cher, et ça ramène la sentinelle vers la requête — le lieu où l'on sait déjà que les voix se déclenchent toutes seules.

### D2 — Préfiltre textuel d'abord, modèle ensuite

```
diff du tour
   │
   ├─ aucun signal du registre trouvé ──────────► fin. Coût : zéro.
   │                                              (le cas de la grande majorité des tours)
   └─ un ou plusieurs signaux ──► appel de modèle
                                   « laquelle de ces questions est porteuse,
                                     et sa réponse changerait-elle la décision ? »
                                   │
                                   ├─ aucune ──► fin, silence
                                   └─ une ────► blocage du Stop, voix nommée
```

Les `Signaux` de `REGISTRE.md` sont déjà écrits pour ça. Le préfiltre leur donne une seconde fonction : **une formulation approximative dans le registre devient un défaut de fonctionnement**, plus seulement de documentation.

C'est aussi ce qui rend le seuil tenable. Sans préfiltre, un appel de modèle par tour, indéfiniment, pour un déclenchement attendu sur moins d'un tour sur cinq.

### D3 — La question posée au modèle est celle de `SILENCE.md`, mot pour mot

> Jamais « est-ce que c'est capitaliste ? » — indécidable, et sa réponse est toujours oui, ce qui produit le dogme.
> Toujours : **« laquelle de ces N questions est porteuse ici, et est-ce que sa réponse changerait la décision ? »**

La seconde clause est celle qu'on oubliera en implémentant. *Porteuse* ne suffit pas : Illich a presque toujours quelque chose à dire sur un outil, Lessig sur un défaut. Il faut que la réponse **change quelque chose**. Sans ce filtre, le seuil d'un tour sur cinq est intenable.

### D4 — Elle convoque, elle ne critique pas

Le hook bloque la fin de tour et nomme la voix porteuse. Le modèle convoque alors la voix, qui produit sa compétence et pose sa trace.

C'est le mécanisme **déjà mesuré** : la convocation forcée donne 4/4 avec traces bien formées. Faire produire l'analyse par le hook lui-même serait un second chemin, non éprouvé, et qui contournerait les voix — c'est-à-dire tout le dépôt.

*Alternative écartée :* poser silencieusement le marqueur sans rien dire, découvert plus tard en relisant. Séduisant — une critique qu'on ne peut pas muter — mais `BASELINE.md` a montré que le marqueur seul ne porte pas l'analyse : le tableau des quatre modalités de Lessig n'entre jamais dans le fichier. Un marqueur sans son analyse est la décoration que le dépôt interdit.

### D5 — Sûreté de boucle

Un hook `Stop` qui bloque peut bloquer le tour suivant, indéfiniment.

Garde-fou : **une voix déjà tracée dans le diff ne se convoque pas.** Le marqueur `incongru-voix: <voix>` sert de témoin. Il est déjà là, il est déjà cherché par `grep`, il ne coûte rien de plus.

Second garde-fou, indépendant : au plus une convocation par tour. Deux voix porteuses, la plus saillante gagne et l'autre attendra le tour suivant — un dispositif qui convoque trois voix d'affilée sera éteint avant la fin de la journée.

### D6 — Critère d'acceptation issu de `BASELINE.md`

La sentinelle est réussie non pas quand elle se déclenche, mais quand **le fichier contient ensuite une trace, et un contenu que le bras baseline ne produit pas**. Le protocole existe et il est écrit : deux bras, même consigne, un artefact réel.

Trois des quatre voix ont un apport franc ou maximal. **Albini est en sursis** — sur le term sheet, le défaut faisait déjà l'analyse. D'où la quatrième condition d'admission : une voix dont l'apport n'est pas mesuré ne doit pas être convoquée automatiquement. La convoquer coûte un tour à l'utilisateur pour rien, et c'est ainsi qu'on fait éteindre un hook.

### D7 — Le contrat du hook se vérifie avant d'être utilisé

Un hook jetable, qui journalise ce qu'il reçoit et tente un blocage, avant toute logique de sentinelle. Trois conclusions fausses hier, toutes tirées de suppositions raisonnables sur un mécanisme non vérifié. Celle-ci ne le sera pas.

## Risks / Trade-offs

| Risque | Atténuation |
|---|---|
| **L'utilisateur désactive le hook.** Le vrai mode d'échec, et aucune mesure ne le prévient. | D2 (coût nul le plus souvent), D3 (le filtre « ça change quelque chose »), D5 (une seule convocation par tour), D6 (ne convoquer que des voix dont l'apport est établi). Toutes visent la même chose : qu'il n'y ait jamais de raison de l'éteindre. |
| Boucle infinie de blocage | D5, deux garde-fous indépendants. |
| Le préfiltre rate ce qui compte | Il est délibérément large — il ne décide pas, il ne fait qu'éviter un appel de modèle. Un faux positif coûte un appel ; un faux négatif coûte une convocation manquée, et se mesure. |
| Le contrat de hook n'est pas celui supposé | D7 : vérifié sur un hook jetable avant d'écrire quoi que ce soit. |
| Deux chemins d'installation divergent enfin pour de bon | Le plugin porte la sentinelle, `install.sh` non. À dire dans le README, sans quoi un utilisateur du clone attendra un dispositif qu'il n'a pas. |
| La sentinelle convoque et la voix n'apporte rien | D6 et la quatrième condition d'admission. Albini est le cas concret. |

## Migration Plan

1. **Vérifier le contrat `Stop`** sur un hook jetable — entrée reçue, sortie qui bloque, motif réinjecté ou non. Rien ne s'écrit avant.
2. Préfiltre seul, en journalisation, sans blocage : sur quelle proportion de tours réels matche-t-il ? Si c'est plus d'un sur cinq, resserrer les `Signaux` avant d'aller plus loin.
3. Routage par modèle, toujours sans blocage, journalisé. Comparer ses verdicts à ce qu'on attendait.
4. Blocage et convocation, garde-fous compris.
5. `plugin.json` reçoit sa clé `hooks`.
6. **Point d'arrêt** : protocole `BASELINE.md` sur les quatre artefacts, en laissant la sentinelle faire le travail. Critère : trace posée, contenu que le bras baseline ne produit pas.
7. Specs, README, publication.

**Rollback** : retirer la clé `hooks` de `plugin.json`. La sentinelle disparaît, les voix restent convocables à la main.

## Open Questions

- **Le blocage réinjecte-t-il un motif exploitable par le modèle ?** Toute la conception de D4 en dépend. Réponse à l'étape 1, pas avant.
- **Que fait la sentinelle hors d'un dépôt git ?** Le diff est la matière ; sans git il faut une autre source. Peut-être rien — se taire est une réponse acceptable, et probablement la bonne pour une première version.
- **Albini reste-t-il routable ?** Son apport est modeste sur le seul artefact éprouvé. Un second artefact — un contrat de prestation, un partage de revenus — trancherait avant de décider.
