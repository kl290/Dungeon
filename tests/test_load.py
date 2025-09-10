import pickle
import unittest
from unittest.mock import mock_open, patch

from Dungeon.load import load


class TestLoad(unittest.TestCase):

    @patch("builtins.open", new_callable = mock_open, read_data = pickle.dumps({}))
    @patch("os.path.exists", return_value = True)
    def test_lade_existierende_datei(self, mock_exists, mock_file):
        game_data = {}
        files = ["test.kl"]
        result = load(files, 1, game_data)

        self.assertEqual(result, 'dungeon')
        self.assertEqual(game_data, {})
        mock_exists.assert_called_once()
        mock_file.assert_called_once()

    @patch("builtins.open")
    @patch("os.path.exists")
    def test_invalider_index(self, mock_open, mock_exists):
        game_data = {}
        files = ["test.kl"]
        result = load(files, 2, game_data)

        self.assertEqual(result, 'menu_main')

        mock_open.assert_not_called()
        mock_exists.assert_not_called()

    @patch("builtins.print")
    @patch("os.path.exists", return_value = True)
    def test_datei_falsche_endung(self, mock_exists, mock_print):
        game_data = {}
        files = ["save.txt"]
        result = load(files, 1, game_data)

        mock_print.assert_any_call("Die Datei 'save.txt' kann nicht geöffnet werden: falsche Endung!")

        self.assertEqual(result, 'menu_main')


if __name__ == "__main__":
    unittest.main()
