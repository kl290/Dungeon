def ist_spiel_aktiv(game_data):
    spieler = game_data.get("spieler")
    dungeon = game_data.get("dungeon")
    if not spieler or not dungeon:
        return False

    if spieler.get("position") == [-1, -1]:
        return False

    return True