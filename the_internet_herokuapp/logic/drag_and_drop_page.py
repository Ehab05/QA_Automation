from selenium.webdriver.common.by import By

from the_internet_herokuapp.infra.base_page import BasePage
from selenium import webdriver


class DragAndDropPage(BasePage):
    COLUMN1 = 'column-a'
    COLUMN2 = 'column-B'
    COLUMN1_HEADER = "//div[@id='columns']/div[@class='column'][1]/header"

    def __init__(self, driver):
        super().__init__(driver)
        driver = webdriver.Chrome()
        driver.get('https://the-internet.herokuapp.com/')
        self._column1 = driver.find_element(By.ID, self.COLUMN1)
        self._column2 = driver.find_element(By.ID, self.COLUMN2)
        self._column1_header = driver.find_element(By.ID, self.COLUMN1_HEADER)

    def column(self, column_number):
        return self._driver.find_element(By.ID, f"self.COLUMN{column_number}")

    def column1_header(self):
        return self._column1_header

