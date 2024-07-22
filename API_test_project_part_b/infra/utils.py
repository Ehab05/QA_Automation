import datetime
import random
import string
import pytz

from API_test_project_part_b.infra.config_provider import ConfigProvider


class Utils:
    def __init__(self):
        self._config = ConfigProvider().load_from_file("../../fake_rest_config.json")

    @staticmethod
    def generate_random_number_within_range(range_values: tuple):
        """
        this function generates a random integer within the given range (a: minimum, b: maximum)
        :param range_values: A tuple containing two integers
        :return: random integer within the given range
        """
        if len(range_values) != 2:
            raise ValueError("The range must be 2 elements.")
        a, b = range_values
        if not (isinstance(a, int) and isinstance(b, int)):
            raise TypeError("The minimum and maximum range values must be integers")
        return random.randint(a, b)

    @staticmethod
    def generate_random_string(string_length):
        """
        Generates a random string of the specified length using letters.
        :param string_length:
        :return: random string
        """
        letters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(letters) for _ in range(string_length))

    @staticmethod
    def generate_random_iso_datetime():
        """
        Generates a random ISO 8601 datetime string in the format 'YYYY-MM-DDTHH:MM:SS.SSSZ'.
        :return: A random ISO 8601 datetime string.
        """
        # Generate a random date
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

        # Format the datetime as ISO 8601 string
        iso_datetime_string = random_datetime.strftime('%Y-%m-%dT%H:%M:%S.') + f"{random_microseconds:06d}" + "+00:00"
        return iso_datetime_string

    @staticmethod
    def random_boolean():
        return random.choice([True, False])
