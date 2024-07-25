import os
import unittest
from API_test_project_part_b.infra.api.api_wrapper import APIWrapper
from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.infra.utils import Utils
from API_test_project_part_b.logic.api.books import Books
from API_test_project_part_b.logic.api.entries.book_entity import BookEntity


class TestFakeRestAPIBooks(unittest.TestCase):
    def setUp(self):
        self._request = APIWrapper()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(base_dir, '../../fake_rest_config.json')
        self._config = ConfigProvider.load_from_file(config_file_path)

    def test_get_all_books(self):
        """
            Test case: 012
            Verify successful fetching of all Books
        """
        # Getting all authors from the API
        books = Books(self._request).get_all_books()

        # Asserting the response status code and type
        self.assertEqual(200, books.status_code)
        self.assertIsInstance(books.data, list)
        # iterating on the response list and asserting response bodies type and number of fields
        for book in books.data:
            self.assertIsInstance(book, dict)
            self.assertEqual(self._config["number_of_book_keyvalues"], len(book))

    def test_get_book_by_id(self):
        """
            Test case: 013
            Verify successful fetching of an author by its ID
        """
        # Generating a random book ID within the accepted range
        book_id = Utils().generate_random_number_within_range(tuple(self._config["book_id_range"]))
        # Getting the book by its id

        book = Books(self._request).get_book_by_id(book_id)

        # Asserting the response status code
        self.assertEqual(200, book.status_code)
        # Asserting that the response body id matched the given id with the request
        self.assertTrue(book.data["id"] == book_id)
        # Asserting the response body title and pageCount type
        self.assertIsInstance(book.data["title"], str)
        self.assertIsInstance(book.data["pageCount"], int)

    def test_post_book(self):
        """
            Test case: 014
            Verify successful adding of a new valid author
        """
        # Initialize valid book to post
        book = Books(self._request)
        # Generating a valid book
        valid_book = BookEntity().book_to_dict()

        # Posting the generated book
        response = book.post_book(valid_book)

        # Asserting the response status code
        self.assertEqual(200, response.status_code)
        # Asserting the response body id type
        self.assertIsInstance(response.data["id"], int)

    def test_update_book_by_id(self):
        """
            Test case: 015
            Verify successful update of a book by its ID with valid data
        """
        # initialize author from performing HTTP requests
        book = Books(self._request)
        # Generating a random book ID within the accepted range
        book_id = Utils().generate_random_number_within_range(tuple(self._config["book_id_range"]))

        # Generating data for updating the book with the given id
        update_book = BookEntity().updated_book_by_id(book_id)
        # Updating new data for the book
        response = book.update_book_by_id(book_id, update_book)

        # Asserting the response status code
        self.assertEqual(200, response.status_code)
        # Asserting if the response body match the newly updated data
        self.assertDictEqual(update_book, response.data)

    def test_delete_book(self):
        """
            Test case: 016
            Verify successful deletion of a book by its ID
        """
        # Getting all books for the successful deletion check
        books = Books(self._request).get_all_books()
        # Generating a random book ID within the accepted range
        book_id = Utils().generate_random_number_within_range(tuple(self._config["book_id_range"]))

        # Deleting the author by its ID
        book = Books(self._request).delete_book_by_id(book_id)

        self.assertEqual(200, book.status_code)
        self.assertFalse(book_id in books.data)
