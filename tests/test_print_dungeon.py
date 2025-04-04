import os
import sys
import unittest
from unittest.mock import patch, call

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dungeon.generate_dungeon import generate_dungeon
from Dungeon.print_dungeon import print_dungeon


class TestPrintDungeon(unittest.TestCase):

    @patch("builtins.print")
    def test_eingang_position(self, mock_print):
        dungeon = generate_dungeon(5, 5)
        print_dungeon(dungeon, (-1, -1))
        erstes_zeichen = mock_print.call_args_list[0][0][0]
        self.assertEqual(erstes_zeichen, "E")

    @patch('builtins.print')
    def test_unbesuchte_raeume(self, mock_print):
        dungeon = generate_dungeon(2, 1)
        print_dungeon(dungeon, (-1, -1))
        assert mock_print.mock_calls == [
            call('E', end = '  '),
            call(),
            call('?', end = '  '),
            call()]

    @patch('builtins.print')
    def test_position_player_korrekt(self, mock_print):
        dungeon = generate_dungeon(2, 1)
        print_dungeon(dungeon, (1, 0))
        assert mock_print.mock_calls == [
            call('E', end = '  '),
            call(),
            call('P', end = '  '),

            call()]
