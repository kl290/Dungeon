import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dungeon import validiereSpielerObjekt, validiere_dungeon


class TestDungeon(unittest.TestCase):

    def test_validierungen(self):
        spieler_korrekt = {'leben': 100, 'gold': 0, 'position': [0, 0]}
        validiereSpielerObjekt(spieler_korrekt)

        spieler_falsch_v1 = {'leben': 100, 'position': [0, 0]}
        with self.assertRaisesRegex(ValueError, "Es müssen alle Elemente des Spielers übergeben werden!"):
            validiereSpielerObjekt(spieler_falsch_v1)

        spieler_falsch_v2 = {'gold': 0, 'position': [0, 0]}
        with self.assertRaises(ValueError):
            validiereSpielerObjekt(spieler_falsch_v2)

        spieler_falsch_v3 = {'leben': 100, 'gold': 0}
        with self.assertRaises(ValueError):
            validiereSpielerObjekt(spieler_falsch_v3)

        dungeon_korrekt = {
            0: {0: {'raumtyp': 'L', 'besucht': True},
                1: {'raumtyp': 'F', 'besucht': False}},
            1: {0: {'raumtyp': 'S', 'besucht': False},
                1: {'raumtyp': 'L', 'besucht': True}}
        }
        validiere_dungeon(dungeon_korrekt)

        dungeon_falsch_v1 = {0: {0: {'raumtyp': 'X', 'besucht': True}}}
        with self.assertRaisesRegex(ValueError, 'Dungeon enthält ungültige Räume!'):
            validiere_dungeon(dungeon_falsch_v1)

        dungeon_falsch_v2 = {0: {0: {'raumtyp': 'L', 'besucht': None}}}
        with self.assertRaisesRegex(ValueError, "Raum 'besucht' muss True oder False sein!"):
            validiere_dungeon(dungeon_falsch_v2)

        dungeon_falsch_v3 = {
            0: {0: {'raumtyp': 'L', 'besucht': True},
                1: {'raumtyp': 'F', 'besucht': False}},
            1: {0: {'raumtyp': 'S', 'besucht': False},
                1: {'raumtyp': 'l', 'besucht': True}}
        }
        with self.assertRaises(ValueError):
            validiere_dungeon(dungeon_falsch_v3)


if __name__ == "__main__":
    unittest.main()
