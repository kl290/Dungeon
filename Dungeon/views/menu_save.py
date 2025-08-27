from Dungeon.utils import ist_spiel_aktiv


def menu_save(game_data):
    if not ist_spiel_aktiv(game_data):
        print('Kein aktives Spiel zum Speichern.')
        return 'menu_main'

    print('=== Spielstand speichern ===')
    name = input('Wie soll der Spielstand heißen?: ').strip()

    if not name:
        print('Kein Name eingegeben – zurück ins Hauptmenü.')
        return 'menu_main'

    print(f"Spielstand '{name}' wurde gespeichert!")
    return 'menu_main'
