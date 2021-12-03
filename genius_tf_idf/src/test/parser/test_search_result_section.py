import unittest

from stub.mini_artist_card_builder import MiniArtistCardBuilder
from stub.search_result_item_builder import SearchResultItemBuilder
from parser.search_result_section import SearchResultSection
from stub.search_result_section_builder import SearchResultSectionBuilder


class SearchResultSectionTestCase(unittest.TestCase):

    def create_item(self, data):
        return SearchResultItemBuilder() \
            .with_data(data) \
            .build_html()

    def test_get_source(self):
        search_result_section_html = SearchResultSectionBuilder()\
            .with_label('Artists')\
            .build_html()
        parser = SearchResultSection(search_result_section_html)
        self.assertEqual(search_result_section_html, parser.get_source())

    def test_get_label(self):
        search_result_section_html = SearchResultSectionBuilder() \
            .with_label('Artists') \
            .build_html()
        parser = SearchResultSection(search_result_section_html)
        self.assertEqual('Artists', parser.get_label())

    def test_get_items(self):
        item1_html = self.create_item(MiniArtistCardBuilder()
                                     .with_artist_name('Trent Tomlinson')
                                     .with_artist_url('https://genius.com/artists/Trent-tomlinson')
                                     .build_html())
        item2_html = self.create_item(MiniArtistCardBuilder()
                                      .with_artist_name('Bob Marley')
                                      .with_artist_url('https://genius.com/artists/Bob-marley')
                                      .build_html())
        search_result_section_html = SearchResultSectionBuilder()\
            .with_label('Artists')\
            .with_item(item1_html) \
            .with_item(item2_html) \
            .build_html()

        parser = SearchResultSection(search_result_section_html)
        expected_items = [
            {
                'artist_name': 'Trent Tomlinson',
                'artist_url': 'https://genius.com/artists/Trent-tomlinson'
            },
            {
                'artist_name': 'Bob Marley',
                'artist_url': 'https://genius.com/artists/Bob-marley'
            }
        ]
        self.assertEqual(expected_items, parser.get_items())

if __name__ == '__main__':
    unittest.main()
