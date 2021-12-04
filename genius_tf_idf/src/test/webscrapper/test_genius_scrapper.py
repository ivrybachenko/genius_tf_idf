import unittest

from configuration import SLOW_TESTS
from webscrapper import GeniusScrapper

SLOW_TESTS = True

class GeniusScrapperTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.scrapper = GeniusScrapper()
        self.maxDiff = None
        with open('data/trent_tomlinson_song1.txt', 'r') as f:
            self.song1 = f.read()
        with open('data/trent_tomlinson_song2.txt', 'r') as f:
            self.song2 = f.read()

    @unittest.skipUnless(SLOW_TESTS, "slow test")
    def test_get_songs(self):
        actual_songs = self.scrapper.get_songs('Trent Tomlinson', 2)
        expected_songs = [
            {
                'artist_name': 'Trent Tomlinson',
                'artist_url': 'https://genius.com/artists/Trent-tomlinson',
                'song_name': 'That’s What’s Working Right Now',
                'song_text': self.song1,
                'song_url': 'https://genius.com/Trent-tomlinson-thats-whats-working-right-now-lyrics'
            },
            {
                'artist_name': 'Trent Tomlinson',
                'artist_url': 'https://genius.com/artists/Trent-tomlinson',
                'song_name': 'For the Life of Me',
                'song_text': self.song2,
                'song_url': 'https://genius.com/Trent-tomlinson-for-the-life-of-me-lyrics'
            }
        ]
        self.assertEqual(expected_songs, actual_songs)

    def tearDown(self) -> None:
        self.scrapper.dispose()

if __name__ == '__main__':
    unittest.main()
