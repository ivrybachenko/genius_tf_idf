import unittest

from data import DataLoader


class DataLoaderTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.songs = DataLoader.load()

    def test_that_count_is_204(self):
        self.assertEqual(204, len(self.songs))

    def test_keys(self):
        expected_keys = ['artist', 'lyrics', 'name']
        self.assertEqual(expected_keys, list(self.songs[0].keys()))


if __name__ == '__main__':
    unittest.main()
