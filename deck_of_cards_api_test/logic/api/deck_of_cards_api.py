from infra.api.apiwrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.logger import Logger


class DeckOfCardsAPI:
    def __init__(self):
        self._config = ConfigProvider.load_from_file('../../config.json')
        self._logger = Logger(self.__class__.__name__).get_logger()
        self._api = APIWrapper(self._config["base_url"])

    def create_new_deck(self):
        endpoint = "new"
        response = self._api.get_request(endpoint)
        return response

    def draw_cards(self, deck_id, count):
        endpoint = f"{deck_id}/draw/?count={count}"
        response = self._api.get_request(endpoint)
        return response

    def shuffle_deck(self, deck_id):
        if not deck_id:
            raise ValueError("Set deck id")
        endpoint = f"{deck_id}/shuffle/"
        response = self._api.get_request(endpoint)
        self._logger.info(f"The deck{deck_id} was shuffled")
        data = response.json()
        return data['shuffled']

    def partial_deck(self, cards):
        endpoint = f"new/shuffle/?cards={cards}"
        response = self._api.get_request(endpoint)
        data = response.json()
        return data['success']

    def check_remaining(self, data):
        return data["remaining"]
