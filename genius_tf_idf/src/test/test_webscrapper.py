import unittest
from src.main.webscrapper import WebScrapper

class WebscrapperTestCase(unittest.TestCase):
    def test_create_scrapper(self):
        scrapper = WebScrapper()
        self.assertIsNotNone(scrapper)

    def test_load_page_source_returns_string(self):
        scrapper = WebScrapper()
        page_source = scrapper.load_page_source('https://genius.com')
        self.assertTrue(isinstance(page_source, str))

    def test_load_page_source_returns_html(self):
        scrapper = WebScrapper()
        page_source = scrapper.load_page_source('https://genius.com')
        self.assertTrue("<html>" in page_source)

if __name__ == '__main__':
    unittest.main()
