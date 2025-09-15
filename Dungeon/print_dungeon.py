def print_dungeon(dungeon, spieler_position):
    for y, zeile in enumerate(dungeon.values()):
        for x, raum in enumerate(zeile.values()):
            if spieler_position == [x, y]:
                print('P', end = '  ')
            else:
                if raum['besucht']:
                    print(raum['raumtyp'], end = '  ')
                else:
                    print('?', end = '  ')
        print()
