import unittest

from youtube.infra.browser_wrapper import BrowserWrapper
from youtube.logic.youtube_home_page import YoutubeHomePage
from youtube.logic.youtube_shorts_page import ShortsPage


class TestShortsPage(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserWrapper().get_driver()

    def tearDown(self):
        self._driver.quit()

    def test_go_to_shorts_page(self):
        """
         test case 001: Navigate to shorts page from Youtube home page through the visible left menu
         testing user navigation to shorts page from the Youtube home
         page by clicking on the shorts icon in the home page
        """
        # initialize youtube home page
        home_page = YoutubeHomePage(self._driver)
        # navigating to the shorts page
        home_page.go_to_shorts_page()
        shorts_page = ShortsPage(self._driver)
        # verifying successful navigation to the shorts page
        shorts_page_id = shorts_page.get_container_id()
        expected_result = shorts_page.CONTAINER_ID
        # asserting if the result page match the shorts page
        self.assertEqual(shorts_page_id, expected_result)

