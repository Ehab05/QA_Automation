from infra.config_provider import ConfigProvider


class Utils:
    def __init__(self):
        self._config = ConfigProvider.load_from_file('../../fake_rest_config.json')

    def get_url_with_endpoint(self, endpoint):
        return f"{self._config["base_url"]}/{endpoint}"
