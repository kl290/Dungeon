import os
import sys
import unittest
from unittest.mock import patch, call

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dungeon.print_dungeon import print_dungeon


class TestPrintDungeon(unittest.TestCase):

    @patch('builtins.print')
    def test_print_dungeon_rooms(self, mock_print):
        tests = [
            [
                {
                    0: {0: {'raumtyp': 'L', 'besucht': False}, 1: {'raumtyp': 'F', 'besucht': True},
                        2: {'raumtyp': 'F', 'besucht': True}},
                    1: {0: {'raumtyp': 'F', 'besucht': True}, 1: {'raumtyp': 'S', 'besucht': True},
                        2: {'raumtyp': 'S', 'besucht': True}},
                    2: {0: {'raumtyp': 'S', 'besucht': False}, 1: {'raumtyp': 'L', 'besucht': True},
                        2: {'raumtyp': 'L', 'besucht': True}},
                },
                [
                    call('P', end = '  '), call('F', end = '  '), call('F', end = '  '),
                    call(),
                    call('F', end = '  '), call('S', end = '  '), call('S', end = '  '),
                    call(),
                    call('?', end = '  '), call('L', end = '  '), call('L', end = '  '),
                    call()
                ]
            ],
            [
                {
                    0: {0: {'raumtyp': 'L', 'besucht': False},
                        1: {'raumtyp': 'S', 'besucht': True}},
                    1: {0: {'raumtyp': 'L', 'besucht': True},
                        1: {'raumtyp': 'F', 'besucht': False}},
                    2: {0: {'raumtyp': 'L', 'besucht': False},
                        1: {'raumtyp': 'F', 'besucht': True}},
                },
                [
                    call('P', end = '  '),
                    call('S', end = '  '),
                    call(),
                    call('L', end = '  '),
                    call('?', end = '  '),
                    call(),
                    call('?', end = '  '),
                    call('F', end = '  '),
                    call()
                ]
            ]
        ]

        for dungeon, expected_calls in tests:
            mock_print.reset_mock()
            print_dungeon(dungeon, [0, 0])
            self.assertEqual(mock_print.mock_calls, expected_calls)

    @patch('builtins.print')
    def test_print_dungeon_spieler_position(self, mock_print):
        tests = [
            (
                {
                    0: {0: {'raumtyp': 'L', 'besucht': True},
                        1: {'raumtyp': 'S', 'besucht': True}},
                    1: {0: {'raumtyp': 'L', 'besucht': True},
                        1: {'raumtyp': 'F', 'besucht': False}},
                    2: {0: {'raumtyp': 'L', 'besucht': True},
                        1: {'raumtyp': 'F', 'besucht': True}},
                },
                [0, 0],
                [
                    call('P', end = '  '), call('S', end = '  '),
                    call(),
                    call('L', end = '  '), call('?', end = '  '),
                    call(),
                    call('L', end = '  '), call('F', end = '  '),
                    call()
                ]
            ),
            (
                {
                    0: {0: {'raumtyp': 'L', 'besucht': True},
                        1: {'raumtyp': 'S', 'besucht': True}},
                    1: {0: {'raumtyp': 'L', 'besucht': False},
                        1: {'raumtyp': 'L', 'besucht': True}},
                    2: {0: {'raumtyp': 'S', 'besucht': True},
                        1: {'raumtyp': 'L', 'besucht': False}},
                },
                [1, 1],
                [
                    call('L', end = '  '), call('S', end = '  '),
                    call(),
                    call('?', end = '  '), call('P', end = '  '),
                    call(),
                    call('S', end = '  '), call('?', end = '  '),
                    call()
                ]
            ),
            (
                {
                    0: {0: {'raumtyp': 'L', 'besucht': True},
                        1: {'raumtyp': 'F', 'besucht': True},
                        2: {'raumtyp': 'S', 'besucht': False},
                        3: {'raumtyp': 'F', 'besucht': False}},
                    1: {0: {'raumtyp': 'S', 'besucht': True},
                        1: {'raumtyp': 'L', 'besucht': False},
                        2: {'raumtyp': 'S', 'besucht': True},
                        3: {'raumtyp': 'F', 'besucht': False}},
                    2: {0: {'raumtyp': 'F', 'besucht': False},
                        1: {'raumtyp': 'F', 'besucht': False},
                        2: {'raumtyp': 'L', 'besucht': True},
                        3: {'raumtyp': 'S', 'besucht': True}},
                    3: {0: {'raumtyp': 'S', 'besucht': True},
                        1: {'raumtyp': 'L', 'besucht': True},
                        2: {'raumtyp': 'F', 'besucht': False},
                        3: {'raumtyp': 'S', 'besucht': False}},
                },
                [2, 3],
                [
                    call('L', end = '  '), call('F', end = '  '), call('?', end = '  '), call('?', end = '  '),
                    call(),
                    call('S', end = '  '), call('?', end = '  '), call('S', end = '  '), call('?', end = '  '),
                    call(),
                    call('?', end = '  '), call('?', end = '  '), call('L', end = '  '), call('S', end = '  '),
                    call(),
                    call('S', end = '  '), call('L', end = '  '), call('P', end = '  '), call('?', end = '  '),
                    call()
                ]
            )
        ]

        for dungeon, position, expected_calls in tests:
            mock_print.reset_mock()
            print_dungeon(dungeon, position)
            self.assertEqual(mock_print.mock_calls, expected_calls)
