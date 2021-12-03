import unittest

from parser import ArtistPage
from stub.artist_page_builder import ArtistPageBuilder
from stub.mini_song_card_builder import MiniSongCardBuilder


class ArtistPageTestCase(unittest.TestCase):
    def test_get_source(self):
        artist_page_html = ArtistPageBuilder()\
            .with_artist_name('Artist1')\
            .build_html()
        parser = ArtistPage(artist_page_html)
        self.assertEqual(artist_page_html, parser.get_source())

    def test_get_artist_name(self):
        artist_page_html = ArtistPageBuilder() \
            .with_artist_name('Artist1') \
            .build_html()
        parser = ArtistPage(artist_page_html)
        self.assertEqual('Artist1', parser.get_artist_name())

    def test_get_songs(self):
        song1 = MiniSongCardBuilder() \
            .with_artist_name('Artist 1') \
            .with_song_name('Song 1') \
            .with_song_url('localhost/song1') \
            .build_html()
        song2 = MiniSongCardBuilder() \
            .with_artist_name('Artist 2') \
            .with_song_name('Song 2') \
            .with_song_url('localhost/song2') \
            .build_html()
        artist_page_html = ArtistPageBuilder() \
            .with_artist_name('Artist1') \
            .with_song(song1)\
            .with_song(song2)\
            .build_html()
        parser = ArtistPage(artist_page_html)
        expected_songs = [
            {
                'artist_name': 'Artist 1',
                'song_name': 'Song 1',
                'song_url': 'localhost/song1'
            },
            {
                'artist_name': 'Artist 2',
                'song_name': 'Song 2',
                'song_url': 'localhost/song2'
            }
        ]
        self.assertEqual(expected_songs, parser.get_songs())