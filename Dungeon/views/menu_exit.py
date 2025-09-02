from Dungeon.utils import ist_spiel_aktiv


def menu_exit(game_data):
    while True:
        if ist_spiel_aktiv(game_data):
            sicher = input('Möchtest du das Spiel wirklich beenden? (j/n): ').strip().lower()
            match sicher:
                case 'n':
                    return 'menu_main'
                case 'j':
                    print('Spiel wurde beendet.')
                    return 'end'
                case _:
                    print("Ungültige Eingabe – bitte 'j' für Ja oder 'n' für Nein eingeben.")
                    return 'menu_main'
        else:
            return 'end'
