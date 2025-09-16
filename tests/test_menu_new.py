import unittest
from unittest.mock import patch

from Dungeon.views.menu_new import menu_new, initialisierung


class TestMenuNew(unittest.TestCase):

    def setUp(self):
        self.game_data = {}

    @patch('Dungeon.views.menu_new.initialisierung', wraps = initialisierung)
    @patch('Dungeon.views.menu_new.ist_spiel_aktiv', return_value = False)
    @patch('Dungeon.views.menu_new.validiere_dungeon', return_value = None)
    @patch('builtins.input', return_value = 'n')
    def test_n_eingabe(self, mock_input, mock_validiere_dungeon, mock_ist_spiel_aktiv, spy_initialisierung):
        result = menu_new(self.game_data)
        spy_initialisierung.assert_called_once_with(self.game_data)
        self.assertEqual(result, 'dungeon')

        mock_validiere_dungeon.assert_called_once()

    @patch('Dungeon.views.menu_new.ist_spiel_aktiv', return_value = True)
    @patch('Dungeon.views.menu_new.validiere_dungeon', return_value = None)
    @patch('builtins.input', return_value = 'j')
    def test_j_eingabe(self, mock_input, mock_validiere_dungeon, mock_ist_spiel_aktiv):
        result = menu_new(self.game_data)
        self.assertEqual(result, 'dungeon')

    @patch('Dungeon.views.menu_new.ist_spiel_aktiv', return_value = True)
    @patch('builtins.print')
    @patch('builtins.input', side_effect = ['x', 'n'])
    def test_ungueltige_eingabe(self, mock_input, mock_print, mock_ist_spiel_aktiv):
        result = menu_new(self.game_data)
        self.assertEqual(result, 'dungeon')
        mock_print.assert_any_call("Ungültige Eingabe – bitte 'j' für Ja oder 'n' für Nein eingeben.")

    @patch('Dungeon.views.menu_new.validiere_dungeon', return_value = None)
    def test_aufruf_dungeon_validierung(self, mock_validiere_dungeon):
        result = menu_new(self.game_data)
        self.assertEqual(result, 'dungeon')
        mock_validiere_dungeon.assert_called_once()
