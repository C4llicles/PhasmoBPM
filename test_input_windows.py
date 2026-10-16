import time
from queue import Empty, SimpleQueue

from bpm import BpmTracker
from input_windows import WindowsKeyboardListener


def main():
    tracker = BpmTracker()
    tap_queue = SimpleQueue()
    listener = WindowsKeyboardListener(tap_queue, only_game=True)

    print("Écoute active : Espacse = tap.")
    print("Ctrl+C dans ce terminal = quitter.")
    print("Attention : Espace est écoutée dans toutes les applications.\n")

    try:
        listener.start()

        while True:
            try:
                timestamp = tap_queue.get(timeout=0.1)
            except Empty:
                if tracker.update(time.perf_counter()):
                    print("Mesure expirée : -- BPM")
                continue

            tracker.add_beat(timestamp)
            bpm = tracker.get_bpm()

            if bpm is None:
                print("Premier tap : -- BPM")
            else:
                print(f"BPM : {bpm:.1f}")

    except KeyboardInterrupt:
        print("\nArrêt de l'écoute.")

    finally:
        listener.stop()


if __name__ == "__main__":
    main()
