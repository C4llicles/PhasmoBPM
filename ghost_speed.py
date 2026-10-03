def convert_bpm_to_speed(bpm):
    if bpm is not None:
        speed = bpm * (1.7 / 115)
    return speed

def bpm_adjustment(bpm, game_speed):
    if bpm is None:
        return "No speed calculated yet."
    if game_speed is None:
        return "Game speed not provided."
    match (game_speed):
        case "very_slow":
            bpm /= 0.5
        case "slow":
            bpm /= 0.75
        case "normal":
            pass
        case "fast":
            bpm *= 0.75
        case "very_fast":
            bpm *= 0.5
        case _:
            return "Invalid game speed option."
    return bpm