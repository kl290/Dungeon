import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dungeon.bewegung_im_dungeon import bewegung_im_dungeon


class TestBewegungImDungeon(unittest.TestCase):
    def test_lower_strip_verarbeitung(self):
        eingaben = ['n', 'S', ' o', 'W ', '  q ']

        for eingabe in eingaben:
            eingabe = eingabe.strip().lower()
            self.assertIn(eingabe, ['n', 's', 'o', 'w', 'q'], f"Fehler bei Eingabe: {eingabe}")

    def setUp(self):
        self.dungeon = {
            0: {0: {}, 1: {}, 2: {}, 3: {}},
            1: {0: {}, 1: {}, 2: {}, 3: {}},
            2: {0: {}, 1: {}, 2: {}, 3: {}},
            3: {0: {}, 1: {}, 2: {}, 3: {}}
        }

    def test_erfolg(self):
        testfaelle = [
            [(2, 3), "n", (2, 2)],
            [(2, 3), "N", (2, 2)],
            [(0, 2), "o", (1, 2)],
            [(0, 2), "O", (1, 2)],
            [(1, 1), "s", (1, 2)],
            [(1, 1), "S", (1, 2)],
            [(3, 1), "w", (2, 1)],
            [(3, 1), "W", (2, 1)],
        ]
        for start, eingabe, ziel in testfaelle:
            spieler = {"position": [start[0], start[1]]}
            result = bewegung_im_dungeon(self.dungeon, spieler, eingabe)
            self.assertEqual('Erfolg', result, f"Fehler bei Testfall: Start={start}, Eingabe='{eingabe}'")
            self.assertEqual([ziel[0], ziel[1]], spieler['position'], f"Position nicht korrekt bei Start={start}, Eingabe='{eingabe}'")

    def test_fehler(self):
        testfaelle = [
            [(1, 0), 'N', (1, 0)],
            [(3, 1), 'O', (3, 1)],
            [(3, 3), 'S', (3, 3)],
            [(0, 0), 'W', (0, 0)],
        ]
        for start, eingabe, ziel in testfaelle:
            spieler = {'position': [start[0], start[1]]}
            result = bewegung_im_dungeon(self.dungeon, spieler, eingabe)
            self.assertEqual('Fehler', result, f"Fehler erwartet bei Start={start}, Eingabe='{eingabe}'")
            self.assertEqual([ziel[0], ziel[1]], spieler['position'], f"Position darf sich nicht ändern bei Fehler: Start={start}, Eingabe='{eingabe}'")

    def test_position_ausserhalb_dungeon(self):
        testfaelle = [
            [-1, 0],
            [0, -1],
            [-1, -1],
        ]
        for position in testfaelle:
            spieler = {'position': [position[0], position[1]]}
            result = bewegung_im_dungeon(self.dungeon, spieler, 'N')
            self.assertEqual('Erfolg', result, f"Fehler bei Startposition außerhalb: {position}")
            self.assertEqual([0, 0], spieler['position'], f"Position nicht zurückgesetzt bei: {position}")

    def test_verlassen_des_dungeons(self):
        positionen = [
            [-2, 1],
            [1, -3],
            [2, 2],
            [-2, -3],
            [0, 0]
        ]

        for pos in positionen:
            spieler = {'position': pos}
            result = bewegung_im_dungeon(self.dungeon, spieler, 'q')
            self.assertEqual('Ende', result, f"Dungeon sollte bei Eingabe 'q' verlassen werden, Position: {pos}")

    def test_ungueltige_eingabe(self):
        testfaelle = ['Z', ' z ', 'X', '!', ' 1 ', '']

        for eingabe in testfaelle:
            spieler = {'position': [0, 0]}
            result = bewegung_im_dungeon(self.dungeon, spieler, eingabe)
            self.assertEqual('Fehler', result, f"Fehler bei ungültiger Eingabe: '{eingabe}'")
            self.assertEqual([0, 0], spieler['position'], f"Position darf sich bei ungültiger Eingabe nicht ändern: '{eingabe}'")
