from Dungeon.utilis.ist_spiel_aktiv import ist_spiel_aktiv

def menu_new(game_data):
    if ist_spiel_aktiv(game_data):
        while True:
            sicher = input(
                'Bist du sicher, dass du ein neues Spiel starten möchtest? (j/n): '
            ).strip().lower()

            match sicher:
                case 'n':
                    return 'dungeon'
                case 'j':
                    return 'menu_new'
                case _:
                    print("Ungültige Eingabe – bitte 'j' für Ja oder 'n' für Nein eingeben.")
    else:
        return 'menu_new'
