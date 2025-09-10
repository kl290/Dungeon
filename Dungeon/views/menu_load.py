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

    eingabe = input("Nummer des Spielstandes eingeben (Enter = zurück zum Menü): ").strip()
    if not eingabe:
        return 'menu_main'

    return load(dateien, eingabe, game_data)


def erstelldatum(dateiname):
    return os.path.getctime(os.path.join(ORDNER_SPIELSTAENDE, dateiname))
