import unittest
from unittest.mock import patch

from Dungeon.generate_dungeon import generate_dungeon
from Dungeon.print_dungeon import print_dungeon
from Dungeon.views.game import game
from Dungeon.views.game import generate_player
from Dungeon.zug_verarbeiten import zug_verarbeiten


class TestGame(unittest.TestCase):

    @patch('builtins.print')
    def test_dungeon_fehlt(self, mock_print):
        game_data = {'spieler'}
        result = game(game_data)

        self.assertEqual(result, 'menu_main')
        mock_print.assert_any_call('Es muss ein Dungeon übergeben werden!')

    @patch('builtins.print')
    def test_spieler_fehlt(self, mock_print):
        game_data = {'dungeon'}
        result = game(game_data)

        self.assertEqual(result, 'menu_main')
        mock_print.assert_any_call('Es muss ein Spieler übergeben werden!')

    @patch('builtins.input', side_effect = ['1', 'm', '4', 'j'])
    @patch('Dungeon.views.game.zug_verarbeiten', wraps = zug_verarbeiten)
    @patch('Dungeon.views.game.bewegung_im_dungeon', return_value = 'Erfolg')
    @patch('Dungeon.views.game.print_dungeon', wraps = print_dungeon)
    @patch('Dungeon.views.menu_new.generate_dungeon', wraps = generate_dungeon)
    def test_dungeon_ablauf(self, spy_generate, spy_print, spy_bewegung, spy_zug, mock_input):
        dungeon = spy_generate(5, 5)
        spieler = generate_player()
        game_data = {'dungeon': dungeon, 'spieler': spieler}

        game(game_data)

        spy_generate.assert_called_once_with(5, 5)
        self.assertEqual(spy_print.call_count, 1)
        self.assertEqual(spy_bewegung.call_count, 1)
        self.assertEqual(spy_zug.call_count, 1)

    @patch('builtins.input', return_value = 'o')
    @patch('builtins.print')
    @patch('Dungeon.views.game.zug_verarbeiten')
    @patch('Dungeon.views.game.print_dungeon')
    @patch('Dungeon.views.game.bewegung_im_dungeon', return_value = 'Erfolg')
    def test_game_over(self, mock_bewegung, mock_print_dungeon, mock_zug, mock_print, mock_input):
        dungeon = generate_dungeon(3, 3)
        spieler = {'leben': 0, 'gold': 0, 'position': [0, 0]}

        game_data = {'dungeon': dungeon, 'spieler': spieler}

        result = game(game_data)

        self.assertEqual(result, 'end')

        mock_print.assert_any_call('Dungeon Karte:')
        mock_print.assert_any_call('Leben:', 0, 'Gold:', 0)
        mock_print.assert_any_call('Game Over! Du bist gestorben.')

    @patch('builtins.input', return_value = 'o')
    @patch('builtins.print')
    @patch('Dungeon.views.game.zug_verarbeiten')
    @patch('Dungeon.views.game.print_dungeon')
    @patch('Dungeon.views.game.bewegung_im_dungeon', return_value = 'Erfolg')
    def test_game_sieg(self, mock_bewegung, mock_print_dungeon, mock_zug, mock_print, mock_input):
        dungeon = generate_dungeon(3, 3)
        spieler = {'leben': 100, 'gold': 50, 'position': [len(dungeon[0]) - 1, len(dungeon) - 1]}

        game_data = {'dungeon': dungeon, 'spieler': spieler}

        result = game(game_data)

        self.assertEqual(result, 'end')

        mock_print.assert_any_call('Dungeon Karte:')
        mock_print.assert_any_call('Leben:', spieler['leben'], 'Gold:', spieler['gold'])
        mock_print.assert_any_call(
            'Sieg! Du hast den Dungeon erfolgreich mit', spieler['gold'], 'Gold verlassen.'
        )

    def test_lade_dungeon_und_spieler(self):
        dungeon = [[0]]
        spieler = {'leben': 100, 'gold': 50, 'position': [0, 0]}
        game_data = {'dungeon': dungeon, 'spieler': spieler}

        geladener_dungeon = game_data.get('dungeon')
        geladener_spieler = game_data.get('spieler')

        self.assertEqual(geladener_dungeon, [[0]], 'Dungeon wurde nicht korrekt aus game_data geladen')
        self.assertEqual(geladener_spieler['leben'], 100, 'Spielerleben stimmt nicht')
        self.assertEqual(geladener_spieler['gold'], 50, 'Spielergold stimmt nicht')
        self.assertEqual(geladener_spieler['position'], [0, 0], 'Spielerposition stimmt nicht')

    def test_start_position_und_werte(self):
        spieler = generate_player()
        self.assertEqual(spieler['position'], [0, 0], 'Spielerstartposition ist falsch')
        self.assertEqual(spieler['leben'], 100, 'Spielerleben beim Start ist falsch')
        self.assertEqual(spieler['gold'], 0, 'Spielergold beim Start ist falsch')

    @patch('builtins.print')
    def test_spieler_fehlt_element(self, mock_print):
        dungeon = {}
        spieler = {'leben': 100, 'gold': 0}
        game_data = {'dungeon': dungeon, 'spieler': spieler}

        with self.assertRaises(ValueError):
            game(game_data)

    @patch('builtins.print')
    @patch('builtins.input', return_value = 'm')
    def test_spieler_hat_alle_elemente(self, mock_input, mock_print):
        dungeon = {}
        spieler = {'leben': 1, 'gold': 0, 'position': [0, 0]}
        game_data = {'dungeon': dungeon, 'spieler': spieler}

        result = game(game_data)

        mock_print.assert_any_call('Dungeon Karte:')
        mock_print.assert_any_call('Leben:', 1, 'Gold:', 0)

    @patch('builtins.print')
    @patch('Dungeon.views.game.bewegung_im_dungeon', return_value = 'Ende')
    @patch('builtins.input', return_value = 'o')
    def test_dungeon_verlassen(self, mock_input, mock_bewegung, mock_print):
        spieler = {'leben': 0, 'gold': 0, 'position': 0}
        game_data = {'dungeon': {}, 'spieler': spieler}

        self.assertEqual(game(game_data), 'end')
        mock_print.assert_any_call('Du hast den Dungeon verlassen.')

    @patch('builtins.print')
    @patch('Dungeon.views.game.bewegung_im_dungeon', return_value = 'Fehler')
    @patch('builtins.input', return_value = 'o')
    @patch('Dungeon.views.game.print_dungeon')
    def test_bewegung_nicht_erlaubt(self, mock_print_dungeon, mock_input, mock_bewegung, mock_print):
        dungeon = [[], []]
        spieler = {'leben': 1, 'gold': 1, 'position': 1}
        game_data = {'dungeon': dungeon, 'spieler': spieler}

        self.assertEqual(game(game_data), 'dungeon')
        mock_print.assert_any_call('Bewegung nicht erlaubt.')
