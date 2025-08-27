import os
import sys
import unittest
from unittest.mock import patch, call

from Dungeon.views.menu_new import initialisierung

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dungeon.views.menu_exit import menu_exit
from Dungeon.main import main
from Dungeon.generate_dungeon import generate_dungeon


class TestMainDungeon(unittest.TestCase):
    @patch('builtins.input', side_effect = ['1', 'm', '4', 'j'])
    @patch('Dungeon.views.menu_exit', wraps = menu_exit)
    @patch('Dungeon.views.menu_new.generate_dungeon', wraps = generate_dungeon)
    @patch('Dungeon.views.menu_new', return_value = True)
    @patch('Dungeon.views.menu_new.initialisierung', wraps = initialisierung)
    @patch('Dungeon.utils.ist_spiel_aktiv', return_Value = False)
    def test_dungeon_ablauf(self, mock_ist, mock_init, mock_new, mock_generate, mock_exit, mock_input):
        main()

    @patch('builtins.input', side_effect = ['1', 'm', '4', 'j'])
    @patch('builtins.print')
    def test_print_begruessung(self, mock_print, mock_input):
        main()
        mock_print.assert_has_calls([
            call(
                'Bereit für das ultimative Dungeon-Erlebnis? Dein Abenteuer startet hier!'),
            call(),
            call('________Hauptmenü________'),
            call('1 - Neues Spiel starten'),
            call('2 - Spielstand laden'),
            call('3 - Spiel speichern'),
            call('4 - Spiel beenden'),
            call('X - Zurück zum Spiel'),
            call(),
            call(),
            call('Dungeon Karte:'),
            call('P', end = '  '),
            call('?', end = '  '),
            call('?', end = '  '),
            call('?', end = '  '),
            call('?', end = '  '),
            call(),
            call('?', end = '  '),
            call('?', end = '  '),
            call('?', end = '  '),
            call('?', end = '  '),
            call('?', end = '  '),
            call(),
            call('?', end = '  '),
            call('?', end = '  '),
            call('?', end = '  '),
            call('?', end = '  '),
            call('?', end = '  '),
            call(),
            call('?', end = '  '),
            call('?', end = '  '),
            call('?', end = '  '),
            call('?', end = '  '),
            call('?', end = '  '),
            call(),
            call('?', end = '  '),
            call('?', end = '  '),
            call('?', end = '  '),
            call('?', end = '  '),
            call('?', end = '  '),
            call(),
            call('Leben:', 100, 'Gold:', 0),
            call(),
            call('________Hauptmenü________'),
            call('1 - Neues Spiel starten'),
            call('2 - Spielstand laden'),
            call('3 - Spiel speichern'),
            call('4 - Spiel beenden'),
            call('X - Zurück zum Spiel'),
            call(),
            call('Spiel wurde beendet.')
        ])

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


if __name__ == '__main__':
    unittest.main()
