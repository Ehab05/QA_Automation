import os

from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.infra.utils import Utils


class BookEntity:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(base_dir, '../../../fake_rest_config.json')
        self._config = ConfigProvider.load_from_file(config_file_path)
        self._id = Utils().generate_random_number_within_range(tuple(self._config["book_id_range"]))
        self._title = Utils().generate_random_string(8)
        self._description = Utils().generate_random_string(8)
        self._pageCount = Utils().generate_random_number_within_range(tuple(self._config["pagecount_range"]))
        self._excerpt = Utils().generate_random_string(8)
        self._publishDate = Utils().generate_random_iso_datetime()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def pageCount(self):
        return self._pageCount

    @property
    def excerpt(self):
        return self._excerpt

    @property
    def publishDate(self):
        return self._publishDate

    def book_to_dict(self):
        return {
            "id": self._id,
            "title": self._title,
            "description": self._description,
            "pageCount": self._pageCount,
            "excerpt": self._excerpt,
            "publishDate": self._publishDate
        }

    def updated_book_by_id(self, book_id):
        return {
            "id": book_id,
            "title": self._title,
            "description": self._description,
            "pageCount": self._pageCount,
            "excerpt": self._excerpt,
            "publishDate": self._publishDate
        }