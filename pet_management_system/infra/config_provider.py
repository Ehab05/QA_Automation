import json

from API_test_project_part_b.infra.logger import Logger


class ConfigProvider:
    def __init__(self):
        self._logger = Logger("pet_store_management.log")

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {filename} Not Found. Starting with an empty library.")
