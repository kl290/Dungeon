import os
import pickle

from Dungeon.save import ORDNER_SPIELSTAENDE


def load(dateiname):
    dateipfad = os.path.join(ORDNER_SPIELSTAENDE, dateiname)

    if not os.path.exists(dateipfad):
        print(f"Fehler: Die Datei '{dateipfad}' existiert nicht.")
        return None

    with open(dateipfad, 'rb') as f:
        return pickle.load(f)
