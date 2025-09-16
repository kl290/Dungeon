import unittest
from unittest.mock import patch

from Dungeon.views.menu_zurueck import menu_zurueck


class TestMenuZurueck(unittest.TestCase):

    def test_spiel_aktiv(self):
        game_data = {
            'spieler': {'position': [1, 0]},
            'dungeon': [[{}, {}], [{}, {}]]
        }
        result = menu_zurueck(game_data)
        self.assertEqual(result, 'dungeon')

    @patch('builtins.print')
    def test_spiel_nicht_aktiv(self, mock_print):
        game_data = {}
        result = menu_zurueck(game_data)
        self.assertEqual(result, 'menu_main')
        mock_print.assert_called_once_with('Kein Spiel aktiv. Du kannst nicht zurückkehren.')
