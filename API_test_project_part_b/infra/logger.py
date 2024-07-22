import logging
import os


class Logger:

    def __init__(self, name):
        """
        setting up logger class for a project use
        :param name:
        """
        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s \n- %(module)s - %(filename)s - %("
                                      "funcName)s - %(message)s")
        log_file_path = os.path.join("../../" 'fake_rest_api.log')
        handler = logging.FileHandler(log_file_path)
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

    def get_logger(self):
        return self._logger
