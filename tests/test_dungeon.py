import unittest
from random import randint
from unittest.mock import patch, call

from Dungeon.bewegung_im_dungeon import bewegung_im_dungeon
from Dungeon.dungeon import main_dungeon, generate_player
from Dungeon.generate_dungeon import generate_dungeon
from Dungeon.print_dungeon import print_dungeon
from Dungeon.zug_verarbeiten import zug_verarbeiten


class TestMainDungeon(unittest.TestCase):

    @patch('builtins.input', side_effect = ['s', 'q'])
    @patch('Dungeon.dungeon.zug_verarbeiten', wraps = zug_verarbeiten)
    @patch('Dungeon.dungeon.bewegung_im_dungeon', wraps = bewegung_im_dungeon)
    @patch('Dungeon.dungeon.print_dungeon', wraps = print_dungeon)
    @patch('Dungeon.dungeon.generate_dungeon', wraps = generate_dungeon)
    def test_dungeon_ablauf(self, spy_generate, spy_print, spy_bewegung, spy_zug, mock_input):
        main_dungeon()

        spy_generate.assert_called_once()
        spy_generate.assert_called_once_with(5, 5)

        self.assertEqual(spy_print.call_count, 2)

        spy_bewegung.assert_called_once()

        spy_zug.assert_called_once()

    @patch('builtins.input', return_value = 'q')
    @patch('builtins.print')
    @patch('Dungeon.dungeon.print_dungeon', return_value = None)
    def test_print_begruessung(self, mock_print_dungeon, mock_print, mock_input):
        main_dungeon()

        mock_print.assert_has_calls([
            call('Willkommen im Dungeon-Abenteuer!'),
            call('Du befindest dich vor dem Eingang eines Dungeons.'),
            call(),
            call('Dungeon Karte:'),
            call('Leben:', 100, 'Gold:', 0),
            call('Du hast den Dungeon verlassen.')

        ])

    @patch('builtins.input', return_value = 'q')
    @patch('builtins.print')
    @patch('Dungeon.dungeon.generate_player', return_value = {
        'leben': 12345,
        'gold': 54321,
        'position': [0, 0]
    })
    def test_print_spielerdaten(self, mock_generate, mock_print, mock_input):
        main_dungeon()

        mock_print.assert_has_calls([call('Leben:', 12345, 'Gold:', 54321)])

    @patch('builtins.input', side_effect = ['q'])
    def test_prompt(self, mock_input):
        main_dungeon()

        mock_input.assert_has_calls([call(
            'Wohin möchtest du gehen? (Osten = O, Westen = W, Süden = S, Norden = N, Q zum Beenden): ')])

    @patch('Dungeon.dungeon.zug_verarbeiten')
    @patch('Dungeon.dungeon.bewegung_im_dungeon', return_value = 'Erfolg')
    @patch('builtins.input', return_value = 's')
    @patch('builtins.print')
    def test_game_over(self, mock_print, mock_input, mock_bewegung, mock_zug):
        def spieler_stirbt(_, spieler):
            spieler['leben'] = 0

        mock_zug.side_effect = spieler_stirbt

        main_dungeon()

        mock_bewegung.assert_called_once()
        mock_print.assert_has_calls([call('Game Over! Du bist gestorben.')])

    @patch('Dungeon.dungeon.bewegung_im_dungeon', return_value = 'Fehler')
    @patch('builtins.input', side_effect = ['x', 'q'])
    @patch('builtins.print')
    def test_bewegung_nicht_erlaubt(self, mock_print, mock_input, mock_bewegung):
        main_dungeon()

        mock_bewegung.assert_called_once()
        mock_print.assert_has_calls([call('Bewegung nicht erlaubt.')])

    @patch('builtins.input', return_value = None)
    @patch('builtins.print')
    @patch('Dungeon.dungeon.generate_dungeon', return_value = [[{}, {}], [{}, {}]])
    @patch('Dungeon.dungeon.bewegung_im_dungeon', return_value = 'Fehler')
    @patch('Dungeon.dungeon.generate_player')
    @patch('Dungeon.dungeon.print_dungeon', return_value = None)
    def test_print_ausgabe_bei_sieg(self, print_dungeon_mock, mock_player, mock_zug, mock_generate_dungeon, mock_print,
            mock_input):
        gold = randint(0, 10)
        mock_player.return_value = {'leben': 100, 'gold': gold, 'position': [1, 1]}

        main_dungeon()

        mock_print.assert_called_with('Sieg! Du hast den Dungeon erfolgreich mit', gold, 'Gold verlassen.')

    def test_start_position(self):
        spieler = generate_player()
        self.assertEqual(spieler["position"], [0, 0])


if __name__ == '__main__':
    unittest.main()
