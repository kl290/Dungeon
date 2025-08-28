import unittest

from Dungeon.utils import ist_spiel_aktiv
from Dungeon.views.menu_new import initialisierung


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

    def test_initialisierung_inhalt(self):
        def setUp(self):
            self.game_data = {}

            result = initialisierung(self.game_data)

            self.assertEqual(result, 'dungeon')

            self.assertIn('spieler', self.game_data)
            self.assertIsNotNone(self.game_data['spieler'])

            self.assertIn('dungeon', self.game_data)
            self.assertIsNotNone(self.game_data['dungeon'])


if __name__ == '__main__':
    unittest.main()
