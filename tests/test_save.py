import os
import unittest
from unittest.mock import patch, mock_open, call

from Dungeon.save import dateiname_aufteilen, neue_namensteile_bestimmen
from Dungeon.save import save, ORDNER_SPIELSTAENDE


class TestDateiname(unittest.TestCase):

    def test_dateiname_aufteilen(self):
        testfaelle = [
            ("Spiel.kl", "Spiel", None),
            ("Spiel (3).kl", "Spiel", "3"),
            ("Mein_Spiel (12).kl", "Mein_Spiel", "12"),
            ("Test-Spiel.kl", "Test-Spiel", None),
        ]

        for dateiname, erwarteter_name, erwartete_nummer in testfaelle:
            dateiname_match = dateiname_aufteilen(dateiname)
            self.assertEqual(dateiname_match.group(1), erwarteter_name)
            self.assertEqual(dateiname_match.group(3), erwartete_nummer)

    def test_namensteile_bestimmen(self):
        testfaelle = [
            ("Spiel.kl", "Spiel", 1),
            ("Spiel (5).kl", "Spiel", 6),
            ("Mein_Spiel (12).kl", "Mein_Spiel", 13),
            ("Test-Spiel.kl", "Test-Spiel", 1),
        ]

        for dateiname, erwarteter_name, erwartete_nummer in testfaelle:
            name, nummer = neue_namensteile_bestimmen(dateiname)
            self.assertEqual(name, erwarteter_name)
            self.assertEqual(nummer, erwartete_nummer)

    @patch("builtins.open")
    @patch("os.makedirs")
    def test_datei_erstellen_v1(self, mock_ordner, mock_datei):
        game_data = {}
        result = save(game_data, "Test")
        mock_ordner.assert_called_once_with(ORDNER_SPIELSTAENDE, exist_ok = True)
        mock_datei.assert_called_once_with(os.path.join(ORDNER_SPIELSTAENDE, "Test.kl"), "xb")
        self.assertEqual(result, "menu_main")

    @patch("builtins.open")
    @patch("os.makedirs")
    def test_datei_erstellen_v2(self, mock_ordner, mock_datei):
        game_data = {}
        result = save(game_data, "Test.lc")
        mock_ordner.assert_called_once_with(ORDNER_SPIELSTAENDE, exist_ok = True)
        mock_datei.assert_called_once_with(os.path.join(ORDNER_SPIELSTAENDE, "Test.lc.kl"), "xb")
        self.assertEqual(result, "menu_main")

    @patch("builtins.open")
    @patch("os.makedirs")
    def test_pkl(self, mock_ordner_erstellen, mock_datei_oeffnen):
        game_data = {}
        result = save(game_data, "Test")
        mock_datei_oeffnen.assert_called_once_with(os.path.join(ORDNER_SPIELSTAENDE, "Test.kl"), "xb")
        self.assertEqual(result, "menu_main")

    @patch("os.path.exists", side_effect = [False, True])
    @patch("Dungeon.save.neue_namensteile_bestimmen", return_value = ("Spiel", 1))
    @patch("builtins.open", side_effect = [FileExistsError, mock_open().return_value])
    @patch("os.makedirs")
    def test_datei_existiert_ruft_save_mit_neuem_namen_auf(self, mock_makedirs, mock_op, mock_namensteile, mock_path):
        game_data = {}

        result = save(game_data, "Spiel.kl")

        self.assertEqual(mock_op.call_count, 2)
        mock_op.assert_has_calls([
            call(os.path.join(ORDNER_SPIELSTAENDE, "Spiel.kl"), "xb"),
            call(os.path.join(ORDNER_SPIELSTAENDE, "Spiel (1).kl"), "xb")
        ])
        self.assertEqual(result, "menu_main")
        mock_namensteile.assert_called_once()
        mock_makedirs.assert_called_once_with(ORDNER_SPIELSTAENDE, exist_ok = True)
