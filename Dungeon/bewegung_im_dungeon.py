from Dungeon import validiereSpielerObjekt

def bewegung_im_dungeon(dungeon, spieler, eingabe):
    validiereSpielerObjekt(spieler)

    x, y = spieler['position']

    if y < 0 or y >= len(dungeon) or x < 0 or x >= len(dungeon[y]):
        spieler['position'] = [0, 0]
        return 'Fehler'

    match eingabe.strip().lower():
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
            if x <= 0:
                return 'Fehler'
            spieler['position'] = [x - 1, y]
        case _:
            return 'Fehler'

    return 'Erfolg'
