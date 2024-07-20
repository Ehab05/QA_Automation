import time


class Utils:
    @staticmethod
    def wait_for_action(action, expected, sleep_time, retries):
        result = action
        while result != expected and retries > 0:
            result = action
            time.sleep(sleep_time)
            retries -= retries
