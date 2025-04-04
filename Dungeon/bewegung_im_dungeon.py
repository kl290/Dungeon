def bewegung_im_dungeon(dungeon, spieler_position, eingabe):
    # Position außerhalb des Dungeons
    if spieler_position["y"] not in dungeon or spieler_position["x"] not in dungeon[spieler_position["y"]]:
        spieler_position["x"] = 0
        spieler_position["y"] = 0
        return "Erfolg"

    # Position im Dungeon prüfen
    match eingabe:
        case "Q":
            print('Sie haben das Dungeon verlassen.')
            return "Ende"
        case "N":
            if spieler_position["y"] <= 0:
                return "Fehler"
            spieler_position["y"] -= 1
        case "S":
            if spieler_position["y"] >= len(dungeon) - 1:
                return "Fehler"
            spieler_position["y"] += 1
        case "O":
            if spieler_position["x"] >= len(dungeon[spieler_position["y"]]) - 1:
                return "Fehler"
            spieler_position["x"] += 1
        case "W":
            if spieler_position["x"] < 1:
                return "Fehler"
            spieler_position["x"] -= 1
        case _:
            return "Fehler"

    return "Erfolg"
