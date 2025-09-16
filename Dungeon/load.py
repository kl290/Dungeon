import os
import pickle

from Dungeon.save import ORDNER_SPIELSTAENDE


def extract_dateiname(dateien, eingabe):
    try:
        index = int(eingabe) - 1
        if index < 0 or index >= len(dateien):
            raise RuntimeError("Ungültige Zahl! Bitte eine korrekte Nummer eingeben.")

        dateiname = dateien[index]

        if not dateiname.endswith(".kl"):
            raise RuntimeError(f"Die Datei '{dateiname}' kann nicht geöffnet werden: falsche Endung!")

        return dateiname
    except ValueError:
        raise RuntimeError("Ungültige Eingabe! Bitte eine Zahl eingeben.")


def load(dateien, eingabe, game_data):
    try:
        dateiname = extract_dateiname(dateien, eingabe)
        dateipfad = os.path.join(ORDNER_SPIELSTAENDE, dateiname)

        if not os.path.exists(dateipfad):
            print(f"Fehler: Die Datei '{dateipfad}' existiert nicht.")
            return 'menu_main'

        with open(dateipfad, 'rb') as f:
            geladene_daten = pickle.load(f)

        game_data.clear()
        game_data.update(geladene_daten)

        print(f"Spielstand '{dateipfad}' erfolgreich geladen!")
        return 'dungeon'

    except Exception as e:
        print(f"Fehler beim Laden des Spielstands: {e}")
        return 'menu_main'
