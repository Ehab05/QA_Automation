import requests
from API_test_project_part_b.infra.logger import Logger


class APIWrapper:

    def __init__(self):
        self._logger = Logger("fake_rest_API_log").get_logger()

    def get_request(self, url, body=None, params=None, headers=None):
        try:
            return requests.get(url)
        except requests.exceptions.HTTPError as e:
            self._logger.error(f"Error HTTP:{e}")
        except Exception as e:
            self._logger.error(f"Error: {e}")

    def post_request(self, url, body=None, headers=None):
        try:
            return requests.post(url, json=body, headers=headers)
        except requests.exceptions.HTTPError as e:
            self._logger.error(f"Error HTTP:{e}")
        except Exception as e:
            self._logger.error(f"Error: {e}")

    def put_request(self, url, body=None, headers=None):
        try:
            return requests.put(url, json=body, headers=headers)
        except requests.exceptions.HTTPError as e:
            self._logger.error(f"Error HTTP:{e}")
        except Exception as e:
            self._logger.error(f"Error: {e}")

    def delete_request(self, url, headers=None):
        try:
            return requests.delete(url, headers=headers)
        except requests.exceptions.HTTPError as e:
            self._logger.error(f"Error HTTP:{e}")
        except Exception as e:
            self._logger.error(f"Error: {e}")

