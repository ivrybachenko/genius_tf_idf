import unittest
from webscrapper import WebScrapper

class WebscrapperTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.scrapper = WebScrapper()

    def test_create_scrapper(self):
        self.assertIsNotNone(self.scrapper)

    def test_load_page_source_returns_string(self):
        page_source = self.scrapper.load_page_source('https://genius.com')
        self.assertTrue(isinstance(page_source, str))

    def test_load_page_source_returns_html(self):
        page_source = self.scrapper.load_page_source('https://genius.com')
        self.assertTrue("<html>" in page_source)

if __name__ == '__main__':
    unittest.main()
