# Test de disjonction croisée

Critère d'admission opérationnel du registre : **un même artefact soumis à toutes les voix ; si deux traces se recouvrent, une voix sort.** À rejouer à chaque candidate.

## Exécution du 2026-08-08 — quatre voix

**Conditions.** Test appliqué en session par lecture des sections `Compétence` et `Trace` de chaque fichier, et non par quatre convocations indépendantes. C'est le contrôle le plus fort disponible avant redémarrage ; il détecte les recouvrements de forme, pas les dérives de ton. À rejouer en convocations séparées.

**Artefact soumis** — un plan trimestriel choisi pour provoquer la collision : il porte à la fois un pitch, un contrat implicite, une automatisation et une contrainte technique.

> **T3 — plateforme d'onboarding self-service pour mainteneurs open source.**
> Modèle freemium. Le support de niveau 1 est automatisé par un bot.
> L'export des données de contribution est réservé au plan payant.
> Pitch : « rendez votre communauté vivante ».

### Traces produites

```
<!-- incongru-voix: debord — « rendez votre communauté vivante » = une base
     d'utilisateurs mesurée, vendue à celui qui l'anime — qui est séparé :
     les contributeurs, entre eux, par le tableau de bord qui les compte -->

// incongru-voix: albini — les mainteneurs fabriquent les données de
   contribution / la plateforme les facture / la plateforme les possède
   — qui absorbe : les mainteneurs, non payés et non propriétaires

// incongru-voix: illich — seuil 2.1 (le bot N1 renvoie 6 h/semaine de
   reprise humaine pour 3 h de tickets évités) — qui perd : le mainteneur
   d'astreinte, qui ne peut ni inspecter ni corriger le bot

// incongru-voix: lessig — export des contributions rendu impossible dans
   l'UI, régulé par l'architecture et non par les CGU qui l'autorisent
   — recours : aucun
```

### Verdict

**Disjonction établie.** Quatre traces, quatre objets distincts :

| Voix | Objet de la trace |
|---|---|
| Debord | une phrase retournée + qui elle sépare |
| Albini | une chaîne de propriété + qui absorbe le manque |
| Illich | un ratio chiffré + qui perd le temps |
| Lessig | une modalité de régulation + la voie de recours |

**Paire la plus serrée : Albini / Lessig**, tous deux déclenchés par le verrouillage de l'export. Ils ne convergent pas : Albini répond *à qui appartient la chose*, Lessig répond *qui peut contester la règle*. Propriété contre recours. À surveiller à la prochaine candidate ; c'est ici que la disjonction cédera en premier si elle cède.

## Faille de méthode découverte le 2026-08-08

**Ce test mesure la disjonction des traces, pas celle du routage.** Deux voix peuvent produire des traces parfaitement distinctes et se disputer quand même la même requête — c'est la voix convoquée qui décide, et elle est choisie avant que la moindre trace n'existe.

La faille s'est manifestée : sur *« notre landing page promet une expérience qui vous rend plus vivant, et le tableau de bord compte les sessions actives »* — un tableau de bord qui tient lieu de la chose qu'il mesure, littéralement dans les `Signaux` de Debord — **c'est Illich qui a été convoqué**. Non parce que sa question convenait mieux, mais parce que sa description était de forme *situation* (« à convoquer chaque fois qu'un outil promet… ») quand celle de Debord était de forme *invitation* (« quand l'utilisateur veut parler avec Debord »). Illich gagnait par défaut.

Un test de disjonction complet comporte donc **deux volets** :

| Volet | Ce qu'il vérifie | Comment |
|---|---|---|
| traces | deux voix ne produisent pas le même objet | même artefact soumis à toutes les voix |
| **routage** | **la bonne voix est convoquée sur sa propre situation** | **une requête par voix, décrivant sa situation sans la nommer** |

Le second est celui dont dépendra la sentinelle : elle route sur la situation, jamais sur un nom.

### Volet routage — exécution du 2026-08-08

| Requête (aucune voix nommée) | Attendu | Obtenu |
|---|---|---|
| landing page promettant « une expérience qui vous rend plus vivant », tableau de bord de sessions | debord | `guy-debord` |
| pipeline CI censé faire gagner du temps, rafistolé tous les matins | illich | `illich` |
| fonds proposant 2M pour 18 % avec liquidation préférentielle 1,5× | albini | `steve-albini` |
| blocage à 100 req/min sans notification ni voie de contestation | lessig | `lessig` |

Les deux premiers ont d'abord échoué. Correction appliquée : les descriptions de **Debord** et **Albini** ouvrent désormais sur une clause de situation — *« à convoquer chaque fois que le travail porte sur… même quand X n'est pas nommé »* — calquée sur leur propre section `Signaux`. Illich et Lessig l'avaient dès l'écriture ; les deux voix héritées d'un usage opt-in ne l'avaient jamais eue.

**Toute voix admise doit porter une clause de situation.** Une voix qui n'existe que sur invitation ne sera jamais convoquée par une sentinelle.

### Rejeu du volet routage après le renommage `voix/` → `skills/`

Même exécution, mêmes quatre requêtes, plus un cas ordinaire : `guy-debord`, `illich`, `steve-albini`, `lessig`, puis silence sur un ajout d'index SQL. Le renommage ne touche aucune `description` — c'est la vérification qui l'établit, pas le raisonnement.

Ces sondes tournent sans `--plugin-dir` : elles passent donc par les liens d'`install.sh`, ce qui vaut aussi contrôle du chemin d'installation sans plugin.

### Collision anticipée, non encore testée

**Illich / Federici (lot 2).** Le *travail fantôme* d'Illich — le travail non payé exigé par la société de consommation — recoupe la question de Federici. Arbitrage déjà inscrit dans `skills/illich/SKILL.md` : Illich cède la place sur la structure de ce travail et n'en garde que le volume. **À vérifier par ce test avant d'admettre Federici**, pas après.
