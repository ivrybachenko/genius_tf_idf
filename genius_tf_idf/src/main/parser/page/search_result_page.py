from bs4 import BeautifulSoup

from parser.component import SearchResultSection


class SearchResultPage:
    def __init__(self, card_html):
        self._root_html = card_html
        self._root_soup = BeautifulSoup(card_html)

    def get_source(self):
        return self._root_html

    def get_artists(self):
        search_result_sections = self._root_soup.select('search-result-section')
        for section in search_result_sections:
            if SearchResultSection(str(section)).get_label() == 'Artists':
                return SearchResultSection(str(section)).get_artists()
        return []