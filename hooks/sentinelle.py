#!/usr/bin/env python3
"""Sentinelle — hook Stop.

Regarde ce qui vient d'être écrit, pas ce qui a été demandé : les voix se
déclenchent déjà seules quand l'utilisateur formule une critique, et jamais
quand la matière est dans le travail produit.

Phase 2 : préfiltre et journalisation seuls. Aucun blocage.
"""
import json
import os
import subprocess
import sys
import datetime

JOURNAL = os.environ.get("SENTINELLE_JOURNAL", "")


def note(msg):
    if not JOURNAL:
        return
    with open(JOURNAL, "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now():%H:%M:%S} {msg}\n")


def git(args, cwd):
    try:
        r = subprocess.run(["git"] + args, cwd=cwd, capture_output=True,
                           text=True, timeout=5)
        return r.stdout if r.returncode == 0 else ""
    except Exception:
        return ""


def diff_du_tour(cwd):
    """Ce qui a été écrit : suivi modifié, plus le contenu des fichiers neufs.

    Un fichier non suivi n'apparaît dans aucun diff — or c'est souvent le
    plus intéressant, puisqu'il vient d'être créé.
    """
    if not git(["rev-parse", "--git-dir"], cwd):
        return None  # hors dépôt git : la sentinelle se tait
    morceaux = [git(["diff", "HEAD"], cwd)]
    for nom in git(["ls-files", "--others", "--exclude-standard"], cwd).split("\n"):
        nom = nom.strip()
        if not nom:
            continue
        chemin = os.path.join(cwd, nom)
        try:
            if os.path.getsize(chemin) < 200_000:
                with open(chemin, encoding="utf-8", errors="replace") as f:
                    morceaux.append(f.read())
        except OSError:
            pass
    return "\n".join(morceaux)


def registre(racine):
    """Les termes discriminants, lus dans REGISTRE.md.

    Le registre est la source de routage depuis le premier jour ; il devient
    ici exécutable. Une formulation approximative y est désormais un défaut
    de fonctionnement, pas seulement de documentation.
    """
    voix, courante = {}, None
    chemin = os.path.join(racine, "REGISTRE.md")
    try:
        lignes = open(chemin, encoding="utf-8").read().split("\n")
    except OSError:
        return voix
    noms = {"Debord": "guy-debord", "Albini": "steve-albini",
            "Illich": "illich", "Lessig": "lessig"}
    for ligne in lignes:
        if ligne.startswith("### "):
            courante = noms.get(ligne[4:].strip())
        elif courante and "**Termes**" in ligne and "`" in ligne:
            bruts = ligne.split("`")[1]
            voix[courante] = [t.strip().lower() for t in bruts.split(",") if t.strip()]
            courante = None
    return voix


def main():
    try:
        entree = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    # Garde-fou de boucle fourni par le harnais : au second passage, on laisse
    # terminer. Vérifié le 2026-08-08.
    if entree.get("stop_hook_active"):
        note("second passage, on laisse terminer")
        sys.exit(0)

    cwd = entree.get("cwd") or os.getcwd()
    diff = diff_du_tour(cwd)
    if diff is None:
        note(f"hors dépôt git ({cwd}) — silence")
        sys.exit(0)
    if not diff.strip():
        note("aucune écriture ce tour-ci — silence")
        sys.exit(0)

    racine = os.environ.get("CLAUDE_PLUGIN_ROOT", os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))))
    bas = diff.lower()
    touchees = {v: [t for t in termes if t in bas]
                for v, termes in registre(racine).items()}
    touchees = {v: t for v, t in touchees.items() if t}

    # Une voix qui a déjà laissé sa trace dans ce diff ne se reconvoque pas.
    touchees = {v: t for v, t in touchees.items()
                if f"incongru-voix: {v.replace('guy-', '').replace('steve-', '')}" not in bas}

    if not touchees:
        note(f"aucun terme ({len(diff)} car. de diff) — silence")
        sys.exit(0)

    note("PORTEUR " + " | ".join(f"{v}: {', '.join(t[:4])}" for v, t in touchees.items()))
    # Phase 2 : on observe, on ne bloque pas encore.
    sys.exit(0)


if __name__ == "__main__":
    main()
