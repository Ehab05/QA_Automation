import importlib
import json
import os

from selenium.webdriver.common.by import By
from the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    HEAD = "//h1[@class='heading']"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self._driver = driver
        self._head = driver.find_element(By.XPATH, self.HEAD)
        self.web_links = None

    def go_to_link(self, link):
        link_click = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//a[contains(text(),'{link}')]")))
        return link_click.click()

    def get_main_head(self):
        return self._head.text

    def count_links(self, locator):
        return len(self._driver.find_elements(*locator))

    def get_link_text(self, link_index):
        return self._driver.find_element(By.XPATH, f"//ul/li[{link_index}]").text

    def get_all_links(self, locator):
        links_cnt = self.count_links(locator)
        self.web_links = list(map(self.get_link_text, range(1, links_cnt + 1)))
        return self.web_links

    def write_links_to_json(self, links_data, file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            json.dump(links_data, f, indent=2)

    def json_file_links(self, main_page, locator, file_path):
        links_data = main_page.get_all_links(locator)
        self.write_links_to_json(links_data, file_path)

    def load_links_from_json(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data['links']

    def make_link_page(self, link: str):
        # Assume link is something like "broken_images"
        module_name = f"the_internet_herokuapp.logic.{link}_page"

        try:
            module = importlib.import_module(module_name)
            page_class_name = f"{link.capitalize()}Page"
            page_class = getattr(module, page_class_name)
            return page_class(self._driver)
        except (ModuleNotFoundError, AttributeError) as e:
            print(f"Page class '{page_class_name}' not found for link: {link}. Returning None. Error: {e}")
