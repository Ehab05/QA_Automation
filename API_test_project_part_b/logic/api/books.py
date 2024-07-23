from API_test_project_part_b.infra.api.apiwrapper import APIWrapper
from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.infra.logger import Logger
from API_test_project_part_b.logic.api.utils_logic import UtilsLogic


class Books:
    """
        This class contains functions that the user can use to perform CRUD operations
        on the Books section in the fake rest API website
    """

    def __init__(self, request: APIWrapper):
        """
            self._endpoint attribute returns the complete url for the endpoint
            APIWrapper This class provides methods for performing HTTP GET, POST, PUT, and DELETE requests.
        """
        self._request = request
        self._endpoint = UtilsLogic().get_url_with_endpoint("Books")
        self._config = ConfigProvider().load_from_file("../../fake_rest_config.json")
        self._logger = Logger("fake_rest_api.log").get_logger()

    def get_all_books(self):
        try:
            response = self._request.get_request(self._endpoint)
            return response
        except Exception as e:
            self._logger.error(f"Error getting all books")
            return None

    def get_book_by_id(self, book_id):
        try:
            response = self._request.get_request(f"{self._endpoint}/{book_id}")
            return response
        except Exception as e:
            self._logger.error(f"Error getting the book by id:{e}")
            return None

    def post_book(self, valid_book):
        try:
            response = self._request.post_request(self._endpoint, valid_book)
            return response
        except Exception as e:
            self._logger.error(f"Error posting activity: {e}")
            return None

    def update_book_by_id(self, book_id, valid_book):
        try:
            response = self._request.put_request(f"{self._endpoint}/{book_id}", valid_book)
            return response
        except Exception as e:
            self._logger.error(f"Error updating book by id: {e}")
            return None

    def delete_book_by_id(self, book_id):
        try:
            headers = {"Content-Type": "application/json"}
            response = self._request.delete_request(f"{self._endpoint}/{book_id}", headers=headers)
            return response
        except Exception as e:
            self._logger.error(f"Error deleting book by id: {e}")
            return None

