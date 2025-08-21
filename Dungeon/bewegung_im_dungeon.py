def bewegung_im_dungeon(dungeon, spieler, eingabe):
    x, y = spieler['position']

    if y not in dungeon or x not in dungeon[y]:
        spieler['position'] = [0, 0]
        return 'Erfolg'

    match eingabe:
        case 'n' | 'N':
            if y <= 0:
                return 'Fehler'
            spieler['position'] = [x, y - 1]
        case 's' | 'S':
            if y >= len(dungeon) - 1:
                return 'Fehler'
            spieler['position'] = [x, y + 1]
        case 'o' | 'O':
            if x >= len(dungeon[y]) - 1:
                return 'Fehler'
            spieler['position'] = [x + 1, y]
        case 'w' | 'W':
            if x < 1:
                return 'Fehler'
            spieler['position'] = [x - 1, y]
        case _:
            return 'Fehler'

    return 'Erfolg'
