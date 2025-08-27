from Dungeon.views.game import game
from Dungeon.views.menu_main import menu_main


def main():
    print('Bereit für das ultimative Dungeon-Erlebnis? Dein Abenteuer startet hier!')

    screen_id = 'menu_main'
    game_data = {}

    while True:
        match screen_id:
            case 'menu_main':
                screen_id = menu_main(game_data)

            case 'dungeon':
                screen_id = game(game_data)

            case 'end':
                break


if __name__ == '__main__':
    main()
