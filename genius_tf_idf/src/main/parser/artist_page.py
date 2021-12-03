from bs4 import BeautifulSoup

from parser.mini_song_card import MiniSongCard


class ArtistPage:
    def __init__(self, card_html):
        self._root_html = card_html
        self._root_soup = BeautifulSoup(card_html)

    def get_source(self):
        return self._root_html

    def get_songs(self):
        songs = []
        songs_cards = self._root_soup.select('mini-song-card')
        for song_card in songs_cards:
            songs.append({
                'artist_name': MiniSongCard(str(song_card)).get_artist_name(),
                'song_name': MiniSongCard(str(song_card)).get_song_name(),
                'song_url': MiniSongCard(str(song_card)).get_song_url()
            })
        return songs

    def get_artist_name(self):
        return self._root_soup.select_one('h1.profile_identity-name_iq_and_role_icon').text.strip()