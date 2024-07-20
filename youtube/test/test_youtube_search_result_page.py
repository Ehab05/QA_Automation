import unittest
from youtube.infra.browser_wrapper import BrowserWrapper
from youtube.logic.no_results_found_page import YoutubeNoResultsPage
from youtube.logic.youtube_home_page import YoutubeHomePage
from youtube.logic.youtube_search_result_page import YoutubeSearchResultPage
import time


class TestYoutubeSearchResultPage(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserWrapper().get_driver()

    def tearDown(self):
        self._driver.quit()

    def test_valid_search_result(self):
        """
           test case 002: Search for a video on the YouTube home page with valid search input
           testing searching with a valid search input and verifying
           the results are relevant to the search
        """
        # initialize youtube home page
        home_page = YoutubeHomePage(self._driver)
        # searching with a valid input
        home_page.search_for("human mind")
        search_result_page = YoutubeSearchResultPage(self._driver)
        # verifying the result
        exist = search_result_page.check_text_in_search_result("human mind")
        # asserting the search result is relevant to the search input
        self.assertTrue(exist)

    def test_invalid_search_result(self):
        """
             test case 003: Search for a video on the YouTube home page with invalid search input
             testing searching with invalid search input and verifying
             the message No results found
        """
        # initialize youtube home page
        home_page = YoutubeHomePage(self._driver)
        # searching with invalid input
        home_page.search_for("!@#@%$@%")
        search_result_page = YoutubeNoResultsPage(self._driver)
        # verifying the result
        result = search_result_page.no_result_found()
        expected = "No results found"
        # asserting that there are no results found for the invalid input
        self.assertEqual(result, expected)

    def test_home_page_button_in_search_result(self):
        """
         testing the home button functionality in the search
         results page
         """
        # initialize youtube home page
        home_page = YoutubeHomePage(self._driver)
        # searching with a valid input
        home_page.search_for("the one thing")
        search_result_page = YoutubeSearchResultPage(self._driver)
        # clicking on the home page button in the search results page
        search_result_page.go_to_home()
        # verifying the page title
        home_page = YoutubeHomePage(self._driver)
        home_page_title = home_page.get_page_title(self._driver, "YouTube")
        # asserting the page title match the title of youtube home page
        self.assertEqual(home_page_title, "YouTube")

