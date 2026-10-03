from ghost import Ghost

class Aswang(Ghost):
    def __init__(self):
        super().__init__(
            name="Aswang",
            base_speed=1.53,
        )

class Banshee(Ghost):
    def __init__(self):
        super().__init__(
            name="Banshee",
        )

class Dayan(Ghost):
    def __init__(self):
        super().__init__(
            name="Dayan",
            min_speed=1.2,
            max_speed=2.25,
        )

class Deildegast(Ghost):
    def __init__(self):
        super().__init__(
            name="Deildegast",
            min_speed=0.4,
            base_speed=3.0,
            range=True
        )

class Demon(Ghost):
    def __init__(self):
        super().__init__(
            name="Demon",
        )

class Deogen(Ghost):
    def __init__(self):
        super().__init__(
            name="Deogen",
            min_speed=0.4,
            max_speed=3,
        )

class Gallu(Ghost):
    def __init__(self):
        super().__init__(
            name="Gallú",
            base_speed=1.7,
            min_speed=1.36,
            max_speed=1.96,
        )

class Goryo(Ghost):
    def __init__(self):
        super().__init__(
            name="Goryo",
        )

class Hantu(Ghost):
    def __init__(self):
        super().__init__(
            name="Hantu",
            min_speed=1.4,
            max_speed=2.7,
            los_max_speed=2.7,
            range=True
        )

class Jinn(Ghost):
    def __init__(self):
        super().__init__(
            name="Jinn",
            max_speed=2.5,
            range=False
        )

class Kormos(Ghost):
    def __init__(self):
        super().__init__(
            name="Kormos",
            max_speed=2.21,
            range=False
        )

class Mare(Ghost):
    def __init__(self):
        super().__init__(
            name="Mare",
        )

class Moroi(Ghost):
    def __init__(self):
        super().__init__(
            name="Moroi",
            base_speed=1.5,
            max_speed=2.25,
            los_max_speed=3.71,
            range=True
        )

class Myling(Ghost):
    def __init__(self):
        super().__init__(
            name="Myling",
        )

class Obake(Ghost):
    def __init__(self):
        super().__init__(
            name="Obake",
        )

class Obambo(Ghost):
    def __init__(self):
        super().__init__(
            name="Obambo",
            base_speed=1.45,
            max_speed=1.96,
        )

class Oni(Ghost):
    def __init__(self):
        super().__init__(
            name="Oni",
        )

class Onryo(Ghost):
    def __init__(self):
        super().__init__(
            name="Onryo",
        )

class Phantom(Ghost):
    def __init__(self):
        super().__init__(
            name="Phantom",
        )

class Poltergeist(Ghost):
    def __init__(self):
        super().__init__(
            name="Poltergeist",
        )

class Raiju(Ghost):
    def __init__(self):
        super().__init__(
            name="Raiju",
            base_speed=1.7,
            max_speed=2.5,
        )

class Revenant(Ghost):
    def __init__(self):
        super().__init__(
            name="Revenant",
            base_speed=1.0,
            max_speed=3.0,
        )

class Shade(Ghost):
    def __init__(self):
        super().__init__(
            name="Shade",
        )

class Spirit(Ghost):
    def __init__(self):
        super().__init__(
            name="Spirit",
        )

class Thaye(Ghost):
    def __init__(self):
        super().__init__(
            name="Thaye",
            base_speed=2.75,
            min_speed=1.0,
            range=True
        )

class TheMimic(Ghost):
    def __init__(self):
        super().__init__(
            name="The Mimic",
            base_speed=1.7,
            min_speed=0.4,
            max_speed=3.0,
            los_max_speed=3.75,
            range=True,
        )

class TheTwins(Ghost):
    def __init__(self):
        super().__init__(
            name="The Twins",
            base_speed=1.5,
            max_speed=1.9,
        )

class Wraith(Ghost):
    def __init__(self):
        super().__init__(
            name="Wraith",
        )

class Yokai(Ghost):
    def __init__(self):
        super().__init__(
            name="Yokai",
        )

class Yurei(Ghost):
    def __init__(self):
        super().__init__(
            name="Yurei",
        )