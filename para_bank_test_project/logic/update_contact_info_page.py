import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from para_bank_test_project.infra.logger import Logger
from para_bank_test_project.infra.utils import Utils
from para_bank_test_project.logic.base_app_page import BaseAppPage


class UpdateContactInfoPage(BaseAppPage):
    PAGE_TITLE = "//div[@id='updateProfileForm']/h1[@class='title']"
    FIRST_NAME = "customer.firstName"
    LAST_NAME = "customer.lastName"
    ADDRESS = "customer.address.street"
    CITY = "customer.address.city"
    STATE = "customer.address.state"
    ZIP_CODE = "customer.address.zipCode"
    PHONE = "customer.phoneNumber"
    UPDATE_PROFILE_BUTTON = "//input[@class='button']"
    FIRS_NAME_ERROR_MESSAGE = "//span[@id='firstName-error']"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._driver = driver
        self._first_name = driver.find_element(By.ID, self.FIRST_NAME)
        self._last_name = driver.find_element(By.ID, self.LAST_NAME)
        self._address = driver.find_element(By.ID, self.ADDRESS)
        self._city = driver.find_element(By.ID, self.CITY)
        self._state = driver.find_element(By.ID, self.STATE)
        self._zip_code = driver.find_element(By.ID, self.ZIP_CODE)
        self._phone = driver.find_element(By.ID, self.PHONE)
        self._logger = Logger("ParaBank").get_logger()

    def insert_first_name(self, first_name: str) -> None:
        self._first_name = (WebDriverWait(self._driver, 10).until
                            (EC.visibility_of_element_located((By.ID, self.FIRST_NAME))))
        self._first_name.send_keys(first_name)

    def insert_last_name(self, last_name):
        self._last_name = (WebDriverWait(self._driver, 10).until
                           (EC.visibility_of_element_located((By.ID, self.LAST_NAME))))
        self._last_name.send_keys(last_name)

    def insert_address(self, address):
        self._address = (WebDriverWait(self._driver, 10).until
                         (EC.visibility_of_element_located((By.ID, self.ADDRESS))))
        self._address.send_keys(address)

    def insert_city(self, city):
        self._city = (WebDriverWait(self._driver, 10).until
                      (EC.visibility_of_element_located((By.ID, self.CITY))))
        self._city.send_keys(city)

    def insert_state(self, state):
        self._state = (WebDriverWait(self._driver, 10).until
                       (EC.visibility_of_element_located((By.ID, self.STATE))))
        self._state.send_keys(state)

    def insert_zip_code(self, zip_code):
        self._zip_code = (WebDriverWait(self._driver, 10).until
                          (EC.visibility_of_element_located((By.ID, self.ZIP_CODE))))
        self._zip_code.send_keys(zip_code)

    def insert_phone(self, phone):
        self._phone = (WebDriverWait(self._driver, 10).until
                       (EC.visibility_of_element_located((By.ID, self.PHONE))))
        self._phone.send_keys(phone)

    def click_update_profile_button(self):
        action = Utils.wait_for_action(WebDriverWait(self._driver, 10).until
                                       (EC.element_to_be_clickable((By.XPATH, self.UPDATE_PROFILE_BUTTON))), 2, 5)
        if action:
            self._driver.find_element(By.XPATH, self.UPDATE_PROFILE_BUTTON).click()
        else:
            self.logger().error(f"Failed to click the button")

    def update_profile_info_by_section(self, section, info_to_update):
        try:
            time.sleep(1)
            method = getattr(self, f"insert_{section}")
            element = getattr(self, f"_{section}")
            element.clear()
            method(info_to_update)
        except Exception as e:
            self.logger().error(f"Check the section name: {section} and the info to update: {info_to_update}")

    def get_first_name_error_message(self):
        message = (WebDriverWait(self._driver, 10).until
                   (EC.visibility_of_element_located((By.XPATH, self.FIRS_NAME_ERROR_MESSAGE))))
        return message.text
