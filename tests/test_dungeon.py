import unittest
from random import randint
from unittest.mock import patch, call

from Dungeon.bewegung_im_dungeon import bewegung_im_dungeon
from Dungeon.dungeon import exit_game
from Dungeon.dungeon import main_dungeon
from Dungeon.generate_dungeon import generate_dungeon
from Dungeon.print_dungeon import print_dungeon
from Dungeon.zug_verarbeiten import zug_verarbeiten


class TestMainDungeon(unittest.TestCase):
    @patch('sys.exit', side_effect = SystemExit)
    @patch('Dungeon.dungeon.exit_game', wraps = exit_game)
    @patch('Dungeon.dungeon.generate_dungeon', wraps = generate_dungeon)
    @patch('Dungeon.dungeon.print_dungeon', wraps = print_dungeon)
    @patch('Dungeon.dungeon.bewegung_im_dungeon', wraps = bewegung_im_dungeon)
    @patch('Dungeon.dungeon.zug_verarbeiten', wraps = zug_verarbeiten)
    @patch('builtins.input', side_effect = ['1', 's', 'm', '4', 'j'])
    @patch('Dungeon.dungeon.ist_spiel_aktiv', return_value = True)
    def test_dungeon_ablauf(self, mock_ist, mock_input, mock_zug, mock_bewegung, mock_print, mock_generate, mock_exit,
            mock_sys_exit):
        with self.assertRaises(SystemExit):
            main_dungeon()

    @patch('sys.exit', side_effect = SystemExit)
    @patch('builtins.input', side_effect = ['4', 'j'])
    @patch('builtins.print')
    def test_print_begruessung(self, mock_print, mock_input, mock_sys_exit):
        with self.assertRaises(SystemExit):
            main_dungeon()

        mock_print.assert_has_calls([
            call('Bereit für das ultimative Dungeon-Erlebnis? Dein Abenteuer startet hier!'),
            call(),
            call('________Hauptmenü________'),
            call('1 - Neues Spiel starten'),
            call('2 - Spielstand laden'),
            call('3 - Spiel speichern'),
            call('4 - Spiel beenden'),
            call('X - Zurück zum Spiel'),
            call(),
            call('Spiel wird beendet.')

        ])

    @patch('sys.exit', side_effect = SystemExit)
    @patch('builtins.input', side_effect = ['1', 'm', '4', 'j'])
    @patch('builtins.print')
    def test_print_spielerdaten(self, mock_print, mock_input, mock_sys_exit):
        with self.assertRaises(SystemExit):
            main_dungeon()

            mock_print.assert_has_calls([call('Leben:', 100, 'Gold:', 0)])

    @patch('sys.exit', side_effect = SystemExit)
    @patch('builtins.input', side_effect = ['1', 'm', '4', 'j'])
    @patch('builtins.print')
    def test_prompt(self, mock_print, mock_input, mock_sys_exit):
        with self.assertRaises(SystemExit):
            main_dungeon()

            mock_print.assert_has_calls(
                [call('Wohin möchtest du gehen? (M = Menü, Osten = O, Westen = W, Süden = S, Norden = N): ')])

    @patch('Dungeon.dungeon.zug_verarbeiten')
    @patch('Dungeon.dungeon.bewegung_im_dungeon', return_value = 'Erfolg')
    @patch('builtins.input', side_effect = ['1', 's'])
    @patch('builtins.print')
    def test_game_over(self, mock_print, mock_input, mock_bewegung, mock_zug):
        def spieler_stirbt(_, spieler):
            spieler['leben'] = 0

        mock_zug.side_effect = spieler_stirbt
        main_dungeon()

        mock_bewegung.assert_called_once()
        mock_print.assert_has_calls([call('Game Over! Du bist gestorben.')])

    @patch('builtins.input', side_effect = ['1', ''])
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


if __name__ == '__main__':
    unittest.main()
