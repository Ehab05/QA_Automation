from API_test_project_part_b.infra.config_provider import ConfigProvider


class UtilsLogic:
    def __init__(self):
        self._config = ConfigProvider.load_from_file('../../fake_rest_config.json')

    def get_url_with_endpoint(self, endpoint):
        """
            Constructs a complete URL by appending the given endpoint to the base URL from the configuration.
        """
        return f"{self._config["base_url"]}/{endpoint}"

