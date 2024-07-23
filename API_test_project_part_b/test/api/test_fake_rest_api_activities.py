import unittest
from API_test_project_part_b.infra.api.apiwrapper import APIWrapper
from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.infra.utils import Utils
from API_test_project_part_b.logic.api.activities import Activities
from API_test_project_part_b.logic.api.entries.activity_entry import ActivityEntry


class TestFakeRestAPIActivities(unittest.TestCase):
    def setUp(self):
        """
            APIWrapper This class provides methods for performing HTTP GET, POST, PUT, and DELETE requests.
        """
        self._request = APIWrapper()
        self._config = ConfigProvider().load_from_file("../../fake_rest_config.json")

    def test_get_all_activities(self):
        """
            Test case: 001
            Verify successful fetching of all activities
        """
        # Getting all the activities from the API
        all_activities = Activities(self._request).get_all_activities()

        # Asserting response status code of the Get request and the type of the response body
        self.assertEqual(200, all_activities.status_code)
        self.assertIsInstance(all_activities.json(), list)

    def test_get_activity_by_id(self):
        """
            Test case: 002
            Verify successful fetching of an activity by its ID
        """
        # Generating a random activity ID within the accepted range
        activity_id = Utils().generate_random_number_within_range(tuple(self._config["activity_id_range"]))

        # Getting the activity by its id
        activity = Activities(self._request).get_activity_by_id(activity_id)

        # Asserting the response status code and the id field and title field in the response body
        self.assertEqual(200, activity.status_code)
        self.assertTrue(activity.json()["id"] == activity_id)
        self.assertIsInstance(activity.json()["id"], int)
        self.assertIsInstance(activity.json()["title"], str)

    def test_post_activity_with_valid_data(self):
        """
            Test case: 003
            Verify successful adding of a new valid activity
        """
        # Initialize valid activity to post
        activity = Activities(self._request)
        # Generating a valid activity
        valid_activity = ActivityEntry().activity_to_dict()

        # Updating the new data of the activity
        response = activity.post_activity(valid_activity)

        # Asserting the response status code of the response and the "completed" field in the response body
        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.json().get('completed'), bool)

    def test_post_activity_with_invalid_data(self):
        """
            Test case: 004
            Verify successful error message with adding of a new activity with invalid data
        """
        # Initialize invalid activity to post
        activity = Activities(self._request)
        invalid_activity = ActivityEntry().get_invalid_activity()

        # Posting the new data of the activity
        response = activity.post_activity(invalid_activity)

        # Asserting the response status code of the response and the error message in the response body
        self.assertEqual(400, response.status_code)
        self.assertTrue(self._config["error_message"] in response.json())
        self.assertIsNotNone(response.json()["errors"])

    def test_update_activity_by_id(self):
        """
            Test case: 005
            Verify successful update of an activity by its ID with valid data
        """
        activity = Activities(self._request)
        # Generating a random activity ID within the accepted range
        activity_id = Utils().generate_random_number_within_range(tuple(self._config["activity_id_range"]))
        # Initialize valid activity to update
        updated_activity = ActivityEntry().updated_activity(activity_id)

        # Updating the new data for the activity by the chosen id
        response = activity.update_activity_by_id(activity_id, updated_activity)

        # Asserting the response status code and completed and title fields of the response body
        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.json().get('completed'), bool)
        self.assertEqual(updated_activity["title"], response.json().get("title"))

    def test_delete_activity(self):
        """
            Test case: 006
            Verify successful deletion of an activity by its ID
        """
        # Getting all the activities for the successful deletion check
        activities = Activities(self._request).get_all_activities()
        # Generating a random activity ID within the accepted range
        activity_id = Utils().generate_random_number_within_range(tuple(self._config["activity_id_range"]))

        # Deleting the activity by its ID
        activity = Activities(self._request).delete_activity_by_id(activity_id)

        # Asserting the status codes of the GET response and DELETE response
        self.assertEqual(200, activities.status_code)
        self.assertEqual(200, activity.status_code)
        # Asserting that after deletion the deleted activity is not in the activity list
        self.assertFalse(activity_id in activities.json())





