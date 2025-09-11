import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dungeon import validiereSpielerObjekt
from Dungeon.bewegung_im_dungeon import bewegung_im_dungeon


class TestBewegungImDungeon(unittest.TestCase):

    def setUp(self):
        self.dungeon = {
            0: {0: {}, 1: {}, 2: {}, 3: {}},
            1: {0: {}, 1: {}, 2: {}, 3: {}},
            2: {0: {}, 1: {}, 2: {}, 3: {}},
            3: {0: {}, 1: {}, 2: {}, 3: {}}
        }

    @patch('Dungeon.bewegung_im_dungeon.validiereSpielerObjekt', return_value = None)
    def test_erfolg(self, mock_validiere_spieler_objekt):
        testfaelle = [
            [(2, 3), 'n', (2, 2)],
            [(2, 3), 'N', (2, 2)],
            [(0, 2), 'o', (1, 2)],
            [(0, 2), 'O', (1, 2)],
            [(1, 1), 's', (1, 2)],
            [(1, 1), 'S', (1, 2)],
            [(3, 1), 'w', (2, 1)],
            [(3, 1), 'W', (2, 1)],
        ]
        for start, eingabe, ziel in testfaelle:
            spieler = {"position": [start[0], start[1]]}
            result = bewegung_im_dungeon(self.dungeon, spieler, eingabe)
            self.assertEqual('Erfolg', result, f"Fehler bei Testfall: Start={start}, Eingabe='{eingabe}'")
            self.assertEqual([ziel[0], ziel[1]], spieler['position'],
                             f"Position nicht korrekt bei Start={start}, Eingabe='{eingabe}'")
            mock_validiere_spieler_objekt.assert_called()

    @patch('Dungeon.bewegung_im_dungeon.validiereSpielerObjekt', return_value = None)
    def test_fehler(self, mock_validiere_spieler_objekt):
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
            self.assertEqual([ziel[0], ziel[1]], spieler['position'],
                             f"Position darf sich nicht ändern bei Fehler: Start={start}, Eingabe='{eingabe}'")

    @patch('Dungeon.bewegung_im_dungeon.validiereSpielerObjekt', return_value = None)
    def test_position_ausserhalb_dungeon(self, mock_validiere_spieler_objekt):
        testfaelle = [
            [-1, 0],
            [0, -1],
            [-1, -1],
        ]
        for position in testfaelle:
            spieler = {'position': [position[0], position[1]],
                       "leben": 100,
                       "gold": 0}
            result = bewegung_im_dungeon(self.dungeon, spieler, 'N')
            self.assertEqual('Fehler', result, f"Fehler bei Startposition außerhalb: {position}")
            self.assertEqual([0, 0], spieler['position'], f"Position nicht zurückgesetzt bei: {position}")

    @patch('Dungeon.bewegung_im_dungeon.validiereSpielerObjekt', return_value = None)
    def test_ungueltige_eingabe(self, mock_validiere_spieler_objekt):
        testfaelle = ['Z', ' z ', 'X', '!', ' 1 ', '']

        for eingabe in testfaelle:
            spieler = {'position': [0, 0],
                       "leben": 100,
                       "gold": 0}
            result = bewegung_im_dungeon(self.dungeon, spieler, eingabe)
            self.assertEqual('Fehler', result, f"Fehler bei ungültiger Eingabe: '{eingabe}'")
            self.assertEqual([0, 0], spieler['position'],
                             f"Position darf sich bei ungültiger Eingabe nicht ändern: '{eingabe}'")

    @patch('Dungeon.istValiderSpieler', return_value = False)
    def test_validiere_spieler_objekt(self, mock_ist_valider_spieler):
        spieler = {'position': [0, 0]}

        with self.assertRaises(ValueError):
            validiereSpielerObjekt(spieler)

        mock_ist_valider_spieler.assert_called_once()
