from config import BASE_SPEED, LOS_MULTIPLIER, TOLERANCE

class Ghost:
    def __init__(self, name, base_speed=BASE_SPEED, min_speed=None, max_speed=None, range=False, los_max_speed=None, los=True):
        self.name = name
        self.base_speed = base_speed

        if min_speed is None:
            min_speed = base_speed

        if max_speed is None:
            max_speed = base_speed

        self.min_speed = min_speed
        self.max_speed = max_speed
        self.los_max_speed = los_max_speed

        self.range = range

        self.los = los

        if self.los_max_speed is None:
            self.los_max_speed = self.max_speed_los_speed()

    def max_speed_los_speed(self):
        return self.max_speed * LOS_MULTIPLIER

    def matches_speed(self, speed, tolerance=TOLERANCE):
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

    def matches_los_speed(self, speed, tolerance=TOLERANCE):
        if speed is None:
            return False

        if self.range:
            minimum = self.min_speed - tolerance
            maximum = self.los_max_speed + tolerance

            return minimum <= speed <= maximum
        else:
            if self.min_speed - tolerance <= speed <= self.min_speed*LOS_MULTIPLIER + tolerance or self.base_speed - tolerance <= speed <= self.base_speed*LOS_MULTIPLIER + tolerance or self.max_speed - tolerance <= speed <= self.los_max_speed + tolerance:
                return True
            return False