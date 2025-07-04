import json
import os


def save_game(game_data):
    name = input('Wie soll der Spielstand heißen?: ').strip()

    ordner = 'Spielstände'

    os.makedirs(ordner, exist_ok = True)
    dateiname = os.path.join(ordner, f'{name}.json')

    try:
        with open(dateiname, 'w') as file:
            json.dump(game_data, file, indent = 4)
        print('Spiel erfolgreich unter', dateiname, 'gespeichert!')
    except Exception as e:
        print('Fehler beim Speichern:', e)

    return 'main_menu'
