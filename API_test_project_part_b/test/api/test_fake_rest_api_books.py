import unittest

from API_test_project_part_b.infra.api.apiwrapper import APIWrapper
from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.logic.api.books import Books
from API_test_project_part_b.logic.api.utils_logic import Utils


class TestFakeRestAPIBooks(unittest.TestCase):
    def setUp(self):
        self._request = APIWrapper()
        self._config = ConfigProvider().load_from_file("../../fake_rest_config.json")

    def test_get_all_books(self):
        books = Books(self._request).get_all_books()
        self.assertEqual(200, books.status_code)
        self.assertIsInstance(books.json(), list)
        for book in books.json():
            self.assertIsInstance(book, dict)
            self.assertEqual(self._config["number_of_book_keyvalues"], len(book))

    def test_get_book_by_id(self):
        book = Books(self._request).get_book_by_id(self._config["get_book_id"])
        self.assertEqual(200, book.status_code)
        self.assertTrue(book.json()["id"] == self._config["get_book_id"])
        self.assertIsInstance(book.json()["title"], str)
        self.assertIsInstance(book.json()["pageCount"], int)

    def test_post_book(self):
        book = Books(self._request)
        response = book.post_book()
        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.json().get("id"), int)

    def test_update_book_by_id(self):
        update_book = Books(self._request).update_book_by_id(self._config["book_to_update"]["id"])
        self.assertEqual(200, update_book.status_code)
        self.assertDictEqual(self._config["book_to_update"], update_book.json())

    def test_delete_book(self):
        books = Books(self._request).get_all_books()
        book = Books(self._request).delete_book_by_id(self._config["book_to_delete"])
        self.assertEqual(200, book.status_code)
        self.assertFalse(self._config["book_to_delete"] in books.json())


