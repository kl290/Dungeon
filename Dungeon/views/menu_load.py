import os

from Dungeon.load import load
from Dungeon.save import ORDNER_SPIELSTAENDE


def menu_load(game_data):
    print('________Spielstände________')

    if not os.path.exists(ORDNER_SPIELSTAENDE) or not os.listdir(ORDNER_SPIELSTAENDE):
        print('(Keine Spielstände vorhanden)')
        return 'menu_main'

    dateien = os.listdir(ORDNER_SPIELSTAENDE)
    dateien.sort(key = erstelldatum)

    for nummer, dateiname in enumerate(dateien, start = 1):
        print(f"{nummer}. {dateiname}")

    return eingabe_nummer(dateien, game_data)


def eingabe_nummer(dateien, game_data):
    eingabe = input("Nummer des Spielstandes eingeben (nur Enter = zurück zum Menü): ").strip()

    if not eingabe:
        print('Kein Name eingegeben – zurück ins Hauptmenü.')
        return 'menu_main'

    try:
        index = int(eingabe) - 1
        if index < 0 or index >= len(dateien):
            print("Ungültige Zahl! Bitte eine korrekte Nummer eingeben.")
            return 'menu_main'

        geladene_daten = load(dateien[index])
        if geladene_daten is None:
            print("Fehler beim Laden des Spielstands.")
            return 'menu_main'

        game_data.clear()
        game_data.update(geladene_daten)

        print(f"Spielstand '{dateien[index]}' erfolgreich geladen!")
        return 'dungeon'

    except ValueError:
        print("Ungültige Eingabe! Bitte eine Zahl eingeben.")
        return 'menu_main'


def erstelldatum(dateiname):
    return os.path.getctime(os.path.join(ORDNER_SPIELSTAENDE, dateiname))
