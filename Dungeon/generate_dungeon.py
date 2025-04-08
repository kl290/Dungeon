import random

# Dungeon-Generierung
Raumtypen = ['F', 'S', 'L']


# Funktion zum Erzeugen des Dungeons
def generate_dungeon(y, x):
    dungeon = {}
    for i in range(y):
        dungeon[i] = {}
        for j in range(x):
            raumtyp = random.choice(Raumtypen)
            if raumtyp == 'S':
                dungeon[i][j] = {
                    'raumtyp': raumtyp,
                    'gold': random.randint(10, 50),
                    'besucht': False
                }
            elif raumtyp == 'F':
                dungeon[i][j] = {
                    'raumtyp': raumtyp,
                    'schaden': random.randint(20, 50),
                    'besucht': False
                }
            else:
                dungeon[i][j] = {
                    'raumtyp': raumtyp,
                    'besucht': False
                }
    return dungeon
