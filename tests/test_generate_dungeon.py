import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dungeon.generate_dungeon import generate_dungeon, Raumtypen


class TestGenerateDungeon(unittest.TestCase):

    @patch('random.randint', side_effect = [42, 17])
    @patch('random.choice', side_effect = ['S', 'F', 'L'])
    def test_dungeon_generierung_mit_mock(self, mock_choice, mock_randint):
        dungeon = generate_dungeon(1, 3, gold_range = (30, 50), damage_range = (10, 40))

        testfaelle1 = {0: {0: {'besucht': False, 'gold': 42, 'raumtyp': 'S'},
                           1: {'besucht': False, 'raumtyp': 'F', 'schaden': 17},
                           2: {'besucht': False, 'raumtyp': 'L'}}}

        self.assertEqual(dungeon, testfaelle1)

    def test_spielfeld_format(self):
        testfaelle = [
            (2, 2),
            (4, 2),
            (4, 7),
        ]

        for x, y in testfaelle:
            with self.subTest(zeilen = x, spalten = y):
                dungeon = generate_dungeon(x, y)
                self.assertEqual(len(dungeon), x, f'Dungeon sollte {x} Zeilen haben')
                for zeile in dungeon.values():
                    self.assertEqual(len(zeile), y, f'Jede Zeile sollte {y} Spalten haben')

    @patch('random.choice', side_effect = ['S', 'F', 'L', 'S', 'F', 'L', 'S', 'L', 'S'])
    @patch('random.randint', side_effect = [30, 15, 10, 50, 20, 25])
    def test_raum_hat_korrekte_attribute(self, mock_choice, mock_randint):
        dungeon = generate_dungeon(3, 3)

        testfaelle2 = {0: {0: {'besucht': False, 'gold': 30, 'raumtyp': 'S'},
                           1: {'besucht': False, 'raumtyp': 'F', 'schaden': 15},
                           2: {'besucht': False, 'raumtyp': 'L'}},
                       1: {0: {'besucht': False, 'gold': 10, 'raumtyp': 'S'},
                           1: {'besucht': False, 'raumtyp': 'F', 'schaden': 50},
                           2: {'besucht': False, 'raumtyp': 'L'}},
                       2: {0: {'besucht': False, 'gold': 20, 'raumtyp': 'S'},
                           1: {'besucht': False, 'raumtyp': 'L'},
                           2: {'besucht': False, 'gold': 25, 'raumtyp': 'S'}}}

        self.assertEqual(dungeon, testfaelle2)

        raumtypen = []

        for zeile in dungeon.values():
            for raum in zeile.values():
                typ = raum['raumtyp']
                self.assertIn(typ, Raumtypen, f'Ungültiger Raumtyp gefunden: {typ}')
                raumtypen.append(typ)

        print('Räume:', ' ', ' '.join(raumtypen))
