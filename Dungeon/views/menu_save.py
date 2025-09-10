from Dungeon.save import save
from Dungeon.utils import ist_spiel_aktiv


def menu_save(game_data):
    if not ist_spiel_aktiv(game_data):
        print('Kein aktives Spiel zum Speichern.')
        return "menu_main"

    print('________Spielstände________')
    dateiname = input('Wie soll der Spielstand heißen? (nur Enter = zurück ins Menü): ')

    if not dateiname:
        print('Kein Name eingegeben – zurück ins Hauptmenü.')
        return 'menu_main'

    return save(game_data, dateiname)
