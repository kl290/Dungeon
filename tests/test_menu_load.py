import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dungeon.views.menu_load import menu_load


class TestMenuLoad(unittest.TestCase):

    @patch('builtins.print')
    @patch('os.path.exists', return_value = False)
    def test_print_keine_spielstaende_existieren(self, mock_exists, mock_print):
        result = menu_load({})
        mock_print.assert_any_call('________Spielstände________')
        mock_print.assert_any_call('(Keine Spielstände vorhanden)')
        self.assertEqual(result, 'menu_main')

    @patch('os.listdir', return_value = [])
    def test_menu_load_ordner_leer(self, mock_listdir):
        result = menu_load({})
        self.assertEqual(result, 'menu_main')

    @patch('os.path.exists', return_value = True)
    @patch('os.listdir', return_value = ['save1.kl'])
    @patch('os.path.getctime', return_value = 0)
    @patch('builtins.input', return_value = '')
    def test_menu_load_eingabe_enter(self, mock_input, mock_getctime, mock_listdir, mock_exists):
        result = menu_load({})
        self.assertEqual(result, 'menu_main')

    @patch('Dungeon.views.menu_load.load')
    @patch('os.path.exists', return_value = True)
    @patch('os.listdir', return_value = ['save1.kl'])
    @patch('os.path.getctime', return_value = 0)
    @patch('builtins.input', return_value = '1')
    def test_menu_load_load_wird_aufgerufen(self, mock_input, mock_getctime, mock_listdir, mock_exists, mock_load):
        game_data = {}
        menu_load(game_data)
        mock_load.assert_called_once_with(['save1.kl'], '1', game_data)


if __name__ == '__main__':
    unittest.main()
