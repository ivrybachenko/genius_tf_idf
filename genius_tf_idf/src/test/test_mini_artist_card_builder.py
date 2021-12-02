import unittest

from parser.mini_artist_card_builder import MiniArtistCardBuilder


class MiniArtistCardBuilderTestCase(unittest.TestCase):

    def test_fills_artist_name(self):
        mini_artist_card_html = MiniArtistCardBuilder().with_artist_name('Trent Tomlinson')\
            .build_html()
        self.assertTrue('Trent Tomlinson' in mini_artist_card_html)

    def test_fills_artist_url(self):
        mini_artist_card_html = MiniArtistCardBuilder().with_artist_url('https://genius.com/artists/Trent-tomlinson')\
            .build_html()
        self.assertTrue('https://genius.com/artists/Trent-tomlinson' in mini_artist_card_html)

if __name__ == '__main__':
    unittest.main()