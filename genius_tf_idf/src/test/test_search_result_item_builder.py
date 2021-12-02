import unittest

from parser.mini_artist_card_builder import MiniArtistCardBuilder
from parser.search_result_item_builder import SearchResultItemBuilder


class SearchResultItemBuilderTestCase(unittest.TestCase):

    def test_fills_data(self):
        mini_artist_card = MiniArtistCardBuilder()\
            .with_artist_name('Bob Marley')\
            .with_artist_url('https://genius.com/artists/Bob-Marley')\
            .build_html()
        search_result_item_html = SearchResultItemBuilder()\
            .with_data(mini_artist_card)\
            .build_html()
        self.assertTrue(mini_artist_card in search_result_item_html)

if __name__ == '__main__':
    unittest.main()
