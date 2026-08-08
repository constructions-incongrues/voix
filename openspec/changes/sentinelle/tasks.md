## 1. Vérifier le mécanisme avant d'écrire quoi que ce soit

- [x] 1.1 Écrire un hook `Stop` jetable qui journalise tout ce qu'il reçoit sur l'entrée standard, et le déclarer dans `plugin.json`
- [x] 1.2 Établir par observation : que reçoit-il exactement ? le chemin du transcript ? l'identifiant de session ? un moyen de connaître les fichiers modifiés ?
- [x] 1.3 Établir ce qu'il faut rendre pour **interrompre la fin de tour**, et si le motif fourni est réinjecté de façon exploitable par le modèle. **Toute la conception de D4 en dépend** — si le motif n'est pas exploitable, la sentinelle ne peut pas convoquer et il faut revenir au design avant de continuer
- [x] 1.4 Consigner le contrat observé dans le design, avec la date. C'est un mécanisme externe qui peut changer

## 2. Préfiltre seul, en observation

- [x] 2.1 Extraire les `Signaux` de `REGISTRE.md` — le registre devient exécutable, ce qui n'était jusqu'ici qu'une intention
- [x] 2.2 Obtenir le diff du tour. Dans un dépôt git, `git diff` ; hors git, trancher la question ouverte du design — se taire est une réponse acceptable pour une première version
- [x] 2.3 Recherche textuelle des signaux dans le diff, **journalisation seule, aucun blocage**
- [x] 2.4 Laisser tourner sur des tours réels et mesurer le taux de correspondance. **Point d'arrêt : au-delà d'un tour sur cinq, resserrer les `Signaux` avant d'aller plus loin.** Un préfiltre trop large fait payer un appel de modèle à chaque tour

## 3. Routage

> **Fusionné avec le groupe 4 en cours d'implémentation.** L'appel de modèle séparé est supprimé (D2 révisé, 9-13 s de latence bloquante mesurées) : le routage *est* le motif du blocage. Il n'y a plus d'étape intermédiaire à observer sans agir.

- [x] 3.1 Sur correspondance, appeler le modèle avec la question de `SILENCE.md` mot pour mot — *laquelle de ces questions est porteuse, et sa réponse changerait-elle la décision ?*
- [x] 3.2 Vérifier que la seconde clause filtre réellement : construire deux cas où une question s'applique sans que sa réponse ne change rien, et constater le silence
- [x] 3.3 Journaliser les verdicts sans agir. Les comparer à ce qu'on attendait, voix par voix
- [x] 3.4 Exclure du routage toute voix dont l'apport n'est pas établi — **Albini est le cas concret**, son apport est modeste sur le seul artefact éprouvé

## 4. Convocation et garde-fous

- [x] 4.1 Bloquer la fin de tour en nommant la voix porteuse, sans produire d'analyse
- [x] 4.2 Garde-fou de boucle : une voix dont le marqueur figure déjà dans le diff n'est pas convoquée
- [x] 4.3 Garde-fou de volume : au plus une convocation par tour, la plus saillante
- [x] 4.4 Éprouver la boucle pour de vrai — provoquer le cas où la sentinelle pourrait se rappeler elle-même, et constater qu'elle s'arrête

## 5. Déclaration

- [x] 5.1 `plugin.json` reçoit sa clé `hooks` — absente depuis `plugin-claude-code`, faute de hook à déclarer
- [ ] 5.2 README : les deux chemins d'installation **cessent d'être équivalents**. Seul le plugin porte la sentinelle. Sans quoi un utilisateur du clone attendra un dispositif qu'il n'a pas

## 6. Point d'arrêt — la sentinelle fait-elle le travail ?

- [ ] 6.1 Rejouer le protocole de `BASELINE.md` sur les quatre artefacts, **sans convocation forcée cette fois** : c'est la sentinelle qui doit appeler
- [ ] 6.2 Critère : l'artefact porte ensuite une trace **et** un contenu que le bras baseline ne produit pas. Le déclenchement seul ne vaut pas réussite
- [ ] 6.3 Vérifier l'exigence nouvelle de `trace-artefact` : le résultat structuré est-il dans le fichier, ou seulement dans la réponse ? C'est le défaut constaté sur Lessig
- [ ] 6.4 Mesurer le taux de déclenchement sur un corpus de tours ordinaires. **Au-delà d'un sur cinq, c'est cassé**
- [ ] 6.5 Une régression ou un dépassement de seuil bloque. Corriger et rejouer

## 7. Specs, README, publication

- [ ] 7.1 Synchroniser `sentinelle`, et les deltas de `admission-voix` et `trace-artefact`
- [ ] 7.2 Consigner les mesures dans `BASELINE.md` et `SILENCE.md`
- [ ] 7.3 Version : une voix devient convocable automatiquement — trancher explicitement ce que la règle du dépôt en dit
- [ ] 7.4 Pousser
