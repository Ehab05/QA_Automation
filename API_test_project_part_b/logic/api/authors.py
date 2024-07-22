from API_test_project_part_b.infra.api.apiwrapper import APIWrapper
from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.logic.api.entries.author_entry import AuthorEntry
from API_test_project_part_b.logic.api.utils_logic import Utils


class Authors:
    """
        This class contains functions that the user can use to perform CRUD operations
        on the Authors section in the fake rest API website
    """
    def __init__(self, request: APIWrapper):
        """
            self._endpoint attribute returns the complete url for the endpoint
            APIWrapper This class provides methods for performing HTTP GET, POST, PUT, and DELETE requests.
        """
        self._request = request
        self._endpoint = Utils().get_url_with_endpoint("Authors")
        self._config = ConfigProvider().load_from_file("../../fake_rest_config.json")

    def get_all_authors(self):
        response = self._request.get_request(self._endpoint)
        return response

    def get_author_by_id(self, author_id):
        response = self._request.get_request(f"{self._endpoint}/{author_id}")
        return response

    def post_author(self):
        author = AuthorEntry(self._config["author_1"])
        response = self._request.post_request(self._endpoint, author.author_to_dict())
        return response

    def update_author_by_id(self, author_id):
        author_update = AuthorEntry(self._config["author_to_update"])
        response = self._request.put_request(f"{self._endpoint}/{author_id}", author_update.author_to_dict())
        return response

    def delete_author_by_id(self, author_id):
        headers = {"Content-Type": "application/json"}
        response = self._request.delete_request(f"{self._endpoint}/{author_id}", headers=headers)
        print(self._request)
        return response


