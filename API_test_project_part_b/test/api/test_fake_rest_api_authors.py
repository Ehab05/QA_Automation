import unittest

from API_test_project_part_b.infra.api.apiwrapper import APIWrapper
from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.logic.api.authors import Authors


class TestFakeRestAPIAuthor(unittest.TestCase):

    def setUp(self):
        self._request = APIWrapper()
        self._config = ConfigProvider().load_from_file("../../fake_rest_config.json")

    def test_get_all_authors(self):
        authors = Authors(self._request).get_all_authors()
        self.assertEqual(200, authors.status_code)
        self.assertIsInstance(authors.json(), list)
        for author in authors.json():
            self.assertIsInstance(author, dict)
            self.assertEqual(self._config["number_of_author_values"], len(author))

    def test_update_author_by_id(self):
        update_author = Authors(self._request).update_author_by_id(self._config["author_to_update"]["id"])
        self.assertEqual(200, update_author.status_code)
        self.assertEqual(self._config["author_to_update"], update_author.json())

    def test_delete_author(self):
        authors = Authors(self._request).get_all_authors()
        author = Authors(self._request).delete_author_by_id(self._config["author_to_delete"])
        self.assertEqual(200, author.status_code)
        self.assertFalse(self._config["author_to_delete"] in authors.json())
