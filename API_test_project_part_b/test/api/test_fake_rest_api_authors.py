import unittest
from API_test_project_part_b.infra.api.apiwrapper import APIWrapper
from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.infra.utils import Utils
from API_test_project_part_b.logic.api.authors import Authors
from API_test_project_part_b.logic.api.entries.author_entry import AuthorEntry


class TestFakeRestAPIAuthor(unittest.TestCase):

    def setUp(self):
        """
            APIWrapper This class provides methods for performing HTTP GET, POST, PUT, and DELETE requests.
        """
        self._request = APIWrapper()
        self._config = ConfigProvider().load_from_file("../../fake_rest_config.json")

    def test_get_all_authors(self):
        """
            Test case: 007
            Verify successful fetching of all Authors
        """
        # Getting all authors from the API
        authors = Authors(self._request).get_all_authors()

        # Asserting the response status code and type
        self.assertEqual(200, authors.status_code)
        self.assertIsInstance(authors.json(), list)
        # iterating on the response list and asserting response bodies type and number of fields
        for author in authors.json():
            self.assertIsInstance(author, dict)
            self.assertEqual(self._config["number_of_author_keyvalues"], len(author))

    def test_get_author_by_id(self):
        """
            Test case: 008
            Verify successful fetching of an author by its ID
        """
        # Generating a random author ID within the accepted range
        author_id = Utils().generate_random_number_within_range(tuple(self._config["author_id_range"]))

        # Getting the author by its id
        author = Authors(self._request).get_author_by_id(author_id)

        # Asserting the response status code
        self.assertEqual(200, author.status_code)
        # Asserting that the response body id matched the given id with the request
        self.assertTrue(author.json()["id"] == author_id)
        # Asserting the response body idbook and firstname type
        self.assertIsInstance(author.json()["idBook"], int)
        self.assertIsInstance(author.json()["firstName"], str)

    def test_post_valid_author(self):
        """
            Test case: 009
            Verify successful adding of a new valid author
        """
        # Initialize valid author to post
        author = Authors(self._request)
        # Generating a valid author
        valid_author = AuthorEntry().author_to_dict()

        # Posting the generated author
        response = author.post_author(valid_author)

        # Asserting the response status code
        self.assertEqual(200, response.status_code)
        # Asserting the response body id type
        self.assertIsInstance(response.json()["id"], int)

    def test_update_author_by_id(self):
        """
            Test case: 010
            Verify successful update of an author by its ID with valid data
        """
        # initialize author from performing HTTP requests
        author = Authors(self._request)
        # Generating a random author ID within the accepted range
        author_id = Utils().generate_random_number_within_range(tuple(self._config["author_id_range"]))
        # Generating data for updating the author with the given id
        updated_author = AuthorEntry().updated_author_by_id(author_id)

        # Updating the new data for the author
        response = author.update_author_by_id(author_id, updated_author)

        # Asserting the response status code
        self.assertEqual(200, response.status_code)
        # Asserting if the response body match the newly updated data
        self.assertDictEqual(updated_author, response.json())

    def test_delete_author(self):
        """
            Test case: 011
            Verify successful deletion of an author by its ID
        """
        # Getting all authors for the successful deletion check
        authors = Authors(self._request).get_all_authors()
        # Generating a random author ID within the accepted range
        author_id = Utils().generate_random_number_within_range(tuple(self._config["author_id_range"]))

        # Deleting the author by its id
        author = Authors(self._request).delete_author_by_id(author_id)

        # Asserting the response status code for the get and delete requests
        self.assertEqual(200, authors.status_code)
        self.assertEqual(200, author.status_code)
        # Asserting that after deletion the deleted author is not in the authors list
        self.assertFalse(author_id in authors.json())
