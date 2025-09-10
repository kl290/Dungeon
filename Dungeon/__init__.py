STANDARD_SPIELER = {
    'leben': 100,
    'gold': 0,
    'position': [0, 0]
}


def validiereSpielerObjekt(spieler):
    if not istValiderSpieler(spieler):
        raise ValueError("Es müssen alle Elemente des Spielers übergeben werden!")


def istValiderSpieler(spieler):
    return STANDARD_SPIELER.keys() == spieler.keys()



