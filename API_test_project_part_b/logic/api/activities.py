from API_test_project_part_b.infra.api.apiwrapper import APIWrapper
from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.logic.api.entries.activity_entry import ActivityEntry

from API_test_project_part_b.logic.api.utils_logic import Utils


class Activities:
    def __init__(self, request: APIWrapper):
        super().__init__()
        self._request = request
        self._endpoint = Utils().get_url_with_endpoint("Activities")
        self._config = ConfigProvider().load_from_file("../../fake_rest_config.json")

    def get_all_activities(self):
        response = self._request.get_request(self._endpoint)
        return response

    def post_activity(self):
        activity = ActivityEntry(self._config["activity_1"])
        response = self._request.post_request(self._endpoint, activity.activity_to_dict())
        return response

    def update_activity(self, id):
        response = self._request.put_request(f"{self._endpoint}/{id}", self._config["activity_to_update"])
        return response

