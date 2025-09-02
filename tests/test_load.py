import pickle
import unittest
from unittest.mock import mock_open, patch

from Dungeon.load import load


class TestLoad(unittest.TestCase):

    @patch("builtins.open", new_callable = mock_open, read_data = pickle.dumps({}))
    @patch("os.path.exists", return_value = True)
    def test_lade_existing_file(self, mock_exists, mock_file):
        result = load("test.pkl")
        self.assertEqual(result, {})
        mock_exists.assert_called_once()
        mock_file.assert_called_once()

    @patch("builtins.open")
    @patch("os.path.exists", return_value = False)
    def test_lade_not_existing_file(self, mock_exists, mock_file):
        result = load("test.pkl")
        self.assertIsNone(result)
        mock_exists.assert_called_once()


if __name__ == "__main__":
    unittest.main()
