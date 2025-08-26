from Dungeon.generate_dungeon import generate_dungeon
from Dungeon.views.game import generate_player


def initialisierung(game_data):
    spieler = generate_player()
    dungeon = generate_dungeon(5, 5)
    game_data['spieler'] = spieler
    game_data['dungeon'] = dungeon

    return 'dungeon'
