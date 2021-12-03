from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class WebScrapper:
    def __init__(self):
        self._driver = self._create_driver()

    def load_page_source(self, url):
        self._driver.get(url)
        return self._driver.page_source

    def _create_driver(self):
        options = Options()
        options.headless = True
        return webdriver.Firefox(options=options)
