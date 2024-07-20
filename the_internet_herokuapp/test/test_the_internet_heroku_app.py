from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from the_internet_herokuapp.infra.browser_wrapper import BrowserWrapper
from the_internet_herokuapp.logic.add_remove_page import AddRemovePage
from the_internet_herokuapp.logic.challenging_dom_page import ChallengingDomPage
from the_internet_herokuapp.logic.main_page import MainPage
from the_internet_herokuapp.infra.base_page import BasePage


class TestHerokuApp:
    def setup_driver(self):
        self._driver = BrowserWrapper().get_driver()

    def teardown_driver(self):
        if self._driver:
            self._driver.quit()

    def test_challenging_dom_page(self):
        self.setup_driver()
        main_page = MainPage(self._driver)
        main_page.go_to_link('Challenging DOM')
        challenging_dom_page = ChallengingDomPage(self._driver)
        button = challenging_dom_page.get_button()
        dynamic_button = challenging_dom_page.get_dynamic_button(button)
        assert dynamic_button.text in ['bar', 'foo', 'baz', 'qux']
        self.teardown_driver()

    def test_main_page(self):
        self.setup_driver()
        main_page = MainPage(self._driver)
        locator = (By.XPATH, '//ul/li')
        links = main_page.get_all_links(locator)
        for link in links:
            main_page.go_to_link(link)
            link_page = main_page.make_link_page(link)
            if link_page:
                assert link == link_page.page_head()
        self.teardown_driver()

    def test_add_remove_page_delete_1_button(self):
        self.setup_driver()
        main_page = MainPage(self._driver)
        main_page.go_to_link('Add/Remove Elements')
        add_remove_page = AddRemovePage(self._driver)
        add_remove_page.add_element()
        add_remove_page.delete_button(0)
        assert add_remove_page.number_of_delete_buttons() == 1
        self.teardown_driver()

    def test_add_remove_page_delete_2_button(self):
        self.setup_driver()
        main_page = MainPage(self._driver)
        main_page.go_to_link('Add/Remove Elements')
        add_remove_page = AddRemovePage(self._driver)
        add_remove_page.add_element()
        add_remove_page.add_element()
        add_remove_page.delete_button(1)
        add_remove_page.delete_button(1)
        assert add_remove_page.number_of_delete_buttons() == 1
        self.teardown_driver()


