import random

Raumtypen = ['F', 'S', 'L']


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
                    'schaden': random.randint(damage_range[0], damage_range[1]),
                    'besucht': False
                }
            else:
                dungeon[i][j] = {
                    'raumtyp': raumtyp,
                    'besucht': False
                }

    startraum_init(dungeon)

    return dungeon


def startraum_init(dungeon):
    dungeon[0][0] = {
        'raumtyp': 'L',
        'besucht': True
    }
