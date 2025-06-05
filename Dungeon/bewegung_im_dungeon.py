def bewegung_im_dungeon(dungeon, spieler, eingabe):
    eingabe = eingabe.strip().lower()
    x, y = spieler['position']

    # Position außerhalb des Dungeons
    if y not in dungeon or x not in dungeon[y]:
        spieler['position'] = [0, 0]
        return 'Erfolg'

    # Position im Dungeon prüfen
    match eingabe:
        case 'n':
            if y <= 0:
                return 'Fehler'
            spieler['position'] = [x, y - 1]
        case 's':
            if y >= len(dungeon) - 1:
                return 'Fehler'
            spieler['position'] = [x, y + 1]
        case 'o':
            if x >= len(dungeon[y]) - 1:
                return 'Fehler'
            spieler['position'] = [x + 1, y]
        case 'w':
            if x < 1:
                return 'Fehler'
            spieler['position'] = [x - 1, y]
        case _:
            return 'Fehler'

    return 'Erfolg'
