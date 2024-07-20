import unittest
from infra.config_provider import ConfigProvider
from logic.api.deck_of_cards_api import DeckOfCardsAPI


class TestDeckOfCards(unittest.TestCase):
    def setUp(self):
        self._config = ConfigProvider.load_from_file('../../config.json')

    def test_create_new_deck(self):
        deck_of_cards = DeckOfCardsAPI()
        response = deck_of_cards.create_new_deck()
        self.assertEqual(response.status_code, 200)

    def test_draw_cards(self):
        deck_of_cards = DeckOfCardsAPI()
        response = deck_of_cards.draw_cards(self._config["deck_id"], self._config["cards_to_draw"])
        self.assertEqual(200, response.status_code)

    def test_shuffle_deck(self):
        deck_of_cards = DeckOfCardsAPI()
        response = deck_of_cards.shuffle_deck(self._config["deck_id"])
        self.assertTrue(response)

    def test_partial_deck(self):
        deck_of_cards = DeckOfCardsAPI()
        response = deck_of_cards.partial_deck(self._config["cards"])
        self.assertTrue(response)
