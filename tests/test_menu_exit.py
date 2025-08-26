import unittest
from unittest.mock import patch

from Dungeon.views.menu_exit import menu_exit


class TestMenuExit(unittest.TestCase):

    def setUp(self):
        self.game_data = {}

    @patch('Dungeon.views.menu_exit.ist_spiel_aktiv', return_value = True)
    @patch('builtins.input', return_value = 'n')
    def test_antwort_n_spiel_aktiv(self, mock_input, mock_ist_aktiv):
        result = menu_exit(self.game_data)
        self.assertEqual(result, 'dungeon')

    @patch('Dungeon.views.menu_exit.ist_spiel_aktiv', return_value = False)
    @patch('builtins.input', return_value = 'n')
    def test_antwort_n_spiel_nicht_aktiv(self, mock_input, mock_ist_aktiv):
        result = menu_exit(self.game_data)
        self.assertEqual(result, 'menu_main')

    @patch('builtins.input', return_value='j')
    @patch('builtins.print')
    def test_antwort_j_beendet_spiel(self, mock_print, mock_input):
        game_data = {}

        with self.assertRaises(SystemExit):
            menu_exit(game_data)

        mock_print.assert_called_with("Spiel wurde beendet.")



    @patch('builtins.input', return_value = 'x')
    @patch('builtins.print')
    def test_ungueltige_eingabe(self, mock_print, mock_input):
        result = menu_exit(self.game_data)
        self.assertEqual(result, 'menu_main')
        mock_print.assert_called_with("Ungültige Eingabe – bitte 'j' für Ja oder 'n' für Nein eingeben.")


if __name__ == '__main__':
    unittest.main()
