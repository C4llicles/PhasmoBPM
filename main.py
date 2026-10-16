import time
from queue import Empty, SimpleQueue

from bpm import BpmTracker
from ghost_options import GHOSTS
from ghost_speed import convert_bpm_to_speed
from input_windows import WindowsKeyboardListener


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
    tap_queue = SimpleQueue()
    listener = WindowsKeyboardListener(tap_queue, only_game=True)

    print("=== PhasmoBPM - Détection de fantômes ===")
    print("Appuie sur Espace dans Phasmophobia au rythme des pas.")
    print("Ctrl+C dans ce terminal pour quitter.\n")

    try:
        listener.start()

        while True:
            try:
                timestamp = tap_queue.get(timeout=0.1)
            except Empty:
                if tracker.update(time.perf_counter()):
                    print("\nMesure expirée.")
                continue

            tracker.add_beat(timestamp)
            display_result(tracker, GHOSTS)

    except KeyboardInterrupt:
        print("\nFermeture.")

    finally:
        listener.stop()


if __name__ == "__main__":
    main()
