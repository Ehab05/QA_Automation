import datetime
import os
import random
import string
import pytz

from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.infra.logger import Logger


class Utils:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(base_dir, '../../fake_rest_config.json')
        self._config = ConfigProvider().load_from_file(config_file_path)
        self._logger = Logger("fake_rest_api.log").get_logger()

    def generate_random_number_within_range(self, range_values: tuple):
        """
        this function generates a random integer within the given range (a: minimum, b: maximum)
        :param range_values: A tuple containing two integers
        :return: random integer within the given range
        """
        try:
            if len(range_values) != 2:
                raise ValueError("The range must be 2 elements.")
            a, b = range_values
            if not (isinstance(a, int) and isinstance(b, int)):
                raise TypeError("The minimum and maximum range values must be integers")
            return random.randint(a, b)
        except Exception as e:
            self._logger.error(f"Error generating a random number: {e}")

    def generate_random_string(self, string_length):
        """
        Generates a random string of the specified length using letters.
        :param string_length:
        :return: random string
        """
        try:
            letters = string.ascii_letters + string.digits + string.punctuation
            return ''.join(random.choice(letters) for _ in range(string_length))
        except Exception as e:
            self._logger.error(f"Error generating a random string: {e}")

    def generate_random_iso_datetime(self):
        """
        Generates a random ISO 8601 datetime string in the format 'YYYY-MM-DDTHH:MM:SS.SSSZ'.
        :return: A random ISO 8601 datetime string.
        """
        # Generate a random date
        try:
            start_date = datetime.datetime(2024, 7, 1, tzinfo=pytz.UTC)
            end_date = datetime.datetime(2050, 12, 1, tzinfo=pytz.UTC)
            delta = end_date - start_date
            random_days = random.randrange(delta.days)
            random_date = start_date + datetime.timedelta(days=random_days)

            # Generate a random time
            random_seconds = random.randint(0, 86399)
            random_microseconds = random.randint(0, 999999)
            random_time = datetime.timedelta(seconds=random_seconds, microseconds=random_microseconds)

            # Combine date and time
            random_datetime = random_date + random_time

            # Convert microseconds to milliseconds
            milliseconds = random_microseconds // 1000
            # Format the datetime as ISO 8601 string
            iso_datetime_string = random_datetime.strftime('%Y-%m-%dT%H:%M:%S.') + f"{milliseconds:03d}" + "+00:00"
            return iso_datetime_string
        except Exception as e:
            self._logger.error(f"Error generating a random date: {e}")

    @staticmethod
    def random_boolean():
        return random.choice([True, False])
