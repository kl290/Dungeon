import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dungeon import validiere_spieler_objekt, validiere_dungeon, ist_valider_spieler


class TestDungeon(unittest.TestCase):

    @patch('Dungeon.ist_valider_spieler', return_value = True)
    def test_mit_validem_spieler_objekt(self, mock_ist_valider_spieler):
        validiere_spieler_objekt({})
        mock_ist_valider_spieler.assert_called()

    @patch('Dungeon.ist_valider_spieler', return_value = False)
    def test_mit_invalidem_spieler_objekt(self, mock_ist_valider_spieler):
        with self.assertRaises(ValueError) as contextManager:
            validiere_spieler_objekt({})
        mock_ist_valider_spieler.assert_called()
        self.assertEqual(contextManager.exception.args[0], "Es müssen alle Elemente des Spielers übergeben werden!")

    def test_valider_spieler(self):
        spieler = {'leben': 1, 'gold': 1, 'position': 1}
        ist_valider_spieler(spieler)

    def test_invalider_spieler(self):
        fehlerhafte_spieler = [
            {},
            {'leben': 1},
            {'gold': 1},
            {'position': 1},
            {'Schaden': 100, 'Start': [1]},
            {'leben': 100, 'Start': [1], 'position': [1], 'zusatz_gold': 100000},
            {'leben': 100, 'position': [1]},
            {'gold': 0, 'position': [1]},
            {'leben': 100, 'gold': 0},
            [{'leben': 100}, {'gold': 0}, {'position': [1]}]
        ]

        for spieler in fehlerhafte_spieler:
            self.assertFalse(ist_valider_spieler(spieler))

    def test_dungeon_korrekt_validiert(self):
        dungeon_korrekt = {
            0: {0: {'raumtyp': 'L', 'besucht': True},
                1: {'raumtyp': 'F', 'besucht': False}},
            1: {0: {'raumtyp': 'S', 'besucht': False},
                1: {'raumtyp': 'L', 'besucht': True}}
        }
        validiere_dungeon(dungeon_korrekt)

    def test_dungeon_falsch_validiert(self):
        dungeon_falsch_v1 = {0: {0: {'raumtyp': 'X', 'besucht': True}}}
        with self.assertRaises(ValueError) as contextManager:
            validiere_dungeon(dungeon_falsch_v1)
        self.assertEqual(contextManager.exception.args[0], "Dungeon enthält ungültige Räume!")

        dungeon_falsch_v2 = {0: {0: {'raumtyp': 'L', 'besucht': None}}}
        with self.assertRaises(ValueError) as contextManager:
            validiere_dungeon(dungeon_falsch_v2)
        self.assertEqual(contextManager.exception.args[0], "Raum 'besucht' muss True oder False sein!")
