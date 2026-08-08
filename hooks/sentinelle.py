#!/usr/bin/env python3
"""Sentinelle — hook Stop.

Regarde ce qui vient d'être écrit, pas ce qui a été demandé : les voix se
déclenchent déjà seules quand l'utilisateur formule une critique, et jamais
quand la matière est dans le travail produit.

Elle ne classe pas et n'appelle aucun modèle — un aller-retour depuis un
hook coûte 9 à 13 secondes de latence bloquante. Elle pose la question au
modèle qui tourne déjà, par le motif du blocage.
"""
import json
import os
import re
import subprocess
import sys
import datetime

JOURNAL = os.environ.get("SENTINELLE_JOURNAL") or os.path.expanduser("~/.sentinelle/journal.log")
NOMS = {"Debord": "guy-debord", "Albini": "steve-albini",
        "Illich": "illich", "Lessig": "lessig"}
REPO = ""


def note(msg):
    """Le journal doit survivre à la session : c'est lui qui porte la mesure.

    La date et le dépôt sont dans la ligne parce qu'un journal durable les
    exige — sans date on ne sait plus quand, sans dépôt on ne peut plus dire
    quelle part des convocations tombe sur du travail écrit par l'usager.
    """
    if not JOURNAL:
        return
    try:
        os.makedirs(os.path.dirname(JOURNAL), exist_ok=True)
        with open(JOURNAL, "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} {REPO} {msg}\n")
    except OSError:
        pass  # ponytail: un journal muet vaut mieux qu'un hook qui plante


def git(args, cwd):
    try:
        r = subprocess.run(["git"] + args, cwd=cwd, capture_output=True,
                           text=True, timeout=5)
        return r.stdout if r.returncode == 0 else ""
    except Exception:
        return ""


def travail_en_cours(cwd):
    """Le travail non commité : suivi modifié, plus le contenu des fichiers neufs.

    Le hook ne reçoit aucune liste de fichiers écrits pendant le tour, et rien
    ne permet de la reconstituer sans prendre un instantané au début du tour.
    L'unité retenue est donc le travail non commité — ce qu'on a sur les bras
    en ce moment — et non « ce que ce tour a écrit ». Un fichier non suivi
    n'apparaît dans aucun diff, or c'est souvent le plus intéressant.

    Ce qui est exclu de l'examen se déclare au `.gitignore`, jamais ici :
    `--exclude-standard` l'applique déjà. Une liste en dur serait une décision
    de routage invisible là où les décisions se lisent (adr/0004).
    """
    if not git(["rev-parse", "--git-dir"], cwd):
        return None, []
    morceaux, fichiers = [git(["diff", "HEAD"], cwd)], []
    fichiers += [f for f in git(["diff", "HEAD", "--name-only"], cwd).split("\n") if f.strip()]
    for nom in git(["ls-files", "--others", "--exclude-standard"], cwd).split("\n"):
        nom = nom.strip()
        if not nom:
            continue
        chemin = os.path.join(cwd, nom)
        try:
            if os.path.getsize(chemin) < 200_000:
                morceaux.append(open(chemin, encoding="utf-8", errors="replace").read())
                fichiers.append(nom)
        except OSError:
            pass
    return "\n".join(morceaux), fichiers


def registre(racine):
    """Les voix routables, leur question et leurs termes — lus dans REGISTRE.md.

    Le registre est la source de routage depuis le premier jour ; il est ici
    exécutable. Une formulation approximative y est un défaut de
    fonctionnement, pas seulement de documentation.
    """
    voix, courante = {}, None
    try:
        lignes = open(os.path.join(racine, "REGISTRE.md"), encoding="utf-8").read().split("\n")
    except OSError:
        return voix
    for ligne in lignes:
        if ligne.startswith("### "):
            courante = NOMS.get(ligne[4:].strip())
            if courante:
                voix[courante] = {"termes": [], "question": "", "routable": False}
        elif not courante:
            continue
        elif "**Question**" in ligne:
            voix[courante]["question"] = ligne.split("—", 1)[-1].strip()
        elif "**Termes**" in ligne and "`" in ligne:
            voix[courante]["termes"] = [t.strip().lower()
                                        for t in ligne.split("`")[1].split(",") if t.strip()]
        elif "**Routage automatique**" in ligne:
            voix[courante]["routable"] = re.search(r"—\s*oui\s*$", ligne.strip()) is not None
    return {v: d for v, d in voix.items() if d["termes"]}


