## Why

Quatre voix écrites, publiées, conformes, éprouvées. Et mesuré hier : **elles ne se déclenchent jamais sur une demande de travail.** Zéro sur quatre — un plan d'orchestration promettant 3 h par semaine, une copy d'accueil vendant « une expérience qui vous rend plus présent », un term sheet en *full ratchet* avec vesting fondateurs remis à zéro, l'ajout d'une limite de débit. Aucun appel de voix, aucun marqueur de trace.

Elles se déclenchent quand l'utilisateur **demande une critique**. Elles ne voient rien quand la matière est dans le travail plutôt que dans la requête. C'est exactement la cible que ce dépôt s'était donnée, et elle n'est pas servie.

Convoquées de force, en revanche, les quatre produisent leur compétence et leur trace ([`BASELINE.md`](../../../BASELINE.md)). La machinerie fonctionne. **Il manque la pièce qui appelle.**

Le résultat qui décide de la forme : devant une page d'accueil affichant 87 % de retour quotidien comme une réussite, le modèle sans voix constate qu'il manque un appel à l'action et **en ajoute un**. Personne ne lui avait demandé d'optimiser une conversion. La matière critiquable n'était pas dans la requête, elle était dans ce qui venait d'être produit — et c'est là que la sentinelle doit regarder.

## What Changes

- **Un hook `Stop`** — la sentinelle s'exécute en fin de tour, sur le travail terminé. Pas à chaque écriture (coût par édition, interruption au milieu d'une chaîne), pas à la soumission du prompt (elle n'y verrait que la requête, précisément ce qui ne suffit pas).
- **Elle regarde le diff, pas la conversation.** Ce qui a été écrit ce tour-ci. C'est l'artefact, et c'est ce que la mesure désigne.
- **Un préfiltre sans modèle.** Les `Signaux` de `REGISTRE.md` sont cherchés textuellement dans le diff. Aucune correspondance, aucun appel de modèle, coût nul — ce qui doit être le cas de la grande majorité des tours.
- **Elle ne critique pas, elle convoque.** Sur correspondance, elle bloque la fin de tour en nommant la voix porteuse. C'est la voix qui produit ensuite sa compétence et sa trace — le mécanisme déjà mesuré comme fonctionnel, plutôt qu'un second chemin à éprouver.
- **La question posée n'est jamais « est-ce capitaliste ».** Elle est *laquelle des questions inscrites est porteuse ici, et sa réponse changerait-elle la décision ?* La première est indécidable et sa réponse est toujours oui, ce qui produit le dogme.
- **Un garde-fou de boucle** — un hook `Stop` qui bloque peut bloquer indéfiniment. Une voix déjà tracée sur ce diff ne se convoque pas deux fois.
- **`plugin.json` reçoit enfin sa clé `hooks`**, absente jusqu'ici faute de hook à déclarer.
- **Quatrième condition d'admission** — une voix ne doit être convocable automatiquement que si son apport contre le défaut a été mesuré. Établie hier, écrite dans le README, pas encore inscrite comme exigence.

## Capabilities

### New Capabilities

- `sentinelle` : la détection sur l'artefact produit, le routage par le registre, la convocation, le seuil de silence et la sûreté de boucle.

### Modified Capabilities

- `admission-voix` : les trois conditions deviennent quatre. Une voix dont le défaut fait déjà le travail ne doit pas être convoquée automatiquement — la convoquer coûterait un tour à l'utilisateur pour un apport nul, et c'est ainsi qu'un dispositif se fait couper.
- `trace-artefact` : le marqueur d'une ligne survit, l'analyse meurt avec la session. Mesuré sur Lessig, dont le tableau des quatre modalités n'entre jamais dans le fichier. L'exigence est trop maigre pour une trace produite par convocation automatique.

## Impact

- **Nouveau** — `hooks/` et son manifeste, le préfiltre, la logique de convocation.
- **`.claude-plugin/plugin.json`** — clé `hooks` ajoutée. Le plugin cesse d'être équivalent à `install.sh` : **les deux chemins d'installation ne sont plus interchangeables**, seul le plugin porte la sentinelle. Le README doit le dire.
- **`REGISTRE.md`** devient exécutable — ses `Signaux` alimentent le préfiltre. Une formulation approximative y devient un défaut de fonctionnement, plus seulement de documentation.
- **`openspec/specs/`** — une capacité créée, deux modifiées.
- **Latence par tour** — nulle quand le préfiltre ne matche pas, un appel de modèle sinon.
- **Le risque réel n'est pas technique** : c'est que l'utilisateur désactive le hook. Un dispositif qu'on éteint a échoué, quelles que soient ses mesures.

## Hors périmètre

- **Le lot 2** — Federici, Ostrom, Polanyi. Trois voix de plus à router avant que le routage n'ait fait ses preuves à quatre serait refaire l'erreur d'hier.
- **La couche lexicale constitutive** — *ressources humaines → gens*, *dette technique → code qu'on n'aime pas*. Elle agit pendant l'écriture, pas après ; c'est un `SessionStart` et un autre problème.
- **Le doublon d'installation**, toujours documenté et non résolu.
