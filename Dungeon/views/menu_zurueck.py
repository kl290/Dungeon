from Dungeon.utils import ist_spiel_aktiv


def menu_zurueck(game_data):
    if ist_spiel_aktiv(game_data):
        return 'dungeon'

    print('Kein Spiel aktiv. Du kannst nicht zurückkehren.')
    return 'menu_main'
