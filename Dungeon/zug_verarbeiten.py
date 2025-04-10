def zug_verarbeiten(dungeon, spieler):
    x, y = spieler['position']
    raum = dungeon[y][x]

    if raum['besucht']:
        print('In diesem Raum warst du bereits.')
    else:
        raum['besucht'] = True

        if raum['raumtyp'] == 'S':
            gold = raum['gold']
            spieler['gold'] += gold
            print('Du hast', gold, 'Gold gefunden!')

        elif raum['raumtyp'] == 'F':
            schaden = raum['schaden']
            spieler['leben'] -= schaden
            print('Du bist in eine Falle getreten und hast', schaden, 'Schaden genommen!')

        else:
            print('Der Raum ist leer.')
