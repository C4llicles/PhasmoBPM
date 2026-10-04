from collections import deque
from config import DEFAULT_MAX_TAPS, EXPIRATION_DELAY, MINIMUM_INTERVAL

class BpmTracker:
    def __init__(self):
        self.bpm = 0.0
        self.taps = deque(maxlen=DEFAULT_MAX_TAPS)
        self.last_tap_time = None

        self.expiration_delay = EXPIRATION_DELAY
        self.minimum_interval = MINIMUM_INTERVAL

    def reset(self):
        self.bpm = 0.0
        self.taps.clear()
        self.last_tap_time = None

    def add_beat(self, timestamp):
        if self.last_tap_time is None:
            self.taps.append(timestamp)
            self.last_tap_time = timestamp
            self.bpm = 0.0
            return

        interval_since_last_tap = timestamp - self.last_tap_time

        if interval_since_last_tap > self.expiration_delay:
            self.reset()

            self.taps.append(timestamp)
            self.last_tap_time = timestamp
            self.bpm = 0.0
            return

        if interval_since_last_tap < self.minimum_interval:
            return

        self.taps.append(timestamp)
        self.last_tap_time = timestamp

        self._calculate_bpm()

    def _calculate_bpm(self):
        if len(self.taps) < 2:
            self.bpm = 0.0
            return

        first_tap = self.taps[0]
        last_tap = self.taps[-1]

        elapsed_time = last_tap - first_tap
        interval_count = len(self.taps) - 1

        if elapsed_time <= 0:
            self.bpm = 0.0
            return

        self.bpm = (interval_count / elapsed_time) * 60

    def get_bpm(self):
        if len(self.taps) < 2:
            return None

        return self.bpm

    def has_expired(self, current_time):
        if self.last_tap_time is None:
            return False

        return current_time - self.last_tap_time >= self.expiration_delay

    def update(self, current_time):
        if self.has_expired(current_time):
            self.reset()
            return True

        return False