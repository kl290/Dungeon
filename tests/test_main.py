import os
import sys
import unittest
from unittest.mock import patch, call

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dungeon.main import main


class TestMainDungeon(unittest.TestCase):

    @patch('builtins.input', side_effect = ['1', 'm', '4', 'j'])
    @patch('builtins.print')
    def test_print_spielerdaten(self, mock_print, mock_input):
        main()

        mock_print.assert_has_calls([call('Leben:', 100, 'Gold:', 0)])

    @patch('builtins.input', side_effect = ['1', 'm', '4', 'j'])
    @patch('Dungeon.utils.ist_spiel_aktiv', return_value = False)
    def test_prompt(self, mock_ist_aktiv, mock_input):
        main()

        mock_input.assert_any_call(
            'Wohin möchtest du gehen? (M = Menü, Osten = O, Westen = W, Süden = S, Norden = N): ')

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

    @patch('builtins.input', side_effect = ['99', '4', 'j'])
    @patch('builtins.print')
    def test_ungueltige_eingabe_im_hauptmenu(self, mock_print, mock_input):
        main()

        mock_print.assert_has_calls(
            [call('Ungültige Eingabe.')])

    @patch('builtins.input', side_effect = ['x', '4', 'j'])
    @patch('builtins.print')
    def test_zurueck_zum_spiel_ohne_aktives_spiel(self, mock_print, mock_input):
        main()

        mock_print.assert_any_call('Kein Spiel aktiv. Du kannst nicht zurückkehren.')
