import time
from queue import SimpleQueue

from pynput import keyboard

from windows_utils import get_foreground_process_name


class WindowsKeyboardListener:
    def __init__(self, tap_queue: SimpleQueue, target_processes=None, only_game=True):
        self.tap_queue = tap_queue
        self.only_game = only_game
        self.space_pressed = False

        if target_processes is None:
            target_processes = {"phasmophobia.exe"}

        self.target_processes = {name.lower() for name in target_processes}

        self.listener = keyboard.Listener(
            on_press=self._on_press,
            on_release=self._on_release,
            suppress=False,
        )

    def _is_game_active(self):
        process_name = get_foreground_process_name()

        if process_name is None:
            return False

        return process_name in self.target_processes

    def _on_press(self, key):
        if key != keyboard.Key.space:
            return
        if self.space_pressed:
            return
        self.space_pressed = True
        if self.only_game and not self._is_game_active():
            return
        self.tap_queue.put(time.perf_counter())

    def _on_release(self, key):
        if key == keyboard.Key.space:
            self.space_pressed = False

    def start(self):
        self.listener.start()
        self.listener.wait()

    def stop(self):
        self.listener.stop()
        self.listener.join()
