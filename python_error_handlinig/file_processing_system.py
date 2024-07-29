from python_error_handlinig.custom_exception import CustomException
from python_error_handlinig.file_handler import FileHandler
from python_error_handlinig.file_processes import FileProcesses


class FileProcessingSystem:
    def __init__(self):
        try:
            try:
                self._file_path = input(f"Please enter the file path")
                self._operation = input(f"Please enter the desired operation: read/write").strip().lower()
            except IOError:
                raise CustomException(f"Please enter a valid file path and valid operation")
            self._file_handler = FileHandler(self._file_path, self._operation)
        except Exception as e:
            raise e

    def file_processing_system(self):
        if self._operation == "read":
            try:
                content = FileProcesses().read_file(self._file_handler)
                return content
            except Exception as e:
                raise e
        if self._operation == "write":
            try:
                content = input(f"Please enter the content.")
                updated_file = FileProcesses().write_file(self._file_handler, content)
                return updated_file
            except Exception as e:
                raise e
