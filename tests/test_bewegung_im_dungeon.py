import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dungeon.bewegung_im_dungeon import bewegung_im_dungeon


class TestBewegungImDungeon(unittest.TestCase):
    def setUp(self):
        self.dungeon = {
            0: {0: {}, 1: {}},
            1: {0: {}, 1: {}}
        }

    def test_erfolg(self):
        # Jeder Fall besteht aus Startkoordinaten, Eingabe und Zielkoordinaten
        testfaelle = [
            [(1, 1), "N", (1, 0)],
            [(0, 1), "O", (1, 1)],
            [(0, 0), "S", (0, 1)],
            [(1, 0), "W", (0, 0)],

        ]
        for testfall in testfaelle:
            self.spieler_position = {"x": testfall[0][0], "y": testfall[0][1]}
            result = bewegung_im_dungeon(self.dungeon, self.spieler_position, testfall[1])
            self.assertEqual('Erfolg', result, f'Fehler bei Index {testfall}')
            self.assertEqual({'x': testfall[2][0], 'y': testfall[2][1]}, self.spieler_position, f'Fehler bei Index {testfall}')

    def test_fehler(self):
        testfaelle = [
            [(1, 0), 'N', (1, 0)],
            [(1, 1), 'O', (1, 1)],
            [(0, 1), 'S', (0, 1)],
            [(0, 0), 'W', (0, 0)],
        ]
        for testfall in testfaelle:
            self.spieler_position = {'x': testfall[0][0], 'y': testfall[0][1]}
            result = bewegung_im_dungeon(self.dungeon, self.spieler_position, testfall[1])
            self.assertEqual('Fehler', result, f'Fehler bei Index {testfall}')
            self.assertEqual({'x': testfall[2][0], 'y': testfall[2][1]}, self.spieler_position, f'Fehler bei Index {testfall}')

    def test_position_ausserhalb_dungeon(self):
        testfaelle = [
            (-1, 0),  # x außerhalb
            (0, -1),  # y außerhalb
            (-1, -1),  # x und y außerhalb
        ]
        for pos in testfaelle:
            self.spieler_position = {'x': pos[0], 'y': pos[1]}
            result = bewegung_im_dungeon(self.dungeon, self.spieler_position, 'N')  # Bewegung kann beliebig sein
            self.assertEqual('Erfolg', result)
            self.assertEqual({'x': 0, 'y': 0}, self.spieler_position)

    def test_verlassen_des_dungeons(self):
        self.spieler_position = {'x': 0, 'y': 0}
        result = bewegung_im_dungeon(self.dungeon, self.spieler_position, 'Q')
        self.assertEqual('Ende', result)

    def test_ungueltige_eingabe(self):
        testfaelle = ["Z", "1", "","!", None, {}]
        for eingabe in testfaelle:
            self.spieler_position = {"x": 0, "y": 0}
            result = bewegung_im_dungeon(self.dungeon, self.spieler_position, eingabe)
            self.assertEqual("Fehler", result, f"Fehler bei Eingabe: {eingabe}")

