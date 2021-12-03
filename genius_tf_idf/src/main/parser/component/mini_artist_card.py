from bs4 import BeautifulSoup


class MiniArtistCard:
    def __init__(self, card_html):
        self._root_html = card_html
        self._root_soup = BeautifulSoup(card_html)

    def get_source(self):
        return self._root_html

    def get_artist_name(self):
        title_div = self._root_soup.select_one('div.mini_card-title')
        return title_div.text.strip()

    def get_artist_url(self):
        return self._root_soup.select_one('a')['href']
