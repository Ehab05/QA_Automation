from API_test_project_part_b.infra.api.apiwrapper import APIWrapper
from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.logic.api.entries.book_entry import BookEntry
from API_test_project_part_b.logic.api.utils_logic import Utils


class Books:
    def __init__(self, request: APIWrapper):
        super().__init__()
        self._request = request
        self._endpoint = Utils().get_url_with_endpoint("Books")
        self._config = ConfigProvider().load_from_file("../../fake_rest_config.json")

    def get_all_books(self):
        response = self._request.get_request(self._endpoint)
        return response

    def get_book_by_id(self, book_id):
        response = self._request.get_request(f"{self._endpoint}/{book_id}")
        return response.json()

    def post_book(self):
        book = BookEntry(self._config["book_1"])
        response = self._request.post_request(self._endpoint, book)
        return response

    def update_book_by_id(self, book_id):
        book_update = BookEntry(self._config["book_to_update"])
        response = self._request.put_request(f"{self._endpoint}/{book_id}", book_update.book_to_dict())
        return response

    def delete_book_by_id(self, book_id):
        headers = {"Content-Type": "application/json"}
        response = self._request.delete_request(f"{self._endpoint}/{book_id}", headers=headers)
        print(self._request)
        return response
