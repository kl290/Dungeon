# Spielerstatus (Leben und Gold)
leben = 100
gold = 0

# Begrüßung
print('Willkommen im Dungeon-Abenteuer!')
print('Sie befinden sich vor dem Eingang eines Dungeons.')
print('Mit Eingabe einer beliebigen Richtung betreten Sie den ersten Raum im Dungeon.')

print()
# Funktion zum Erzeugen des Dungeons
from generate_dungeon import generate_dungeon

# Initialisierung
dungeon_aussen = generate_dungeon(5, 5)

spieler_position = [-1, -1]
from print_dungeon import print_dungeon

print()
print("Dungeon Karte:")
print_dungeon(dungeon_aussen, spieler_position)
print('Leben:', leben, "Gold:", gold)
print("Drücke Enter, um das Spiel zu starten:  ")

input()

while True:

    richtung = input('Wohin möchten Sie gehen? (Osten, Westen, Süden, Norden, Q zum Beenden): ')

    if richtung == 'Q':
        print('Sie haben das Dungeon verlassen.')
        break

    # ergebnis der bewegung = bewegung_ausführen(spielerposition, richtung)
    # ergebnis der auswertung = bewegung_auswerten(spielerposition)
    # "ergebnis der auswertung" auswerten
    #     "Erfolg" -> alles gut und weiter
    #     "Tod" -> Ende mit Nachricht

    # Bewege den Spieler in die angegebene Richtung
