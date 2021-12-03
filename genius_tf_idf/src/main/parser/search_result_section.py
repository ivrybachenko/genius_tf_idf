from bs4 import BeautifulSoup

from parser import MiniArtistCard


class SearchResultSection():
    def __init__(self, html):
        self._root_html = html
        self._root_soup = BeautifulSoup(html)

    def get_source(self):
        return self._root_html

    def get_label(self):
        section_labels = self._root_soup.select('div.search_results_label')
        if len(section_labels) == 1:
            return section_labels[0].text.strip()
        else:
            return None

    def get_items(self):
        if self.get_label() == 'Artists':
            return self.get_artists()
        return []

    def get_artists(self):
        artists = []
        artist_cards = self._root_soup.select('mini-artist-card')
        for artist_card in artist_cards:
            artists.append({
                'artist_name': MiniArtistCard(str(artist_card)).get_artist_name(),
                'artist_url': MiniArtistCard(str(artist_card)).get_artist_url()
            })
        return artists
