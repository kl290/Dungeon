import random

# Dungeon-Generierung
Raumtypen = ['F', 'S', 'L']


# Funktion zum Erzeugen des Dungeons
def generate_dungeon(y, x, gold_range = (10, 50), damage_range = (10, 40)):
    dungeon = {}
    for i in range(y):
        dungeon[i] = {}
        for j in range(x):
            raumtyp = random.choice(Raumtypen)
            if raumtyp == 'S':
                dungeon[i][j] = {
                    'raumtyp': raumtyp,
                    'gold': random.randint(gold_range[0], gold_range[1]),
                    'besucht': False
                }
            elif raumtyp == 'F':
                dungeon[i][j] = {
                    'raumtyp': raumtyp,
                    'schaden':random.randint(damage_range[0], damage_range[1]),
                    'besucht': False
                }
            else:
                dungeon[i][j] = {
                    'raumtyp': raumtyp,
                    'besucht': False
                }
    return dungeon
