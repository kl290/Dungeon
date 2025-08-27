import unittest

from Dungeon.utils import ist_spiel_aktiv


class TestIstSpielAktiv(unittest.TestCase):

    def test_spiel_aktiv(self):
        game_data = {
            'spieler': {'position': [1, 0]},
            'dungeon': [[{}, {}], [{}, {}]]
        }
        result = ist_spiel_aktiv(game_data)
        self.assertTrue(result)

    def test_spiel_inaktiv(self):
        game_data1 = {'dungeon': [[{}, {}], [{}, {}]]}
        self.assertFalse(ist_spiel_aktiv(game_data1))

        game_data2 = {'spieler': {'position': [0, 0]}}
        self.assertFalse(ist_spiel_aktiv(game_data2))


if __name__ == '__main__':
    unittest.main()
