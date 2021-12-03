import unittest

from stub.artist_page_builder import ArtistPageBuilder
from stub.mini_song_card_builder import MiniSongCardBuilder


class ArtistPageBuilderTestCase(unittest.TestCase):

    def test_fills_artist_name(self):
        artist_page_html = ArtistPageBuilder() \
            .with_artist_name('Trent Tomlinson') \
            .build_html()
        self.assertTrue('Trent Tomlinson' in artist_page_html)

    def test_fills_songs(self):
        song1 = MiniSongCardBuilder()\
            .with_artist_name('Artist 1')\
            .with_song_name('Song 1')\
            .with_song_url('localhost/song1')\
            .build_html()
        song2 = MiniSongCardBuilder() \
            .with_artist_name('Artist 2') \
            .with_song_name('Song 2') \
            .with_song_url('localhost/song2') \
            .build_html()
        artist_page_html = ArtistPageBuilder() \
            .with_artist_name('Trent Tomlinson') \
            .with_song(song1)\
            .with_song(song2)\
            .build_html()
        self.assertTrue(song1 in artist_page_html
                        and
                        song2 in artist_page_html)

    def test_raises_exception_when_building_without_data(self):
        self.assertRaises(ValueError, ArtistPageBuilder().build_html)


if __name__ == '__main__':
    unittest.main()
