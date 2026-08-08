## ADDED Requirements

### Requirement: Budget de description et ordre de priorité

La `description` d'une voix MUST tenir dans la limite de la spécification tout en portant les clauses que ce format rend obligatoires. Ces deux exigences entrent en concurrence pour un espace fini, et l'ordre de priorité MUST être respecté quand il faut arbitrer :

1. **La clause de situation** — intouchable. Sans elle, la voix n'est convocable que par son nom, et une autre voix remporte ses requêtes par défaut.
2. **La clause d'exclusion des demandes expositives** — le fond est intouchable, l'énumération des cas est compressible.
3. **Les amorces nommées** — trois à quatre suffisent, dont une dans une autre langue que celle du fichier.
4. **La mention de contre-voix** — une phrase ; le développement appartient au corps du fichier.
5. **Les exemples d'outillage tiers** — supprimables sans condition. Ce sont des exemples, jamais des dépendances, et ils coûtent plusieurs centaines de caractères pour aucun déclenchement propre.

Sans budget écrit, chaque voix admise repassera au-dessus de la limite et sera corrigée après coup, au moment où sa correction est la plus risquée.

#### Scenario: Description trop longue à l'écriture
- **QUAND** la `description` d'une voix candidate dépasse la limite
- **ALORS** elle est réduite en commençant par le rang le plus bas de l'ordre de priorité

#### Scenario: Arbitrage atteignant les clauses obligatoires
- **QUAND** la réduction des rangs 3 à 5 ne suffit pas à passer sous la limite
- **ALORS** la clause de situation est conservée intégralement et l'arbitrage est rapporté à l'auteur plutôt que tranché en silence
