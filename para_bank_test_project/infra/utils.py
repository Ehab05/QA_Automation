import random
import string
import time
from selenium.webdriver.chrome.webdriver import WebDriver


class Utils:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def generate_username(self, username_length: int) -> str:
        """
        Generating a random username that contains letters with the given length
        :param username_length:
        :return: Username
        """
        letters = string.ascii_letters
        return "".join(random.choice(letters) for _ in range(username_length))

    def generate_passwrod(self, password_length) -> str:
        """
            Generating a random password that contains digits and letters with the given length
            :param password_length:
            :return: Password
        """
        letters = string.ascii_letters + string.digits
        return "".join(random.choice(letters) for _ in range(password_length))

    def scramble_password(self, password):
        """
            This function get a password and rearrange the letters in a random way
            :param password:
            :return: Scrambled password
        """
        return "".join(random.sample(password, len(password)))

    def generate_amount(self, amount_range: tuple):
        """
        Generate a random amount within the given range
        :param amount_range: A tuple that contains the range (min, max).
        :return: random amount within the range
        """
        if not isinstance(amount_range, tuple) or len(amount_range) != 2:
            raise ValueError("The input must be a tuple of 2 numbers the first is the min value and the second is the "
                             "max value")
        min_amount, max_amount = amount_range
        if not (isinstance(min_amount, int) and isinstance(max_amount,int)):
            raise ValueError("The 2 values of the range should be integers")
        if min_amount > max_amount:
            raise ValueError("The first value should be less or equal than the second value")
        return random.randint(min_amount, max_amount)


    @staticmethod
    def wait_for_action(action, sleep_time, retries):
        """
            This function effectively uses sleep and wait for an action to be met for the given
            sleep time and a number of retries preventing waste of time
            :param action:
            :param sleep_time:
            :param retries:

        """

        result = action
        while retries > 0:
            if result:
                return result
            time.sleep(sleep_time)
            result = action
            retries -= 1
        return False
