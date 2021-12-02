import unittest

from parser.mini_artist_card_builder import MiniArtistCardBuilder
from parser.search_result_item_builder import SearchResultItemBuilder
from parser.search_result_section_builder import SearchResultSectionBuilder


class SearchResultSectionBuilderTestCase(unittest.TestCase):

    def create_item(self, data):
        return SearchResultItemBuilder()\
                .with_data(data)\
                .build_html()

    def test_fills_label(self):
        search_result_section_html = SearchResultSectionBuilder() \
            .with_label('Artists') \
            .build_html()
        self.assertTrue('Artists' in search_result_section_html)

    def test_fills_single_item(self):
        item = self.create_item(MiniArtistCardBuilder()
                                .with_artist_name('Trent Tomlinson')
                                .with_artist_url('https://genius.com/artists/Trent-tomlinson')
                                .build_html())
        search_result_section_html = SearchResultSectionBuilder() \
            .with_label('Artists') \
            .with_item(item) \
            .build_html()

        self.assertTrue(item in search_result_section_html)

    def test_fills_multiple_items(self):
        item1 = self.create_item(MiniArtistCardBuilder()
                                 .with_artist_name('Trent Tomlinson')
                                 .with_artist_url('https://genius.com/artists/Trent-tomlinson')
                                 .build_html())
        item2 = self.create_item(MiniArtistCardBuilder()
                                 .with_artist_name('Eminem')
                                 .with_artist_url('https://genius.com/artists/Eminem')
                                 .build_html())
        search_result_section_html = SearchResultSectionBuilder() \
            .with_label('Artists') \
            .with_item(item1) \
            .with_item(item2) \
            .build_html()

        self.assertTrue(item1 in search_result_section_html
                        and
                        item2 in search_result_section_html)

    def test_does_not_raise_exception_without_data(self):
        SearchResultSectionBuilder().build_html()


if __name__ == '__main__':
    unittest.main()
