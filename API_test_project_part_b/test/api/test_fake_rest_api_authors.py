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
            self.assertEqual(self._config["number_of_author_keyvalues"], len(author))

    def test_get_author_by_id(self):
        author = Authors(self._request).get_author_by_id(self._config["get_author_id"])
        self.assertEqual(200, author.status_code)
        self.assertTrue(author.json()["id"] == self._config["get_author_id"])
        self.assertIsInstance(author.json()["idBook"], int)
        self.assertIsInstance(author.json()["firstName"], str)

    def test_post_author(self):
        book = Authors(self._request)
        response = book.post_author()
        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.json().get("id"), int)

    def test_update_author_by_id(self):
        update_author = Authors(self._request).update_author_by_id(self._config["author_to_update"]["id"])
        self.assertEqual(200, update_author.status_code)
        self.assertDictEqual(self._config["author_to_update"], update_author.json())

    def test_delete_author(self):
        authors = Authors(self._request).get_all_authors()
        author = Authors(self._request).delete_author_by_id(self._config["author_to_delete"])
        self.assertEqual(200, authors.status_code)
        self.assertEqual(200, author.status_code)
        self.assertFalse(self._config["author_to_delete"] in authors.json())
