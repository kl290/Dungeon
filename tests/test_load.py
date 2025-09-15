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
    def test_invalider_index(self, mock_open1, mock_exists):
        game_data = {}
        files = ["test.kl"]
        result = load(files, 2, game_data)

        self.assertEqual(result, 'menu_main')

        mock_open1.assert_not_called()
        mock_exists.assert_not_called()

    @patch("builtins.print")
    @patch("os.path.exists", return_value = True)
    def test_datei_falsche_endung(self, mock_exists, mock_print):
        game_data = {}
        files = ["save.txt"]
        result = load(files, 1, game_data)

        mock_print.assert_any_call("Die Datei 'save.txt' kann nicht geöffnet werden: falsche Endung!")

        self.assertEqual(result, 'menu_main')

    @patch("builtins.print")
    @patch("os.path.exists", return_value = False)
    def test_dateipfad_existiert_nicht(self, mock_print, mock_exists):
        dateien = ["savegame.kl"]
        eingabe = "1"
        game_data = {}

        result = load(dateien, eingabe, game_data)

        self.assertEqual(result, "menu_main")
        mock_exists.assert_called()

    @patch("builtins.print")
    def test_load_value_error(self, mock_print):
        dateien = ["savegame.kl"]
        eingabe = "abc"
        game_data = {}

        result = load(dateien, eingabe, game_data)

        self.assertEqual(result, "menu_main")

        mock_print.assert_called_with("Ungültige Eingabe! Bitte eine Zahl eingeben.")

    @patch("builtins.print")
    @patch("os.path.exists", return_value = True)
    @patch("builtins.open", side_effect = Exception("Dateifehler"))
    def test_load_exception(self, mock_op, mock_exists, mock_print):
        dateien = ["savegame.kl"]
        eingabe = "1"
        game_data = {}

        result = load(dateien, eingabe, game_data)

        self.assertEqual(result, "menu_main")

        mock_print.assert_called_with("Fehler beim Laden des Spielstands: Dateifehler")


if __name__ == "__main__":
    unittest.main()
