from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from para_bank_test_project.infra.config_provider import ConfigProvider
from para_bank_test_project.infra.utils import Utils
from para_bank_test_project.logic.base_app_page import BaseAppPage
from para_bank_test_project.logic.utils_logic import UtilsLogic


class RegisterPage(BaseAppPage):
    FIRST_NAME = "customer.firstName"
    LAST_NAME = "customer.lastName"
    ADDRESS = "customer.address.street"
    CITY = "customer.address.city"
    STATE = "customer.address.state"
    ZIP_CODE = "customer.address.zipCode"
    PHONE = "customer.phoneNumber"
    SSN = "customer.ssn"
    USER_NAME = "customer.username"
    PASSWORD = "customer.password"
    CONFIRM_PASSWORD = "repeatedPassword"
    REGISTER_BUTTON = "//input[@class='button' and @value='Register']"
    PASSWORD_ERROR_MESSAGE = "//span[@id='repeatedPassword.errors']"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._utils = Utils(self._driver)
        self.config = ConfigProvider.load_from_file('../config_parabank.json')
        self._first_name = driver.find_element(By.ID, self.FIRST_NAME)
        self._last_name = driver.find_element(By.ID, self.LAST_NAME)
        self._address = driver.find_element(By.ID, self.ADDRESS)
        self._city = driver.find_element(By.ID, self.CITY)
        self._state = driver.find_element(By.ID, self.STATE)
        self._zip_code = driver.find_element(By.ID, self.ZIP_CODE)
        self._phone = driver.find_element(By.ID, self.PHONE)
        self._ssn = driver.find_element(By.ID, self.SSN)
        self._user_name = driver.find_element(By.ID, self.USER_NAME)
        self._password = driver.find_element(By.ID, self.PASSWORD)
        self._confirm_password = driver.find_element(By.ID, self.CONFIRM_PASSWORD)
        self._register_button = driver.find_element(By.XPATH, self.REGISTER_BUTTON)

    def insert_first_name(self, first_name: str) -> None:
        try:
            self._first_name.send_keys(first_name)
        except Exception as e:
            self.logger().error(f"Failed to insert the input:{e}")

    def insert_last_name(self, last_name):
        try:
            self._last_name.send_keys(last_name)
        except Exception as e:
            self.logger().error(f"Failed to insert the input:{e}")

    def insert_address(self, address):
        try:
            self._address.send_keys(address)
        except Exception as e:
            self.logger().error(f"Failed to insert the input:{e}")

    def insert_city(self, city):
        try:
            self._city.send_keys(city)
        except Exception as e:
            self.logger().error(f"Failed to insert the input:{e}")

    def insert_state(self, state):
        try:
            self._state.send_keys(state)
        except Exception as e:
            self.logger().error(f"Failed to insert the input:{e}")

    def insert_zip_code(self, zip_code):
        try:
            self._zip_code.send_keys(zip_code)
        except Exception as e:
            self.logger().error(f"Failed to insert the input:{e}")

    def insert_phone(self, phone):
        try:
            self._phone.send_keys(phone)
            self.logger().info(f"The phone number for registration is:{phone}")
        except Exception as e:
            self.logger().error(f"Failed to insert the input:{e}")

    def insert_ssn(self, ssn):
        try:
            self._ssn.send_keys(ssn)
        except Exception as e:
            self.logger().error(f"Failed to insert the input:{e}")

    def insert_user_name(self, user_name, config):
        try:
            config['user'] = user_name
            self.logger().info(f"The user name for registration is:{user_name}")
            self._user_name.send_keys(user_name)
            UtilsLogic.save_to_file('../config_parabank.json', config)
        except Exception as e:
            self.logger().error(f"Failed to insert the input:{e}")

    def insert_password(self, password, config):
        try:
            config['password'] = password
            self.logger().info(f"The password for registration is:{password}")
            self._password.send_keys(password)
            UtilsLogic.save_to_file('../config_parabank.json', config)
        except Exception as e:
            self.logger().error(f"Failed to insert the input:{e}")

    def insert_confirm_password(self, confirm_password):
        try:
            self._confirm_password.send_keys(confirm_password)
            self.logger().info(f"The confirmation password for registration is:{confirm_password}")
        except Exception as e:
            self.logger().error(f"Failed to insert the input:{e}")

    def click_register_button(self):
        try:
            self._register_button.click()
        except Exception as e:
            self.logger().error(f"Failed to click the register button:{e}")

    def get_password_mismatch_message(self):
        password_mismatch_message = WebDriverWait(self._driver, 12).until(
            EC.presence_of_element_located((By.XPATH, self.PASSWORD_ERROR_MESSAGE)))
        return password_mismatch_message.text

    def register_flow_from_config(self, config):
        self.insert_first_name(config.get("first_name"))
        self.insert_last_name(config.get("last_name"))
        self.insert_address(config.get("address"))
        self.insert_city(config.get("city"))
        self.insert_state(config.get("state"))
        self.insert_zip_code(config.get("zip_code"))
        self.insert_phone(config.get("phone"))
        self.insert_ssn(config.get("ssn"))
        user = self._utils.generate_username(5)
        self.logger().info(f"The username that was generated for registration is:{user}")
        self.insert_user_name(user, config)
        password = self._utils.generate_passwrod(8)
        self.logger().info(f"The password that was generated for registration is:{password}")
        self.insert_password(password, config)
        self.insert_confirm_password(password)
        self.click_register_button()
