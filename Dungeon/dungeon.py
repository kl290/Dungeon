from bewegung_im_dungeon import bewegung_im_dungeon
from generate_dungeon import generate_dungeon
from print_dungeon import print_dungeon

spieler = {
    'leben': 100,
    'gold': 0,
    'position': [-1, -1]
}

# Begrüßung
print('Willkommen im Dungeon-Abenteuer!')
print('Sie befinden sich vor dem Eingang eines Dungeons.')

print()
# Funktion zum Erzeugen des Dungeons

# Initialisierung
dungeon = generate_dungeon(5, 5)


while True:
    print()
    print('Dungeon Karte:')
    print_dungeon(dungeon, spieler)
    print('Leben:', spieler['leben'], 'Gold:', spieler['gold'])

    eingabe = input('Wohin möchten Sie gehen? (Osten = O, Westen = W, Süden = S, Norden = N, Q zum Beenden): ')

    ergebnis = bewegung_im_dungeon(dungeon, spieler, eingabe)

    if ergebnis == 'Fehler':
        print('Bewegung nicht erlaubt')
        continue

    if ergebnis == 'Erfolg':
        print("")