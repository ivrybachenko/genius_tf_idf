from bs4 import BeautifulSoup

from parser.component.mini_song_card import MiniSongCard


class SongPage:
    def __init__(self, card_html):
        self._root_html = card_html
        self._root_soup = BeautifulSoup(card_html)

    def get_source(self):
        return self._root_html

    def get_text(self):
        p = self._root_soup.select_one('div.lyrics p')
        p_without_br = BeautifulSoup(str(p).replace('<br/>', '\n'))
        for tag in p_without_br.select('defer-compile'):
            tag.extract()
        return p_without_br.text

    def get_song_name(self):
        return self._root_soup.select_one('h1.header_with_cover_art-primary_info-title').text.strip()

    def get_artist_name(self):
        return self._root_soup.select_one('a.header_with_cover_art-primary_info-primary_artist').text.strip()