def motif(voix, question, termes, fichiers):
    """La question de SILENCE.md, adressée au modèle en cours.

    Les deux clauses comptent. « Porteuse » ne suffit pas : Illich a presque
    toujours quelque chose à dire d'un outil. Il faut que la réponse change
    quelque chose.
    """
    ou = ", ".join(fichiers[:4]) or "les fichiers modifiés"
    return (
        f"Le travail non commité ({ou}) porte des signaux de la voix "
        f"`{voix}` ({', '.join(termes[:4])}).\n\n"
        f"Sa question est : {question}\n\n"
        f"Deux clauses, et la seconde compte autant que la première :\n"
        f"1. Cette question est-elle porteuse sur ce qui vient d'être écrit ?\n"
        f"2. Sa réponse changerait-elle une décision ?\n\n"
        f"Ne demande jamais si la chose est capitaliste — c'est indécidable et "
        f"la réponse est toujours oui.\n\n"
        f"Si les deux réponses sont oui : convoque la skill `{voix}` sur ce "
        f"travail. Elle doit laisser dans le fichier son marqueur ET son "
        f"résultat structuré — le calcul, le tableau, le décompte, les règles. "
        f"Un marqueur seul porte une conclusion sans ce qui la fonde, et la "
        f"conversation fermée, plus personne ne peut la vérifier. Peu importe "
        f"que tu aies écrit ces lignes toi-même ou qu'elles étaient déjà là — "
        f"c'est le contenu qui est en question, pas son auteur.\n"
        f"Si l'une des deux est non : termine sans rien dire, et sans expliquer "
        f"que tu as vérifié. Le silence est un résultat."
    )


def main():
    try:
        entree = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    cwd = entree.get("cwd") or os.getcwd()
    global REPO
    REPO = os.path.basename(cwd)

    # Garde-fou fourni par le harnais : au second passage on laisse terminer.
    if entree.get("stop_hook_active"):
        note("second passage — on laisse terminer")
        sys.exit(0)

    diff, fichiers = travail_en_cours(cwd)
    if diff is None:
        note(f"hors dépôt git ({cwd}) — silence")
        sys.exit(0)
    if not diff.strip():
        note("aucune écriture — silence")
        sys.exit(0)

    racine = os.environ.get("CLAUDE_PLUGIN_ROOT") or os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))
    bas = diff.lower()
    candidates = []
    for voix, d in registre(racine).items():
        if not d["routable"]:
            continue
        # Voix déjà tracée dans ce diff : on ne la reconvoque pas.
        if f"incongru-voix: {voix.replace('guy-', '').replace('steve-', '')}" in bas:
            continue
        touches = [t for t in d["termes"] if t in bas]
        if touches:
            candidates.append((len(touches), voix, d["question"], touches))

    if not candidates:
        note(f"aucun terme routable ({len(diff)} car.) — silence")
        sys.exit(0)

    # Une seule convocation par tour : la plus saillante.
    candidates.sort(reverse=True)
    _, voix, question, touches = candidates[0]
    note(f"CONVOQUE {voix} ({', '.join(touches[:4])}) sur {', '.join(fichiers[:3])}")
    print(json.dumps({"decision": "block",
                      "reason": motif(voix, question, touches, fichiers)}))
    sys.exit(0)


if __name__ == "__main__":
    main()
