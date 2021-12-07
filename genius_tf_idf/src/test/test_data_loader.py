import unittest

from data import DataLoader


class DataLoaderTestCase(unittest.TestCase):
    def test_that_count_is_204(self):
        loader = DataLoader()
        songs = loader.load()
        self.assertEqual(204, len(songs))


if __name__ == '__main__':
    unittest.main()
