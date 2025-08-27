from Dungeon.views.menu_exit import menu_exit
from Dungeon.views.menu_load import menu_load
from Dungeon.views.menu_new import menu_new
from Dungeon.views.menu_save import menu_save
from Dungeon.views.menu_zurueck import menu_zurueck


def menu_main(game_data):
    while True:
        print()
        print('________Hauptmenü________')
        print('1 - Neues Spiel starten')
        print('2 - Spielstand laden')
        print('3 - Spiel speichern')
        print('4 - Spiel beenden')
        print('X - Zurück zum Spiel')
        print()
        wahl = input('Nummer: ')
        match wahl.strip().lower():
            case '1':
                return menu_new(game_data)
            case '2':
                return menu_load(game_data)
            case '3':
                return menu_save(game_data)
            case '4':
                return menu_exit(game_data)
            case 'x':
                return menu_zurueck(game_data)
            case _:
                print('Ungültige Eingabe.')
