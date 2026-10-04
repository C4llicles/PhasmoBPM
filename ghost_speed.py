def convert_bpm_to_speed(bpm):
    if bpm is None:
        return None

    if bpm <= 115:
        return 0.4 + (bpm - 24) * (1.7 - 0.4) / (115 - 24)

    return 1.7 + (bpm - 115) * (3.0 - 1.7) / (232 - 115)


def bpm_adjustment(bpm, game_speed):
    if bpm is None:
        return "No speed calculated yet."
    if game_speed is None:
        return "Game speed not provided. Normal speed will be used."
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