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
                [
                    [{'raumtyp': 'S', 'besucht': False}, {'raumtyp': 'F', 'besucht': True},
                     {'raumtyp': 'F', 'besucht': True}],
                    [{'raumtyp': 'F', 'besucht': True}, {'raumtyp': 'S', 'besucht': True},
                     {'raumtyp': 'S', 'besucht': True}]
                ],
                [
                    call('P', end = '  '), call('F', end = '  '), call('F', end = '  '),
                    call(),
                    call('F', end = '  '), call('S', end = '  '), call('S', end = '  '),
                    call()
                ]
            ],
            [
                [
                    [{'raumtyp': 'F', 'besucht': False}, {'raumtyp': 'S', 'besucht': True}],
                    [{'raumtyp': 'L', 'besucht': True}, {'raumtyp': 'F', 'besucht': False}]
                ],
                [
                    call('P', end = '  '),
                    call('S', end = '  '),
                    call(),
                    call('L', end = '  '),
                    call('?', end = '  '),
                    call()
                ]
            ]
        ]

        for test in tests:
            print_dungeon(test[0], {"x": 0, "y": 0})

            self.assertEqual(mock_print.mock_calls, test[1])

            mock_print.reset_mock()

    @patch('builtins.print')
    def test_print_dungeon_spieler_position(self, mock_print):
        tests = [
            [
                [
                    [{'raumtyp': '', 'besucht': False}, {'raumtyp': 'S', 'besucht': True}],
                    [{'raumtyp': 'L', 'besucht': True}, {'raumtyp': 'F', 'besucht': False}]
                ],
                {"x": 0, "y": 0},
                [
                    call('P', end = '  '), call('S', end = '  '),
                    call(),
                    call('L', end = '  '), call('?', end = '  '),
                    call()
                ]
            ],
            [
                [
                    [{'raumtyp': 'F', 'besucht': True}, {'raumtyp': 'S', 'besucht': True}],
                    [{'raumtyp': '', 'besucht': False}, {'raumtyp': 'L', 'besucht': True}]
                ],
                {"x": 1, "y": 1},
                [
                    call('E', end = '  '), call('S', end = '  '),
                    call(),
                    call('?', end = '  '), call('P', end = '  '),
                    call()
                ]
            ]
        ]

        for test in tests:
            print_dungeon(test[0], test[1])

            self.assertEqual(mock_print.mock_calls, test[2])
            
            mock_print.reset_mock()
