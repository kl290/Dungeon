import unittest
from unittest.mock import patch, call

from Dungeon.views.menu_save import menu_save


class TestMenuSave(unittest.TestCase):

    @patch('Dungeon.views.menu_save.ist_spiel_aktiv', return_value = True)
    @patch('builtins.input', return_value = '')
    @patch('builtins.print')
    def test_kein_name(self, mock_print, mock_input, mock_ist_spiel_aktiv):
        result = menu_save(game_data = {})
        self.assertEqual(result, 'menu_main')
        mock_print.assert_has_calls([
            call('________Spielstände________'),
            call('Kein Name eingegeben – zurück ins Hauptmenü.')
        ])

    @patch('Dungeon.views.menu_save.ist_spiel_aktiv', return_value = False)
    @patch('builtins.print')
    def test_kein_aktives_Spiel(self, mock_print, mock_ist_spiel_aktiv):
        result = menu_save(game_data = {})
        self.assertEqual(result, 'menu_main')
        mock_print.assert_called_with('Kein aktives Spiel zum Speichern.')

    @patch("Dungeon.views.menu_save.ist_spiel_aktiv", return_value = True)
    @patch("Dungeon.views.menu_save.save", return_value = None)
    @patch("builtins.input", return_value = "test")
    def test_aufruf_save(self, mock_input, mock_save, mock_ist_spiel_aktiv):
        result = menu_save(game_data = {})

        mock_save.assert_called()
