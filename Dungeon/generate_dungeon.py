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
                gold = random.randint(gold_range[0], gold_range[1])
                if not (gold_range[0] <= gold <= gold_range[1]):
                    print('Goldwert außerhalb der Range!')
                dungeon[i][j] = {
                    'raumtyp': raumtyp,
                    'gold': gold,
                    'besucht': False
                }
            elif raumtyp == 'F':
                schaden = random.randint(damage_range[0], damage_range[1])
                if not (damage_range[0] <= schaden <= damage_range[1]):
                    print('Schadenswert außerhalb der Range!')
                dungeon[i][j] = {
                    'raumtyp': raumtyp,
                    'schaden': schaden,
                    'besucht': False
                }
            else:
                dungeon[i][j] = {
                    'raumtyp': raumtyp,
                    'besucht': False
                }
    return dungeon
