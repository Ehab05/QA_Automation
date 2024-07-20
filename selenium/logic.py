from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class SearchGoogle:
    def __init__(self, driver):
        self.driver = driver

    def search_by_text(self, search_text):
        search_field = self.driver.find_element(By.NAME, "q")
        search_field.send_keys(search_text, Keys.RETURN)

    @staticmethod
    def check_text_in_search_result(self, text, search_result):
        return text in search_result

    def check_search_results(self, text_to_check):
        search_result = self.driver.find_elements(By.CSS_SELECTOR, "h3")
        filterd_results = filter(lambda result: text_to_check in result.text, search_result)
        if filterd_results is not []:
            return text_to_check
        return False

