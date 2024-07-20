from API_test_project_part_b.infra.api.apiwrapper import APIWrapper
from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.logic.api.entries.post_author import PostAuthor
from API_test_project_part_b.logic.api.entries.update_author import UpdateAuthor
from API_test_project_part_b.logic.api.utils_logic import Utils


class Authors:
    def __init__(self, request: APIWrapper):
        super().__init__()
        self._request = request
        self._endpoint = Utils().get_url_with_endpoint("Authors")
        self._config = ConfigProvider().load_from_file("../../fake_rest_config.json")

    def get_all_authors(self):
        response = self._request.get_request(self._endpoint)
        return response

    def get_author_by_id(self, author_id):
        response = self._request.get_request(f"{self._endpoint}/{author_id}")
        return response.json()

    def post_author(self):
        author = PostAuthor(self._config["author_1"])
        response = self._request.post_request(self._endpoint, author)
        return response

    def update_author_by_id(self, author_id):
        author_update = UpdateAuthor(self._config["author_to_update"])
        response = self._request.put_request(f"{self._endpoint}/{author_id}", author_update.author_to_dict())
        return response

    def delete_author_by_id(self, author_id):
        headers = {"Content-Type": "application/json"}
        response = self._request.delete_request(f"{self._endpoint}/{author_id}", headers=headers)
        print(self._request)
        return response

