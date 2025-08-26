import unittest
from unittest.mock import patch, call

from Dungeon.views.menu_load import menu_load

class TestMenuLoad(unittest.TestCase):
    @patch("builtins.input", side_effect=["2", "x"])
    @patch("builtins.print")
    def test_prints(self, mock_print, mock_input):
        result = menu_load({})
        self.assertEqual(result, "menu_main")

        mock_print.assert_has_calls([
            call('________Hauptmenü________'),
            call(),
            call("X - Zurück zum Menü"),
            call(),
            call("Ungültige Eingabe! Gib entweder eine Zahl für das Laden eines Spielstandes ein "
                 "oder ein X um ins Hauptmenü zurückzukehren"),
            call('________Hauptmenü________'),
            call(),
            call("X - Zurück zum Menü"),
            call()
        ])


if __name__ == "__main__":
    unittest.main()