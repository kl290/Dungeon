import os
import random
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dungeon.generate_dungeon import generate_dungeon, startraum_init


class TestGenerateDungeon(unittest.TestCase):

    @patch('random.randint', side_effect = [42, 17])
    @patch('random.choice', side_effect = ['S', 'F', 'L'])
    @patch('Dungeon.generate_dungeon.startraum_init', return_value = None)
    def test_dungeon_generierung_mit_mock(self, mock_startraum_init, mock_choice, mock_randint):
        dungeon = generate_dungeon(1, 3, gold_range = (30, 50), damage_range = (10, 40))

        testfaelle1 = {0: {0: {'besucht': False, 'gold': 42, 'raumtyp': 'S'},
                           1: {'besucht': False, 'raumtyp': 'F', 'schaden': 17},
                           2: {'besucht': False, 'raumtyp': 'L'}}}

        self.assertEqual(testfaelle1, dungeon)

        mock_startraum_init.assert_called_once()

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

    @patch('random.choice', wraps = random.choice)
    def test_raum_hat_nur_korrekte_raumtypen(self, spy_choice):
        dungeon = generate_dungeon(5, 5)

        spy_choice.assert_any_call(['F', 'S', 'L'])

        for row in dungeon.values():
            for room in row.values():
                raumtyp = room['raumtyp']
                self.assertIn(raumtyp, ['F', 'S', 'L'])

    def test_startraum_wird_korrekt_initialisiert(self):
        dungeon1 = {
            0: {
                0: {},
                1: {'key01': 'value'}
            },
            1: {
                0: {'key10': 'value'},
                1: {'key11': 'value'}
            }
        }
        startraum_init(dungeon1)

        self.assertEqual(dungeon1[0][0], {'raumtyp': 'L', 'besucht': True})
        self.assertEqual(dungeon1[0][1], {'key01': 'value'})
        self.assertEqual(dungeon1[1][0], {'key10': 'value'})
        self.assertEqual(dungeon1[1][1], {'key11': 'value'})

        dungeon2 = {
            0: {
                0: {},
                1: {'key01': 'value'},
                2: {'key02': 'value'},
                3: {'key03': 'value'},
                4: {'key04': 'value'}
            }
        }
        startraum_init(dungeon2)
        self.assertEqual(dungeon2[0][0], {'raumtyp': 'L', 'besucht': True})
        self.assertEqual(dungeon2[0][1], {'key01': 'value'})
        self.assertEqual(dungeon2[0][2], {'key02': 'value'})
        self.assertEqual(dungeon2[0][3], {'key03': 'value'})
        self.assertEqual(dungeon2[0][4], {'key04': 'value'})

        dungeon3 = {
            0: {
                0: {},
                1: {'key01': 'value'}
            },
            1: {
                0: {'key10': 'value'},
                1: {'key11': 'value'}
            },
            2: {
                0: {'key20': 'value'},
                1: {'key21': 'value'}
            }
        }
        startraum_init(dungeon3)
        self.assertEqual(dungeon3[0][0], {'raumtyp': 'L', 'besucht': True})
        self.assertEqual(dungeon3[0][1], {'key01': 'value'})
        self.assertEqual(dungeon3[1][0], {'key10': 'value'})
        self.assertEqual(dungeon3[1][1], {'key11': 'value'})
        self.assertEqual(dungeon3[2][0], {'key20': 'value'})
        self.assertEqual(dungeon3[2][1], {'key21': 'value'})
