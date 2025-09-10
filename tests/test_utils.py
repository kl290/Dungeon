import unittest

from Dungeon.utils import ist_spiel_aktiv
from Dungeon.views.menu_new import initialisierung


class TestIstSpielAktiv(unittest.TestCase):

    def setUp(self):
        self.game_data = {}

    def test_initialisierung_inhalt(self):
        result = initialisierung(self.game_data)

        self.assertEqual(result, 'dungeon')
        self.assertIn('spieler', self.game_data)
        self.assertIsNotNone(self.game_data['spieler'])
        self.assertIn('dungeon', self.game_data)
        self.assertIsNotNone(self.game_data['dungeon'])


    def test_ist_spiel_aktiv(self):
        game_data = {'spieler': 1, 'dungeon': [[]]}
        self.assertTrue(ist_spiel_aktiv(game_data))

        game_data = {'spieler': {'position': [0, 0]}}
        self.assertFalse(ist_spiel_aktiv(game_data))

        game_data = {'dungeon': [[{}, {}]]}
        self.assertFalse(ist_spiel_aktiv(game_data))

        game_data = {}
        self.assertFalse(ist_spiel_aktiv(game_data))


if __name__ == '__main__':
    unittest.main()
