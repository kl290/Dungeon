def ist_spiel_aktiv(game_data):
    spieler = game_data.get("spieler")
    dungeon = game_data.get("dungeon")

    return spieler and dungeon