import os
import pickle

from Dungeon.save import ORDNER_SPIELSTAENDE


def load(dateien, eingabe, game_data):
    try:
        index = int(eingabe) - 1
        if index < 0 or index >= len(dateien):
            print("Ungültige Zahl! Bitte eine korrekte Nummer eingeben.")
            return 'menu_main'

        dateiname = dateien[index]
        dateipfad = os.path.join(ORDNER_SPIELSTAENDE, dateiname)

        if not os.path.exists(dateipfad):
            print(f"Fehler: Die Datei '{dateipfad}' existiert nicht.")
            return 'menu_main'

        if not dateiname.endswith(".kl"):
            print(f"Die Datei '{dateiname}' kann nicht geöffnet werden: falsche Endung!")
            return 'menu_main'

        with open(dateipfad, 'rb') as f:
            geladene_daten = pickle.load(f)

        game_data.clear()
        game_data.update(geladene_daten)

        print(f"Spielstand '{dateien[index]}' erfolgreich geladen!")
        return 'dungeon'

    except ValueError:
        print("Ungültige Eingabe! Bitte eine Zahl eingeben.")
        return 'menu_main'
    except Exception as e:
        print(f"Fehler beim Laden des Spielstands: {e}")
        return 'menu_main'
