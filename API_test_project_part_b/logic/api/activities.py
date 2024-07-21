from API_test_project_part_b.infra.api.apiwrapper import APIWrapper
from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.logic.api.entries.activity_entry import ActivityEntry

from API_test_project_part_b.logic.api.utils_logic import Utils


class Activities:
    def __init__(self, request: APIWrapper):
        self._request = request
        self._endpoint = Utils().get_url_with_endpoint("Activities")
        self._config = ConfigProvider().load_from_file("../../fake_rest_config.json")

    def get_all_activities(self):
        response = self._request.get_request(self._endpoint)
        return response

    def post_activity(self, valid_data):
        activity = ActivityEntry(valid_data)
        response = self._request.post_request(self._endpoint, activity.activity_to_dict())
        return response

    def get_activity_by_id(self, activity_id):
        response = self._request.get_request(f"{self._endpoint}/{activity_id}")
        return response

    def update_activity(self, activity_id):
        response = self._request.put_request(f"{self._endpoint}/{activity_id}", self._config["activity_to_update"])
        return response

    def delete_activity_by_id(self, activity_id):
        headers = {"Content-Type": "application/json"}
        response = self._request.delete_request(f"{self._endpoint}/{activity_id}", headers=headers)
        print(self._request)
        return response
