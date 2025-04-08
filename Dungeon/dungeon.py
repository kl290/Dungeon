from bewegung_im_dungeon import bewegung_im_dungeon
from generate_dungeon import generate_dungeon
from print_dungeon import print_dungeon

leben = 100
gold = 0

# Begrüßung
print('Willkommen im Dungeon-Abenteuer!')
print('Sie befinden sich vor dem Eingang eines Dungeons.')

print()
# Funktion zum Erzeugen des Dungeons

# Initialisierung
dungeon = generate_dungeon(5, 5)

spieler_position = {
    'y': -1,
    'x': -1
}

while True:
    print()
    print('Dungeon Karte:')
    print_dungeon(dungeon, spieler_position)
    print('Leben:', leben, 'Gold:', gold)

    eingabe = input('Wohin möchten Sie gehen? (Osten = O, Westen = W, Süden = S, Norden = N, Q zum Beenden): ')

    ergebnis = bewegung_im_dungeon(dungeon, spieler_position, eingabe)

    if ergebnis == 'Fehler':
        print('Bewegung nicht erlaubt')
        continue

    if ergebnis == 'Erfolg':
        print('')