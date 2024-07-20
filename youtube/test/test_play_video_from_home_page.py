import unittest
from youtube.infra.browser_wrapper import BrowserWrapper
from youtube.logic.youtube_home_page import YoutubeHomePage
from youtube.logic.youtube_search_result_page import YoutubeSearchResultPage
from youtube.logic.youtube_video_page import VideoPage


class TestVideoPage(unittest.TestCase):
    def setUp(self):
        self._driver = BrowserWrapper().get_driver()

    def tearDown(self):
        self._driver.quit()

    def test_play_video_from_home_page(self):
        """
            test case 005: play a video from the home page
            Perform a search using valid search input
            Navigate to the video page and verify that the video plays successfully
        """
        # initialize youtube home page
        home_page = YoutubeHomePage(self._driver)
        # searching with a valid input
        home_page.search_for("health")
        search_result_page = YoutubeSearchResultPage(self._driver)
        # Verifying the video title from the search results page and video page
        video_title_from_search_results = search_result_page.get_video_title()
        search_result_page.click_on_video_title()
        video_page = VideoPage(self._driver)
        video_title_from_video_page = video_page.get_video_title()
        # asserting that the title in the video page math the title that was clicked
        self.assertEqual(video_title_from_search_results, video_title_from_video_page)


