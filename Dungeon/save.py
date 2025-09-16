import os
import pickle
import re

ORDNER_SPIELSTAENDE = "Spielstände"


def save(game_data, dateiname):
    if not dateiname.endswith(".kl"):
        dateiname += ".kl"

    if not os.path.exists(ORDNER_SPIELSTAENDE):
        os.makedirs(ORDNER_SPIELSTAENDE, exist_ok = True)

    dateipfad = os.path.join(ORDNER_SPIELSTAENDE, dateiname)

    try:
        with open(dateipfad, "xb") as f:
            pickle.dump(game_data, f)

        return "menu_main"

    except FileExistsError:
        eingabe_name, versionsnummer = neue_namensteile_bestimmen(dateiname)

        neuer_name = f"{eingabe_name} ({versionsnummer}).kl"

        return save(game_data, neuer_name)


def neue_namensteile_bestimmen(dateiname):
    dateiname_match = dateiname_aufteilen(dateiname)

    eingabe_name = dateiname_match.group(1)
    versionsnummer = int(dateiname_match.group(3) or 0) + 1

    return eingabe_name, versionsnummer


def dateiname_aufteilen(dateiname):
    regex = re.compile(r'(.+?)( \((-?[0-9]+)\))?\.kl')
    dateiname_match = regex.fullmatch(dateiname)
    return dateiname_match
