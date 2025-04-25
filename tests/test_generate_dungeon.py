import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dungeon.generate_dungeon import generate_dungeon


class TestGenerateDungeon(unittest.TestCase):

    @patch('random.randint')
    @patch('random.choice')
    def test_dungeon_generierung_mit_mock(self, mock_choice, mock_randint):

        mock_choice.side_effect = ['S', 'F', 'L']

        mock_randint.side_effect = [42, 17]

        dungeon = generate_dungeon(1, 3)

        testfaelle = {
            0: {
                0: {'raumtyp': 'S', 'gold': 42, 'besucht': False},
                1: {'raumtyp': 'F', 'schaden': 17, 'besucht': False},
                2: {'raumtyp': 'L', 'besucht': False}
            }
        }

        self.assertEqual(dungeon, testfaelle)

    def test_spielfeld_format(self):
        dungeon = generate_dungeon(5, 5)
        self.assertEqual(len(dungeon), 5)
        for row in dungeon.values():
            self.assertEqual(len(row), 5)

    def test_raum_hat_korrekte_attribute(self):
        dungeon = generate_dungeon(5, 5)
        for row in dungeon.values():
            for room in row.values():
                raumtyp = room['raumtyp']
                self.assertIn(raumtyp, ['F', 'S', 'L'])

    def test_zufaelligkeit_der_dungeon_generierung(self):
        dungeon1 = generate_dungeon(1, 1)
        dungeon2 = generate_dungeon(2, 2)

        self.assertNotEqual(dungeon1, dungeon2, "Zwei generierte Dungeons sind identisch – Zufälligkeit fehlt.")
