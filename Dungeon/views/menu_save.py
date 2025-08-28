import os
import pickle

from Dungeon.utils import ist_spiel_aktiv


def menu_save(game_data):
    if not ist_spiel_aktiv(game_data):
        print('Kein aktives Spiel zum Speichern.')
        return "menu_main"

    print('=== Spielstand speichern ===')
    name = input('Wie soll der Spielstand heißen? (Mit Leertaste kehrst du zurück ins Hauptmenü): ').strip()

    if not name:
        print('Kein Name eingegeben – zurück ins Hauptmenü.')
        return 'menu_main'

    ordner = 'Spielstände'
    os.makedirs(ordner, exist_ok = True)

    zahl = len(os.listdir(ordner)) + 1
    dateiname = os.path.join(ordner, f"{zahl}. {name}.pkl")

    with open(dateiname, 'wb') as f:
        pickle.dump(game_data, f)
    print(f"Spiel erfolgreich unter {dateiname} gespeichert!")

    return 'menu_main'
