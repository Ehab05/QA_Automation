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

    def test_post_activity(self):
        activity = Activities(self._request)
        response = activity.post_activity()
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.json().get('completed'))

    def test_update_activity_by_id(self):
        activity = Activities(self._request)
        response = activity.update_activity(self._config["activity_1"]["id"])
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.json().get('completed'))
        self.assertEqual(self._config["activity_to_update"]["title"], response.json().get("title"))






