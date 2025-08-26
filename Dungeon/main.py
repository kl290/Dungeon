from Dungeon.initialisierung import initialisierung
from Dungeon.views.game import game
from Dungeon.views.menu_exit import menu_exit
from Dungeon.views.menu_load import menu_load
from Dungeon.views.menu_new import menu_new
from Dungeon.views.menu_save import menu_save
from Dungeon.views.menu_zurueck import menu_zurueck


def screen_output(screen_id, game_data):
    match screen_id:
        case 'menu_main':
            return menu_main(game_data)
        case 'menu_load':
            return menu_load(game_data)
        case 'menu_save':
            return menu_save(game_data)
        case 'menu_exit':
            return menu_new(game_data)
        case 'menu_new':
            return menu_new(game_data)
        case 'menu_zurueck':
            return menu_zurueck(game_data)

    return None


def menu_main(game_data):
    print()
    print("________Hauptmenü________")
    print("1 - Neues Spiel starten")
    print("2 - Spielstand laden")
    print("3 - Spiel speichern")
    print("4 - Spiel beenden")
    print("X - Zurück zum Spiel")

    while True:
        print()
        wahl = input('Nummer: ')

        match wahl:
            case '1':
                return menu_new(game_data)
            case '2':
                return menu_load(game_data)
            case '3':
                return menu_save(game_data)
            case '4':
                return menu_exit(game_data)
            case 'x' | 'X':
                return menu_zurueck(game_data)
            case _:
                print('Ungültige Eingabe.')
                return 'menu_main'


def main():
    game_data = {}
    screen_id = 'menu_main'

    print('Bereit für das ultimative Dungeon-Erlebnis? Dein Abenteuer startet hier!')

    while True:
        match screen_id:
            case 'menu_new':
                screen_id = initialisierung(game_data)

            case 'menu_main':
                screen_id = menu_main(game_data)

            case 'dungeon':
                screen_id = game(game_data)
                if screen_id == 'end':
                    break


if __name__ == '__main__':
    main()
