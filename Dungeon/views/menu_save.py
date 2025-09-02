from Dungeon.save import save
from Dungeon.utils import ist_spiel_aktiv


def menu_save(game_data):
    if not ist_spiel_aktiv(game_data):
        print('Kein aktives Spiel zum Speichern.')
        return "menu_main"

    print('________Spielstände________')
    name = input('Wie soll der Spielstand heißen? (nur Enter = zurück ins Menü): ').strip()

    if not name:
        print('Kein Name eingegeben – zurück ins Hauptmenü.')
        return 'menu_main'

    save(game_data, name)
    return 'menu_main'
