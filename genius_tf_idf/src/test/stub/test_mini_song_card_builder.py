import unittest

from stub.mini_song_card_builder import MiniSongCardBuilder


class MiniSongCardBuilderTestCase(unittest.TestCase):

    def test_fills_song_name(self):
        mini_song_card_html = MiniSongCardBuilder() \
            .with_artist_name('Trent Tomlinson') \
            .with_song_name('That’s What’s Working Right Now') \
            .with_song_url('https://genius.com/Trent-tomlinson-thats-whats-working-right-now-lyrics') \
            .build_html()
        self.assertTrue('That’s What’s Working Right Now' in mini_song_card_html)

    def test_fills_artist_name(self):
        mini_song_card_html = MiniSongCardBuilder() \
            .with_artist_name('Trent Tomlinson') \
            .with_song_name('That’s What’s Working Right Now') \
            .with_song_url('https://genius.com/Trent-tomlinson-thats-whats-working-right-now-lyrics') \
            .build_html()
        self.assertTrue('Trent Tomlinson' in mini_song_card_html)

    def test_fills_song_url(self):
        mini_song_card_html = MiniSongCardBuilder() \
            .with_artist_name('Trent Tomlinson') \
            .with_song_name('That’s What’s Working Right Now') \
            .with_song_url('https://genius.com/Trent-tomlinson-thats-whats-working-right-now-lyrics') \
            .build_html()
        self.assertTrue('https://genius.com/Trent-tomlinson-thats-whats-working-right-now-lyrics' in mini_song_card_html)

    def test_raises_exception_when_building_without_data(self):
        self.assertRaises(ValueError, MiniSongCardBuilder().build_html)

    def test_raises_exception_when_building_without_artist_name(self):
        self.assertRaises(ValueError, MiniSongCardBuilder()
                          .with_song_name('That’s What’s Working Right Now')
                          .with_song_url('https://genius.com/Trent-tomlinson-thats-whats-working-right-now-lyrics')
                          .build_html)

    def test_raises_exception_when_building_without_song_name(self):
        self.assertRaises(ValueError, MiniSongCardBuilder()
                          .with_artist_name('Trent Tomlinson')
                          .with_song_url('https://genius.com/Trent-tomlinson-thats-whats-working-right-now-lyrics')
                          .build_html)

    def test_raises_exception_when_building_without_song_url(self):
        self.assertRaises(ValueError, MiniSongCardBuilder()
                          .with_artist_name('Trent Tomlinson')
                          .with_song_name('That’s What’s Working Right Now')
                          .build_html)

if __name__ == '__main__':
    unittest.main()
