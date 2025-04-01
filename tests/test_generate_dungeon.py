import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dungeon.generate_dungeon import generate_dungeon


class TestGenerateDungeon(unittest.TestCase):

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
        for _ in range(0, 10):
            dungeon1 = generate_dungeon(5, 5)
            dungeon2 = generate_dungeon(5, 5)
            if dungeon1 != dungeon2:
                return
        self.fail('Keine Unterschiede generiert')
