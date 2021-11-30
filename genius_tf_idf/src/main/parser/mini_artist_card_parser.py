from bs4 import BeautifulSoup

class MiniArtistCardParser():
    def __init__(self, card_html):
        self._root_html = card_html
        self._root_soup = BeautifulSoup(card_html)

    def get_source(self):
        return self._root_html