import unittest
from random import randint
from unittest.mock import patch, call

from Dungeon.main import main
from Dungeon.views.game import game
from Dungeon.views.game import generate_player


class TestGenerateDungeon(unittest.TestCase):
    def test_lade_dungeon_und_spieler(self):
        game_data = {
            'dungeon': [[0]],
            'spieler': {'leben': 100, 'gold': 50, 'position': [0, 0]}
        }

        dungeon = game_data.get('dungeon')
        spieler = game_data.get('spieler')

        self.assertEqual(dungeon, [[0]], "Dungeon wurde nicht korrekt aus game_data geladen")
        self.assertEqual(spieler['leben'], 100, "Spielerleben stimmt nicht")
        self.assertEqual(spieler['gold'], 50, "Spielergold stimmt nicht")
        self.assertEqual(spieler['position'], [0, 0], "Spielerposition stimmt nicht")

    def test_start_position_und_werte(self):
        spieler = generate_player()
        self.assertEqual(spieler["position"], [0, 0], "Spielerstartposition ist falsch")
        self.assertEqual(spieler["leben"], 100, "Spielerleben beim Start ist falsch")
        self.assertEqual(spieler["gold"], 0, "Spielergold beim Start ist falsch")

    @patch('builtins.input', side_effect = [''])
    @patch('builtins.print')
    @patch('Dungeon.views.game.bewegung_im_dungeon', return_value = 'Erfolg')
    @patch('Dungeon.views.game.zug_verarbeiten', return_value = None)
    @patch('Dungeon.views.game.print_dungeon', return_value = None)
    def test_sieg_ausgabe(self, mock_print_dungeon, mock_zug, mock_bewegung, mock_print, mock_input):
        dungeon = [[{}, {}], [{}, {}]]
        gold = randint(0, 10)
        spieler = {'leben': 100, 'gold': gold, 'position': [1, 1]}
        game_data = {'dungeon': dungeon, 'spieler': spieler}

        result = game(game_data)

        self.assertEqual(result, 'end')

        mock_print.assert_any_call(
            'Sieg! Du hast den Dungeon erfolgreich mit', gold, 'Gold verlassen.'
        )

    @patch('Dungeon.views.game.zug_verarbeiten')
    @patch('Dungeon.views.game.bewegung_im_dungeon', return_value = 'Erfolg')
    @patch('builtins.input', side_effect = ['1', 's'])
    @patch('builtins.print')
    def test_game_over(self, mock_print, mock_input, mock_bewegung, mock_zug):
        def spieler_stirbt(_, spieler):
            spieler['leben'] = 0

        mock_zug.side_effect = spieler_stirbt
        main()

        mock_bewegung.assert_called_once()
        mock_print.assert_has_calls([call('Game Over! Du bist gestorben.')])


if __name__ == "__main__":
    unittest.main()
