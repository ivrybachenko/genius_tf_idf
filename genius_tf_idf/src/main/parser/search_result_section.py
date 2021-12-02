from bs4 import BeautifulSoup


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
        pass