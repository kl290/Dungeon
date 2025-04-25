from Dungeon.bewegung_im_dungeon import bewegung_im_dungeon
from Dungeon.generate_dungeon import generate_dungeon
from Dungeon.print_dungeon import print_dungeon
from Dungeon.zug_verarbeiten import zug_verarbeiten


def main_dungeon():
    spieler = {
        'leben': 100,
        'gold': 0,
        'position': [-1, -1]
    }

    # Begrüßung
    print('Willkommen im Dungeon-Abenteuer!')
    print('Du befindest dich vor dem Eingang eines Dungeons.')

    # Initialisierung
    dungeon = generate_dungeon(5, 5)

    while True:
        print()
        print('Dungeon Karte:')
        print_dungeon(dungeon, spieler['position'])
        print('Leben:', spieler['leben'], 'Gold:', spieler['gold'])

        eingabe = input('Wohin möchtest du gehen? (Osten = O, Westen = W, Süden = S, Norden = N, Q zum Beenden): ')

        ergebnis = bewegung_im_dungeon(dungeon, spieler, eingabe)

        match ergebnis:
            case 'Ende':
                print('Du hast den Dungeon verlassen.')
                break
            case 'Fehler':
                print('Bewegung nicht erlaubt.')
            case 'Erfolg':
                zug_verarbeiten(dungeon, spieler)

        if spieler['leben'] <= 0:
            print()
            print('Game Over! Du bist gestorben.')
            break

        if spieler['position'] == [len(dungeon[0]) - 1, len(dungeon) - 1]:
            print()
            print('Sieg! Du hast den Dungeon erfolgreich mit', spieler['gold'], 'Gold verlassen.')
            break


if __name__ == '__main__':
    main_dungeon()
