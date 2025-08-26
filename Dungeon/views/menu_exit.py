import sys

from Dungeon.utilis.ist_spiel_aktiv import ist_spiel_aktiv


def menu_exit(game_data):
    while True:
        sicher = input("Möchtest du das Spiel wirklich beenden? (j/n): ").strip().lower()
        match sicher:
            case "n":
                if ist_spiel_aktiv(game_data):
                    return "dungeon"
                else:
                    return "menu_main"
            case "j":
                print("Spiel wurde beendet.")
                sys.exit()
            case _:
                print("Ungültige Eingabe – bitte 'j' für Ja oder 'n' für Nein eingeben.")
                return "menu_main"
