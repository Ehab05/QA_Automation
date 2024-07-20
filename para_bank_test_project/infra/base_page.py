from para_bank_test_project.infra.logger import Logger


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self._logger = Logger(self.__class__.__name__).get_logger()

    def logger(self):
        return self._logger
