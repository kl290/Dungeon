def menu_load(game_data):
    while True:
        print('________Hauptmenü________')
        print()
        print("X - Zurück zum Menü")

        eingabe = input('Welchen Spielstand möchtest du laden? (Zahl eingeben): ')
        print()

        match eingabe.strip().lower():
            case 'x':
                return 'menu_main'
            case _:
                print('Ungültige Eingabe! Gib entweder eine Zahl für das Laden eines Spielstandes ein '
                      'oder ein X um ins Hauptmenü zurückzukehren')
