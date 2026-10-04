import time

from bpm import BpmTracker
from ghost_speed import convert_bpm_to_speed
from ghost_options import GHOSTS


def get_possible_ghosts(speed, ghosts):
    possible_ghosts = []

    for ghost in ghosts:
        if ghost.matches_speed(speed):
            possible_ghosts.append(ghost)

    return possible_ghosts


def display_result(tracker, ghosts):
    bpm = tracker.get_bpm()

    if bpm is None:
        print("Pas assez de taps pour calculer le BPM.")
        return

    speed = convert_bpm_to_speed(bpm)
    possible_ghosts = get_possible_ghosts(speed, ghosts)

    print(f"\nBPM mesuré : {bpm:.1f}")
    print(f"Vitesse estimée : {speed:.2f} m/s")

    if not possible_ghosts:
        print("Aucun fantôme ajouté ne correspond à cette vitesse.")
        return

    print("Fantômes possibles :")

    for ghost in possible_ghosts:
        print(f"- {ghost.name}")


def main():
    tracker = BpmTracker()

    print("=== PhasmoBPM - Détection de fantômes ===")
    print("Appuie sur Entrée au rythme des pas.")
    print("Tape r puis Entrée pour réinitialiser.")
    print("Tape q puis Entrée pour quitter.\n")

    while True:
        command = input("> ").strip().lower()

        if command == "q":
            print("Fermeture.")
            break

        if command == "r":
            tracker.reset()
            print("Mesure réinitialisée.")
            continue

        tracker.add_beat(time.perf_counter())
        display_result(tracker, GHOSTS)


if __name__ == "__main__":
    main()