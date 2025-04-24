import os
import sys
import unittest
from unittest.mock import patch

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

    @patch('builtins.print')
    @patch('random.choice', side_effect=['S', 'S', 'S'])
    @patch('random.randint', side_effect=[5, 60, 30])
    def test_randint_ausserhalb_gold_range(self, mock_randint, mock_choice, mock_print):
        generate_dungeon(1, 3, gold_range=(10, 50))

        mock_print.assert_any_call('Goldwert außerhalb der Range!')
        self.assertEqual(mock_print.call_count, 2)

    @patch('builtins.print')
    @patch('random.choice', side_effect=['F', 'F', 'F'])
    @patch('random.randint', side_effect=[8, 50, 35])
    def test_randint_ausserhalb_damage_range(self, mock_randint, mock_choice, mock_print):
        generate_dungeon(1, 3, damage_range = (10, 40))

        mock_print.assert_any_call('Schadenswert außerhalb der Range!')
        self.assertEqual(mock_print.call_count, 2)