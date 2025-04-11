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
        testfaelle = [
            [(1, 1), "N", (1, 0)],
            [(0, 1), "O", (1, 1)],
            [(0, 0), "S", (0, 1)],
            [(1, 0), "W", (0, 0)],
        ]
        for start, eingabe, ziel in testfaelle:
            spieler = {"position": [start[0], start[1]]}
            result = bewegung_im_dungeon(self.dungeon, spieler, eingabe)
            self.assertEqual('Erfolg', result, ('Fehler bei Testfall', start, eingabe))
            self.assertEqual([ziel[0], ziel[1]], spieler['position'], 'Position nicht korrekt')

    def test_fehler(self):
        testfaelle = [
            [(1, 0), 'N', (1, 0)],
            [(1, 1), 'O', (1, 1)],
            [(0, 1), 'S', (0, 1)],
            [(0, 0), 'W', (0, 0)],
        ]
        for start, eingabe, ziel in testfaelle:
            spieler = {'position': [start[0], start[1]]}
            result = bewegung_im_dungeon(self.dungeon, spieler, eingabe)
            self.assertEqual('Fehler', result, ('Fehler erwartet bei', start, eingabe))
            self.assertEqual([ziel[0], ziel[1]], spieler['position'], 'Position darf sich nicht ändern bei Fehler')

    def test_position_ausserhalb_dungeon(self):
        testfaelle = [
            [-1, 0],
            [0, -1],
            [-1, -1],
        ]
        for position in testfaelle:
            spieler = {'position': [position[0], position[1]]}
            result = bewegung_im_dungeon(self.dungeon, spieler, 'N')  # Bewegung beliebig
            self.assertEqual('Erfolg', result)
            self.assertEqual([0, 0], spieler['position'])

    def test_verlassen_des_dungeons(self):
        spieler = {'position': [0, 0]}
        result = bewegung_im_dungeon(self.dungeon, spieler, 'Q')
        self.assertEqual('Ende', result)

    def test_ungueltige_eingabe(self):
        testfaelle = ['Z', '1', '', '!', None, {}]
        for eingabe in testfaelle:
            spieler = {'position': [0, 0]}
            result = bewegung_im_dungeon(self.dungeon, spieler, eingabe)
            self.assertEqual('Fehler', result, ('Fehler bei Eingabe:', eingabe))
            self.assertEqual([0, 0], spieler['position'], 'Position darf sich bei ungültiger Eingabe nicht ändern')

    def test_gross_und_kleinbuchtsaben(self):
        testfaelle = [
            [(1, 1), "N", (1, 0)],
            [(1, 1), "n", (1, 0)],
            [(0, 1), "o", (1, 1)],
            [(0, 1), "O", (1, 1)],

        ]
        for start, eingabe, ziel in testfaelle:
            spieler = {"position": [start[0], start[1]]}
            result = bewegung_im_dungeon(self.dungeon, spieler, eingabe)
            self.assertEqual('Erfolg', result, ('Fehler bei Testfall', start, eingabe))
            self.assertEqual([ziel[0], ziel[1]], spieler['position'], 'Position nicht korrekt')
