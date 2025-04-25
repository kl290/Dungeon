import os
import random
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dungeon.zug_verarbeiten import zug_verarbeiten


class TestZugVerarbeiten(unittest.TestCase):

    def setUp(self):
        self.spieler = {'position': (1, 0), 'gold': 10, 'leben': 100}

    @patch('builtins.print')
    def test_besuchter_raum(self, mock_print):
        dungeon = [
            [{'raumtyp': 'S', 'gold': 10, 'besucht': True}, {'raumtyp': 'S', 'gold': 30, 'besucht': False}],
            [{'raumtyp': 'L', 'besucht': False}, {'raumtyp': 'F', 'schaden': 10, 'besucht': False}]
        ]

        self.spieler['position'] = (0, 0)
        zug_verarbeiten(dungeon, self.spieler)

        self.assertEqual(self.spieler['gold'], 10)
        self.assertEqual(self.spieler['leben'], 100)

    @patch('builtins.print')
    def test_schatzraum(self, mock_print):
        gold = random.randint(10, 50)
        schaden = random.randint(10, 50)
        dungeon = [
            [{'raumtyp': 'F', 'schaden': schaden, 'besucht': False}, {'raumtyp': 'S', 'gold': gold, 'besucht': False}],
            [{'raumtyp': 'S', 'gold': gold, 'besucht': False}, {'raumtyp': 'S', 'gold': gold, 'besucht': False}]
        ]
        zug_verarbeiten(dungeon, self.spieler)
        self.assertEqual(self.spieler['gold'], 10 + gold)
        self.assertTrue(dungeon[0][1]['besucht'])
        mock_print.assert_called_with('Du hast', gold, 'Gold gefunden!')

    @patch('builtins.print')
    def test_fallenraum(self, mock_print):
        gold = random.randint(10, 50)
        schaden = random.randint(10, 50)
        dungeon = [
            [{'raumtyp': 'F', 'schaden': schaden, 'besucht': False},
             {'raumtyp': 'F', 'schaden': schaden, 'besucht': False}],
            [{'raumtyp': 'S', 'gold': gold, 'besucht': False}, {'raumtyp': 'F', 'schaden': schaden, 'besucht': False}]
        ]
        zug_verarbeiten(dungeon, self.spieler)
        self.assertEqual(self.spieler['leben'], 100 - schaden)
        self.assertTrue(dungeon[0][1]['besucht'])
        mock_print.assert_called_with('Du bist in eine Falle getreten und hast', schaden, 'Schaden genommen!')

    @patch('builtins.print')
    def test_leerraum(self, mock_print):
        gold = random.randint(10, 50)
        schaden = random.randint(10, 50)
        dungeon = [
            [{'raumtyp': 'F', 'schaden': schaden, 'besucht': False}, {'raumtyp': 'L', 'besucht': False}],
            [{'raumtyp': 'S', 'gold': gold, 'besucht': False}, {'raumtyp': 'F', 'schaden': schaden, 'besucht': False}]
        ]
        zug_verarbeiten(dungeon, self.spieler)
        self.assertTrue(dungeon[0][1]['besucht'])
        mock_print.assert_called_with('Der Raum ist leer.')
