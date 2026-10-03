class Ghost:
    LOS_MULTIPLIER = 1.65

    def __init__(self, name, base_speed=1.7, min_speed=None, max_speed=None, range=False, los_max_speed=None):
        self.name = name
        self.base_speed = base_speed

        if min_speed is None:
            min_speed = base_speed

        if max_speed is None:
            max_speed = base_speed

        self.min_speed = min_speed
        self.max_speed = max_speed
        self.los_max_speed = los_max_speed

        if self.los_max_speed is None:
            self.los_max_speed = self.max_speed_los_speed()

        self.range = range

    def max_speed_los_speed(self):
        return self.max_speed * self.LOS_MULTIPLIER

    def matches_speed(self, speed, tolerance=0.07):
        if speed is None:
            return False

        if self.range:
            minimum = self.min_speed - tolerance
            maximum = self.max_speed + tolerance

            return minimum <= speed <= maximum
        else:
            if self.min_speed - tolerance <= speed <= self.min_speed + tolerance or self.base_speed - tolerance <= speed <= self.base_speed + tolerance or self.max_speed - tolerance <= speed <= self.max_speed + tolerance:
                return True
            return False