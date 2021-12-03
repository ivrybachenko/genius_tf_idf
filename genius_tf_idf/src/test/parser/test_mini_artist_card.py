import unittest

from parser.component import MiniArtistCard
from stub.mini_artist_card_builder import MiniArtistCardBuilder


class MiniArtistCardTestCase(unittest.TestCase):

    def test_get_source(self):
        mini_artist_card_html = MiniArtistCardBuilder()\
            .with_artist_name('Trent Tomlinson')\
            .with_artist_url('https://genius.com/artists/Trent-tomlinson')\
            .build_html()
        parser = MiniArtistCard(mini_artist_card_html)
        self.assertEqual(mini_artist_card_html, parser.get_source())

    def test_get_artist_name(self):
        mini_artist_card_html = MiniArtistCardBuilder() \
            .with_artist_name('Trent Tomlinson') \
            .with_artist_url('https://genius.com/artists/Trent-tomlinson') \
            .build_html()
        parser = MiniArtistCard(mini_artist_card_html)
        self.assertEqual('Trent Tomlinson', parser.get_artist_name())

    def test_get_artist_name_removes_whitespaces(self):
        mini_artist_card_html = MiniArtistCardBuilder() \
            .with_artist_name(' Trent Tomlinson ') \
            .with_artist_url('https://genius.com/artists/Trent-tomlinson') \
            .build_html()
        parser = MiniArtistCard(mini_artist_card_html)
        self.assertEqual('Trent Tomlinson', parser.get_artist_name())

    def test_get_artist_url(self):
        mini_artist_card_html = MiniArtistCardBuilder() \
            .with_artist_name('Trent Tomlinson') \
            .with_artist_url('https://genius.com/artists/Trent-tomlinson') \
            .build_html()
        parser = MiniArtistCard(mini_artist_card_html)
        self.assertEqual('https://genius.com/artists/Trent-tomlinson', parser.get_artist_url())

if __name__ == '__main__':
    unittest.main()
