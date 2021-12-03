import unittest

from parser.component import MiniSongCard
from stub.mini_song_card_builder import MiniSongCardBuilder


class MiniSongCardTestCase(unittest.TestCase):

    def test_get_source(self):
        mini_song_card_html = MiniSongCardBuilder() \
            .with_artist_name('Trent Tomlinson') \
            .with_song_name('That’s What’s Working Right Now') \
            .with_song_url('https://genius.com/Trent-tomlinson-thats-whats-working-right-now-lyrics') \
            .build_html()
        parser = MiniSongCard(mini_song_card_html)
        self.assertEqual(mini_song_card_html, parser.get_source())

    def test_get_artist_name(self):
        mini_song_card_html = MiniSongCardBuilder() \
            .with_artist_name('Trent Tomlinson') \
            .with_song_name('That’s What’s Working Right Now') \
            .with_song_url('https://genius.com/Trent-tomlinson-thats-whats-working-right-now-lyrics') \
            .build_html()
        parser = MiniSongCard(mini_song_card_html)
        self.assertEqual('Trent Tomlinson', parser.get_artist_name())

    def test_get_artist_name_removes_whitespaces(self):
        mini_song_card_html = MiniSongCardBuilder() \
            .with_artist_name(' Trent Tomlinson ') \
            .with_song_name('That’s What’s Working Right Now') \
            .with_song_url('https://genius.com/Trent-tomlinson-thats-whats-working-right-now-lyrics') \
            .build_html()
        parser = MiniSongCard(mini_song_card_html)
        self.assertEqual('Trent Tomlinson', parser.get_artist_name())

    def test_get_song_name(self):
        mini_song_card_html = MiniSongCardBuilder() \
            .with_artist_name('Trent Tomlinson') \
            .with_song_name('That’s What’s Working Right Now') \
            .with_song_url('https://genius.com/Trent-tomlinson-thats-whats-working-right-now-lyrics') \
            .build_html()
        parser = MiniSongCard(mini_song_card_html)
        self.assertEqual('That’s What’s Working Right Now', parser.get_song_name())

    def test_get_song_name_removes_whitespaces(self):
        mini_song_card_html = MiniSongCardBuilder() \
            .with_artist_name('Trent Tomlinson') \
            .with_song_name(' That’s What’s Working Right Now ') \
            .with_song_url('https://genius.com/Trent-tomlinson-thats-whats-working-right-now-lyrics') \
            .build_html()
        parser = MiniSongCard(mini_song_card_html)
        self.assertEqual('That’s What’s Working Right Now', parser.get_song_name())

    def test_get_song_url(self):
        mini_song_card_html = MiniSongCardBuilder() \
            .with_artist_name('Trent Tomlinson') \
            .with_song_name('That’s What’s Working Right Now') \
            .with_song_url('https://genius.com/Trent-tomlinson-thats-whats-working-right-now-lyrics') \
            .build_html()
        parser = MiniSongCard(mini_song_card_html)
        self.assertEqual('https://genius.com/Trent-tomlinson-thats-whats-working-right-now-lyrics', parser.get_song_url())

if __name__ == '__main__':
    unittest.main()
