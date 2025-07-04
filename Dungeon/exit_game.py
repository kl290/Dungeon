import sys


def exit_game(game_data):
    sicher = input("Möchtest du das Spiel wirklich beenden? (j/n): ").strip().lower()

    if sicher == 'n':
        return 'main_menu'

    elif sicher == 'j':
        print("Spiel wird beendet.")
        sys.exit()
