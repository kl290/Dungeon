from Dungeon.utilis.ist_spiel_aktiv import ist_spiel_aktiv


def menu_zurueck(game_data):
    if ist_spiel_aktiv(game_data):
        return 'dungeon'
    else:
        print("Kein Spiel aktiv. Du kannst nicht zurückkehren.")
        return 'menu_main'
