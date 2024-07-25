import os

from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.infra.utils import Utils


class AuthorEntity:
    def __init__(self):
        """
            This class initialize a random activity
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(base_dir, '../../../fake_rest_config.json')
        self._config = ConfigProvider.load_from_file(config_file_path)
        self._id = Utils().generate_random_number_within_range(tuple(self._config["author_id_range"]))
        self._idbook = Utils().generate_random_number_within_range(tuple(self._config["idbook_range"]))
        self._first_name = Utils().generate_random_string(8)
        self._last_name = Utils().generate_random_string(8)

    @property
    def id(self):
        return self._id

    @property
    def idbook(self):
        return self._idbook

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def author_to_dict(self):
        return {
            "id": self._id,
            "idBook": self._idbook,
            "firstName": self._first_name,
            "lastName": self._last_name
        }

    def updated_author_by_id(self, author_id):
        """
            This function generate a random author with the same given ID
        """
        return {
            "id": author_id,
            "idBook": self._idbook,
            "firstName": self._first_name,
            "lastName": self._last_name
        }
