STANDARD_SPIELER = {
    'leben': 100,
    'gold': 0,
    'position': [0, 0]
}

Raumtypen = ['F', 'S', 'L']


def validiere_spieler_objekt(spieler):
    if not ist_valider_spieler(spieler):
        raise ValueError("Es müssen alle Elemente des Spielers übergeben werden!")


def ist_valider_spieler(spieler):
    return isinstance(spieler, dict) and STANDARD_SPIELER.keys() == spieler.keys()


def validiere_dungeon(dungeon):
    for zeile in dungeon.values():
        for raum in zeile.values():
            if raum['raumtyp'] not in Raumtypen:
                raise ValueError("Dungeon enthält ungültige Räume!")
            if raum.get('besucht') not in [True, False]:
                raise ValueError("Raum 'besucht' muss True oder False sein!")
