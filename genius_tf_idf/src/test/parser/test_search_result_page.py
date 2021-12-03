import unittest

from parser.page import SearchResultPage


class SearchResultPageTestCase(unittest.TestCase):
    def setUp(self):
        with open('data/search_result_page.html', 'r') as f:
            self.search_result_page_html = f.read()

    def test_get_artists(self):
        parser = SearchResultPage(self.search_result_page_html)
        expected_artists = [
            {
                'artist_name': 'Trent Tomlinson',
                'artist_url': 'https://genius.com/artists/Trent-tomlinson'
            }
        ]
        self.assertEqual(expected_artists, parser.get_artists())