from Dungeon import STANDARD_SPIELER, validiereSpielerObjekt
from Dungeon.bewegung_im_dungeon import bewegung_im_dungeon
from Dungeon.print_dungeon import print_dungeon
from Dungeon.zug_verarbeiten import zug_verarbeiten


def game(game_data):
    if 'spieler' not in game_data:
        print("Es muss ein Spieler übergeben werden!")
        return 'menu_main'
    if 'dungeon' not in game_data:
        print("Es muss ein Dungeon übergeben werden!")
        return 'menu_main'

    dungeon = game_data.get('dungeon')
    spieler = game_data.get('spieler')

    validiereSpielerObjekt(spieler)

    print()
    print('Dungeon Karte:')
    print_dungeon(dungeon, spieler['position'])
    print('Leben:', spieler['leben'], 'Gold:', spieler['gold'])

    eingabe = input(
        'Wohin möchtest du gehen? (M = Menü, Osten = O, Westen = W, Süden = S, Norden = N): '
    ).strip().lower()

    if eingabe.lower() == 'm':
        return 'menu_main'

    ergebnis = bewegung_im_dungeon(dungeon, spieler, eingabe)

    match ergebnis:
        case 'Ende':
            print('Du hast den Dungeon verlassen.')
            return 'end'
        case 'Fehler':
            print('Bewegung nicht erlaubt.')
        case 'Erfolg':
            zug_verarbeiten(dungeon, spieler)

    if spieler['leben'] <= 0:
        print('Game Over! Du bist gestorben.')
        return 'end'

    if spieler['position'] == [len(dungeon[0]) - 1, len(dungeon) - 1]:
        print('Sieg! Du hast den Dungeon erfolgreich mit', spieler['gold'], 'Gold verlassen.')
        return 'end'

    return 'dungeon'


def generate_player():
    return {
        'leben': STANDARD_SPIELER['leben'],
        'gold': STANDARD_SPIELER['gold'],
        'position': STANDARD_SPIELER['position']
    }
