from contextlib import contextmanager
from python_error_handlinig.custom_exception import CustomException


class FileHandler:
    def __init__(self, path, mode):
        self._path = path
        self._mode = mode


    @contextmanager
    def file_handler(self):
        try:
            with open(self._path, self._mode) as file:
                yield file
        except FileNotFoundError:
            raise CustomException(f"File not found")
        except Exception as e:
            raise CustomException(f"File processing error: {e}")
