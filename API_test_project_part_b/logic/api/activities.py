from infra.api.apiwrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.entries.post_activity import PostActivity
from logic.api.utils_logic import Utils


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
        activity = PostActivity(self._config["activity_1"])
        response = self._request.post_request(self._endpoint, activity.activity_to_dict())
        return response

    def update_activity(self, id):
        response = self._request.put_request(f"{self._endpoint}/{id}", self._config["activity_to_update"])
        return response

