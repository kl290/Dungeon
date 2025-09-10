from Dungeon.generate_dungeon import generate_dungeon
from Dungeon.utils import ist_spiel_aktiv
from Dungeon.views.game import generate_player


def menu_new(game_data):
    if ist_spiel_aktiv(game_data):
        while True:
            sicher = input('Bist du sicher, dass du ein neues Spiel starten möchtest? (j/n): '
                           ).strip().lower()

            match sicher:
                case 'n':
                    return 'dungeon'
                case 'j':
                    break
                case _:
                    print("Ungültige Eingabe – bitte 'j' für Ja oder 'n' für Nein eingeben.")

    return initialisierung(game_data)


def initialisierung(game_data):
    spieler = generate_player()
    dungeon = generate_dungeon(5, 5)
    game_data['spieler'] = spieler
    game_data['dungeon'] = dungeon

    return 'dungeon'
