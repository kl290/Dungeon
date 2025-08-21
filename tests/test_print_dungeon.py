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
                     {'raumtyp': 'S', 'besucht': True}],
                    [{'raumtyp': 'S', 'besucht': False}, {'raumtyp': 'L', 'besucht': True},
                     {'raumtyp': 'L', 'besucht': True}],
                ],
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
                [
                    [{'raumtyp': 'F', 'besucht': False}, {'raumtyp': 'S', 'besucht': True}],
                    [{'raumtyp': 'L', 'besucht': True}, {'raumtyp': 'F', 'besucht': False}],
                    [{'raumtyp': 'L', 'besucht': False}, {'raumtyp': 'F', 'besucht': True}],
                ],
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

        for test in tests:
            print_dungeon(test[0], [0, 0])

            self.assertEqual(mock_print.mock_calls, test[1])

            mock_print.reset_mock()

    @patch('builtins.print')
    def test_print_dungeon_spieler_position(self, mock_print):
        tests = [
            [
                [
                    [{'raumtyp': '', 'besucht': False}, {'raumtyp': 'S', 'besucht': True}],
                    [{'raumtyp': 'L', 'besucht': True}, {'raumtyp': 'F', 'besucht': False}],
                    [{'raumtyp': 'L', 'besucht': True}, {'raumtyp': 'F', 'besucht': True}],
                ],
                [0, 0],
                [
                    call('P', end = '  '), call('S', end = '  '),
                    call(),
                    call('L', end = '  '), call('?', end = '  '),
                    call(),
                    call('L', end = '  '), call('F', end = '  '),
                    call()
                ]
            ],
            [
                [
                    [{'raumtyp': 'F', 'besucht': True}, {'raumtyp': 'S', 'besucht': True}],
                    [{'raumtyp': 'L', 'besucht': False}, {'raumtyp': 'L', 'besucht': True}],
                    [{'raumtyp': 'S', 'besucht': True}, {'raumtyp': 'L', 'besucht': False}],
                ],
                [1, 1],
                [
                    call('F', end = '  '), call('S', end = '  '),
                    call(),
                    call('?', end = '  '), call('P', end = '  '),
                    call(),
                    call('S', end = '  '), call('?', end = '  '),
                    call()
                ]
            ],
            # Test mit größerem Dungeon (4x4), um x/y-Verwechslung zu erkennen
            [
                [
                    [{'raumtyp': 'S', 'besucht': False}, {'raumtyp': 'F', 'besucht': True},
                     {'raumtyp': 'S', 'besucht': False}, {'raumtyp': 'F', 'besucht': False}],
                    [{'raumtyp': 'S', 'besucht': True}, {'raumtyp': 'L', 'besucht': False},
                     {'raumtyp': 'S', 'besucht': True},
                     {'raumtyp': 'F', 'besucht': False}],
                    [{'raumtyp': 'F', 'besucht': False}, {'raumtyp': 'F', 'besucht': False},
                     {'raumtyp': 'L', 'besucht': True},
                     {'raumtyp': 'S', 'besucht': True}],
                    [{'raumtyp': 'S', 'besucht': True}, {'raumtyp': 'L', 'besucht': True},
                     {'raumtyp': 'F', 'besucht': False},
                     {'raumtyp': 'S', 'besucht': False}]
                ],
                [2, 3],  # P erscheint bei [3][2], also bei y=3, x=2
                [
                    call('?', end = '  '), call('F', end = '  '), call('?', end = '  '), call('?', end = '  '),
                    call(),
                    call('S', end = '  '), call('?', end = '  '), call('S', end = '  '), call('?', end = '  '),
                    call(),
                    call('?', end = '  '), call('?', end = '  '), call('L', end = '  '), call('S', end = '  '),
                    call(),
                    call('S', end = '  '), call('L', end = '  '), call('P', end = '  '), call('?', end = '  '),
                    call()
                ]
            ]
        ]

        for test in tests:
            print_dungeon(test[0], test[1])

            self.assertEqual(test[2], mock_print.mock_calls)

            mock_print.reset_mock()
