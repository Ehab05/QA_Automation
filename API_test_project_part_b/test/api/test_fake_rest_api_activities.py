import unittest
from API_test_project_part_b.infra.api.apiwrapper import APIWrapper
from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.logic.api.activities import Activities


class TestFakeRestAPIActivities(unittest.TestCase):
    def setUp(self):
        self._request = APIWrapper()
        self._config = ConfigProvider().load_from_file("../../fake_rest_config.json")

    def test_get_all_activities(self):
        all_activities = Activities(self._request).get_all_activities()
        self.assertEqual(200, all_activities.status_code)
        self.assertIsInstance(all_activities.json(), list)

    def test_get_activity_by_id(self):
        activity = Activities(self._request).get_activity_by_id(self._config["get_activity_id"])
        self.assertEqual(200, activity.status_code)
        self.assertTrue(activity.json()["id"] == self._config["get_activity_id"])
        self.assertIsInstance(activity.json()["id"], int)
        self.assertIsInstance(activity.json()["title"], str)

    def test_post_activity_with_valid_data(self):
        activity = Activities(self._request)
        response = activity.post_activity(self._config["valid_activity_1"])
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.json().get('completed'))

    def test_post_activity_with_invalid_data(self):
        activity = Activities(self._request)
        response = activity.post_activity(self._config["invalid_activity_1"])
        self.assertEqual(400, response.status_code)
        self.assertTrue(self._config["error_message"] in response.json())
        self.assertIsNotNone(response.json()["errors"])

    def test_update_activity_by_id(self):
        activity = Activities(self._request)
        response = activity.update_activity(self._config["activity_1"]["id"])
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.json().get('completed'))
        self.assertEqual(self._config["activity_to_update"]["title"], response.json().get("title"))

    def test_delete_activity(self):
        activities = Activities(self._request).get_all_activities()
        activity = Activities(self._request).delete_activity_by_id(self._config["activity_to_delete"])
        self.assertEqual(200, activities.status_code)
        self.assertEqual(200, activity.status_code)
        self.assertFalse(self._config["activity_to_delete"] in activities.json())





