from API_test_project_part_b.infra.api.apiwrapper import APIWrapper
from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.infra.logger import Logger
from API_test_project_part_b.logic.api.utils_logic import UtilsLogic



class Activities:
    """
        This class contains functions that the user can use to perform CRUD operations
        on the Activities section in the fake rest API website
    """

    def __init__(self, request: APIWrapper):
        """
            self._endpoint attribute returns the complete url for the endpoint
            APIWrapper This class provides methods for performing HTTP GET, POST, PUT, and DELETE requests.
        """
        self._request = request
        self._endpoint = UtilsLogic().get_url_with_endpoint("Activities")
        self._config = ConfigProvider().load_from_file("../../fake_rest_config.json")
        self._logger = Logger("fake_rest_api.log").get_logger()

    def get_all_activities(self):
        try:
            response = self._request.get_request(self._endpoint)
            return response
        except Exception as e:
            self._logger.error(f"Error getting all activities")
            return None

    def get_activity_by_id(self, activity_id):
        """
        Get a specific activity by its ID from the API
        :param activity_id:
        :return: HTTP GET response
        """
        try:
            response = self._request.get_request(f"{self._endpoint}/{activity_id}")
            self._logger.info(f"The generated activity id is:{activity_id} ")
            return response
        except Exception as e:
            self._logger.error(f"Error getting the activity by id:{e}")
            return None

    def post_activity(self, valid_activity):
        """
                Creates a new activity by posting the provided data to the API.
        """
        try:
            response = self._request.post_request(self._endpoint, valid_activity)
            self._logger.info(f"{response.json()}")
            return response
        except Exception as e:
            self._logger.error(f"Error posting activity: {e}")
            return None

    def update_activity_by_id(self, activity_id, updated_activity):
        """
        Updates a specific activity by its ID from the data in the configuration
        :param: Activity id and new activity data to update
        :return: HTTP PUT response
        """
        try:
            response = self._request.put_request(f"{self._endpoint}/{activity_id}", updated_activity)
            return response
        except Exception as e:
            self._logger.error(f"Error updating activity by id: {e}")
            return None

    def delete_activity_by_id(self, activity_id):
        try:
            headers = {"Content-Type": "application/json"}
            response = self._request.delete_request(f"{self._endpoint}/{activity_id}", headers=headers)
            return response
        except Exception as e:
            self._logger.error(f"Error deleting activity by id: {e}")
            return None
