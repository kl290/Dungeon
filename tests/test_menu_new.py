import unittest
from unittest.mock import patch
from Dungeon.views.menu_new import menu_new

class TestMenuNew(unittest.TestCase):

    def setUp(self):
        self.game_data = {}

    @patch('Dungeon.views.menu_new.ist_spiel_aktiv', return_value=True)
    @patch('builtins.input', return_value='n')
    def test_n_eingabe(self, mock_input, mock_ist):
        result = menu_new(self.game_data)
        self.assertEqual(result, 'dungeon')

    @patch('Dungeon.views.menu_new.ist_spiel_aktiv', return_value=True)
    @patch('builtins.input', return_value='j')
    def test_j_eingabe(self, mock_input, mock_ist):
        result = menu_new(self.game_data)
        self.assertEqual(result, 'dungeon')

    @patch('Dungeon.views.menu_new.ist_spiel_aktiv', return_value=True)
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['x', 'n'])
    def test_ungueltige_eingabe(self, mock_input, mock_print, mock_ist):
        result = menu_new(self.game_data)
        self.assertEqual(result, 'dungeon')
        mock_print.assert_any_call("Ungültige Eingabe – bitte 'j' für Ja oder 'n' für Nein eingeben.")

    @patch('Dungeon.utils.ist_spiel_aktiv', return_value=False)
    def test_spiel_nicht_aktiv(self, mock_ist):
        result = menu_new(self.game_data)
        self.assertEqual(result, 'dungeon')


if __name__ == '__main__':
    unittest.main()
