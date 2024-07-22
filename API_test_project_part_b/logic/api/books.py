from API_test_project_part_b.infra.api.apiwrapper import APIWrapper
from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.logic.api.entries.book_entry import BookEntry
from API_test_project_part_b.infra.utils import Utils
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

    def get_all_books(self):
        response = self._request.get_request(self._endpoint)
        return response

    def get_book_by_id(self, book_id):
        response = self._request.get_request(f"{self._endpoint}/{book_id}")
        return response

    def post_book(self, valid_book):
        response = self._request.post_request(self._endpoint, valid_book)
        return response

    def update_book_by_id(self, book_id, valid_book):
        response = self._request.put_request(f"{self._endpoint}/{book_id}", valid_book)
        return response

    def delete_book_by_id(self, book_id):
        headers = {"Content-Type": "application/json"}
        response = self._request.delete_request(f"{self._endpoint}/{book_id}", headers=headers)
        print(self._request)
        return response
