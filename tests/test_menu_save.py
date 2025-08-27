import unittest
from unittest.mock import patch, call

from Dungeon.views.menu_save import menu_save


class TestMenuSave(unittest.TestCase):

    @patch('Dungeon.views.menu_save.ist_spiel_aktiv', return_value = True)
    @patch('builtins.input', return_value = '')
    @patch('builtins.print')
    def test_kein_name(self, mock_print, mock_input, mock_ist):
        result = menu_save(game_data = {})
        self.assertEqual(result, 'menu_main')
        mock_print.assert_has_calls([
            call('=== Spielstand speichern ==='),
            call('Kein Name eingegeben – zurück ins Hauptmenü.')
        ])

    @patch('Dungeon.views.menu_save.ist_spiel_aktiv', return_value = True)
    @patch('builtins.input', return_value = 'Test1')
    @patch('builtins.print')
    def test_mit_name(self, mock_print, mock_input, mock_ist):
        result = menu_save(game_data = {})
        self.assertEqual(result, 'menu_main')
        mock_print.assert_has_calls([
            call('=== Spielstand speichern ==='),
            call("Spielstand 'Test1' wurde gespeichert!")
        ])

    @patch('Dungeon.views.menu_save.ist_spiel_aktiv', return_value = False)
    @patch('builtins.print')
    def test_kein_aktives_Spiel(self, mock_print, mock_ist):
        result = menu_save(game_data = {})
        self.assertEqual(result, 'menu_main')
        mock_print.assert_called_with('Kein aktives Spiel zum Speichern.')


if __name__ == '__main__':
    unittest.main()
