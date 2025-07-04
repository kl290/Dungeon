from Dungeon.bewegung_im_dungeon import bewegung_im_dungeon
from Dungeon.generate_dungeon import generate_dungeon
from Dungeon.print_dungeon import print_dungeon
from Dungeon.zug_verarbeiten import zug_verarbeiten
from exit_game import exit_game
from load_game import load_game
from save_game import save_game
from show_game import show_game


def ist_spiel_aktiv(game_data):
    spieler = game_data.get('spieler')
    dungeon = game_data.get('dungeon')
    if not spieler or not dungeon:
        return False

    if spieler.get('position') == [-1, -1]:
        return False

    return True


# screenOutput(screenId, {"dungeon": dungeon, "spieler": spieler})

def screen_output(screen_id, game_data):
    match screen_id:
        case 'main_menu':
            return main_menu(game_data)
        case 'load_game':
            return load_game(game_data)
        case 'save_game':
            return save_game(game_data)
        case 'exit_game':
            return exit_game(game_data)
        case 'game':
            return show_game(game_data)

    return None


def main_menu(game_data):
    print()
    print('________Hauptmenü________')
    print('1 - Neues Spiel starten')
    print('2 - Spielstand laden')
    print('3 - Spiel speichern')
    print('4 - Spiel beenden')
    print('X - Zurück zum Spiel')

    while True:
        print()
        wahl = input('Nummer: ')

        match wahl:
            case '1':
                return 'dungeon'
            case '2':
                return load_game(game_data)
            case '3':
                if ist_spiel_aktiv(game_data):
                    return save_game(game_data)
                else:
                    print('Kein aktives Spiel zum Speichern.')
            case '4':
                return exit_game(game_data)
            case 'x' | 'X':
                if ist_spiel_aktiv(game_data):
                    return 'dungeon'
                else:
                    print('Kein Spiel aktiv. Du kannst nicht zurückkehren.')
            case _:
                print('Ungültige Eingabe.')


def main_dungeon():
    spieler = generate_player()

    # Initialisierung
    dungeon = generate_dungeon(5, 5)
    game_data = {'dungeon': dungeon, 'spieler': spieler}

    screen_id = 'main_menu'

    print('Bereit für das ultimative Dungeon-Erlebnis? Dein Abenteuer startet hier!')

    while True:


        screen_id = screen_output(screen_id, game_data)

        ## verschieben
        print()
        print('Dungeon Karte:')
        print_dungeon(dungeon, spieler['position'])
        print('Leben:', spieler['leben'], 'Gold:', spieler['gold'])

        eingabe = input(
            'Wohin möchtest du gehen? (M = Menü, Osten = O, Westen = W, Süden = S, Norden = N): ')
        if eingabe == 'm' or eingabe == 'M':
            screen_id = 'main_menu'

        ergebnis = bewegung_im_dungeon(dungeon, spieler, eingabe)
        eingabe = eingabe.lower()

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


def generate_player():
    spieler = {
        'leben': 100,
        'gold': 0,
        'position': [-1, -1]
    }
    return spieler


if __name__ == '__main__':
    main_dungeon()
