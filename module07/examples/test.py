import time
import pages
import unittest
from selenium import webdriver

class PageObjectTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_search_for_tutorial_should_work(self):
        # create main page and navigate to it
        main_page = pages.MainPage(self.driver)
        main_page.search_for('tutorial')

        # wait for search results to load
        time.sleep(7)
        search_results = pages.SearchResults(self.driver)
        # .results is a list of <a> tags
        assert 'https://www.python.org/' in search_results.results()[0].get_attribute('href') 


    def test_search_for_non_existing(self):
        # create main page and navigate to it
        main_page = pages.MainPage(self.driver)
        main_page.search_for('banitza')

        # wait for search results to load
        time.sleep(7)
        search_results = pages.SearchResults(self.driver)
        # .results is empty
        assert 0 == len(search_results.results())


if __name__ == '__main__':
    unittest.main()

