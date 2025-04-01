def print_dungeon(dungeon, spieler_position):
    for y in range(0, len(dungeon)):
        for x in range(0, len(dungeon[y])):
            if spieler_position == (y, x):
                print('P', end = '  ')
            else:
                if [y, x] == [0, 0]:
                    print('E', end = '  ')
                elif dungeon[y][x]['besucht']:
                    print(dungeon[y][x]['raumtyp'], end = '  ')
                else:
                    print('?', end = '  ')  # Unbesuchte Position
        print()
