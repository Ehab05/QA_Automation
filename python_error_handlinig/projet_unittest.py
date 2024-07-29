import unittest

from python_error_handlinig.file_handler import FileHandler
from python_error_handlinig.file_processes import FileProcesses


class TestFileProcessingSystem(unittest.TestCase):

    def test_file_handler_with_write_mode(self):
        try:
            file_handler = FileHandler("file.txt", "w")
            self.assertIsInstance(file_handler, file_handler.__class__)
        except Exception as e:
            self.fail(f"Error:{e}")

    def test_file_handler_with_read_mode(self):
        try:
            file_handler = FileHandler("file.txt", "r")
            self.assertIsInstance(file_handler, file_handler.__class__)
        except Exception as e:
            self.fail(f"Error:{e}")

    def test_write_function(self):
        file_handler = FileHandler("file.txt", "w")
        file_processes = FileProcesses()
        with file_handler.file_handler() as file:
            result = file_processes.write_file(file, "Isn't there error handling for my life")
            self.assertEqual(result, "The content was successfully written: Isn't there error handling for my life")

    def test_read_function(self):
        file_handler = FileHandler("file.txt", "r")
        file_processes = FileProcesses()
        with file_handler.file_handler() as file:
            file_content = file_processes.read_file(file)
            self.assertEqual(file_content, "Isn't there error handling for my life")

