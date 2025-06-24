import unittest
from unittest.mock import patch, call

from Dungeon.bewegung_im_dungeon import bewegung_im_dungeon
from Dungeon.dungeon import main_dungeon
from Dungeon.generate_dungeon import generate_dungeon
from Dungeon.print_dungeon import print_dungeon
from Dungeon.zug_verarbeiten import zug_verarbeiten


class TestMainDungeon(unittest.TestCase):

    @patch('builtins.input', side_effect = ['s', 'q'])
    @patch('Dungeon.dungeon.zug_verarbeiten', wraps = zug_verarbeiten)
    @patch('Dungeon.dungeon.bewegung_im_dungeon', wraps = bewegung_im_dungeon)
    @patch('Dungeon.dungeon.print_dungeon', wraps = print_dungeon)
    @patch('Dungeon.dungeon.generate_dungeon', wraps = generate_dungeon)
    def test_dungeon_flow(self, spy_generate, spy_print, spy_bewegung, spy_zug, mock_input):
        main_dungeon()

        self.assertEqual(spy_generate.call_count, 1)
        spy_generate.assert_called_once_with(5, 5)

        self.assertEqual(spy_print.call_count, 2)

        self.assertEqual(spy_bewegung.call_count, 1)

        self.assertEqual(spy_zug.call_count, 1)

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
    def test_print_spielerdaten(self, mock_print, mock_input):
        main_dungeon()

        self.assertIn(
            ('Leben:', 100, 'Gold:', 0),
            [call.args for call in mock_print.call_args_list]
        )

    @patch('builtins.input', side_effect = ['s', 'q'])
    def test_prompt(self, mock_input):
        main_dungeon()

        erwarteter_prompt = 'Wohin möchtest du gehen? (Osten = O, Westen = W, Süden = S, Norden = N, Q zum Beenden): '
        self.assertEqual(mock_input.call_args_list, [call(erwarteter_prompt), call(erwarteter_prompt)])

    @patch('Dungeon.dungeon.zug_verarbeiten', )
    @patch('Dungeon.dungeon.bewegung_im_dungeon', return_value = 'Erfolg')
    @patch('builtins.input', return_value = 's')
    @patch('builtins.print')
    def test_game_over(self, mock_print, mock_input, mock_bewegung, mock_zug):
        def spieler_stirbt(_, spieler):
            spieler['leben'] = 0

        mock_zug.side_effect = spieler_stirbt

        main_dungeon()

        self.assertEqual(mock_bewegung.call_count, 1)
        mock_print.assert_has_calls([call('Game Over! Du bist gestorben.')])

    @patch('Dungeon.dungeon.bewegung_im_dungeon', return_value = 'Ende')
    @patch('builtins.input', return_value = 's')
    @patch('builtins.print')
    def test_bewegung_ende(self, mock_print, mock_input, mock_bewegung):
        main_dungeon()

        self.assertEqual(mock_bewegung.call_count, 1)
        mock_print.assert_has_calls([call('Du hast den Dungeon verlassen.')])

    @patch('Dungeon.dungeon.bewegung_im_dungeon', return_value = 'Fehler')
    @patch('builtins.input', side_effect = ['x', 'q'])
    @patch('builtins.print')
    def test_bewegung_nicht_erlaubt(self, mock_print, mock_input, mock_bewegung):
        main_dungeon()

        self.assertEqual(mock_bewegung.call_count, 1)
        mock_print.assert_has_calls([call('Bewegung nicht erlaubt.')])

    if __name__ == '__main__':
        unittest.main()
