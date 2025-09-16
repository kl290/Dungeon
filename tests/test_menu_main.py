import unittest
from unittest.mock import patch

from Dungeon.views.menu_main import menu_main


class TestMenuMain(unittest.TestCase):

    @patch('Dungeon.views.menu_main.menu_new')
    @patch('builtins.input', return_value = '1')
    def test_wahl_neues_spiel(self, mock_input, mock_new):
        game_data = {}
        result = menu_main(game_data)
        mock_new.assert_called_once_with(game_data)

    @patch('Dungeon.views.menu_main.menu_load')
    @patch('builtins.input', return_value = '2')
    def test_wahl_laden(self, mock_input, mock_load):
        game_data = {}
        result = menu_main(game_data)
        mock_load.assert_called_once_with(game_data)

    @patch('Dungeon.views.menu_main.menu_save')
    @patch('builtins.input', return_value = '3')
    def test_wahl_speichern(self, mock_input, mock_save):
        game_data = {}
        result = menu_main(game_data)
        mock_save.assert_called_once_with(game_data)

    @patch('Dungeon.views.menu_main.menu_exit')
    @patch('builtins.input', return_value = '4')
    def test_wahl_beenden(self, mock_input, mock_exit):
        game_data = {}
        result = menu_main(game_data)
        mock_exit.assert_called_once_with(game_data)

    @patch('Dungeon.views.menu_main.menu_zurueck')
    @patch('builtins.input', return_value = 'x')
    def test_wahl_zurueck(self, mock_input, mock_zurueck):
        game_data = {}
        result = menu_main(game_data)
        mock_zurueck.assert_called_once_with(game_data)
