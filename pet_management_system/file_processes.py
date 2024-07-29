import json

from python_error_handlinig.custom_exception import CustomException


class FileProcesses:
    def __init__(self, file):
        self._file = file

    def read_json_file(self):
        try:
            data = json.load(self._file)
            return data
        except json.JSONDecodeError:
            raise CustomException("Error decoding JSON from the file")
        except PermissionError:
            raise CustomException("There is no permission to read this file")
        except IOError:
            raise CustomException("Error with the file content")
        finally:
            self._file.close()

    def write_json_file(self, data):
        try:
            json.dump(data, self._file, indent=4)
            return "The JSON content was successfully written"
        except TypeError:
            raise CustomException("Invalid data type for JSON serialization")
        except PermissionError:
            raise CustomException("There is no permission to write to this file")
        except IOError:
            raise CustomException("Error with the file content")
        finally:
            self._file.close()

    def update_json_file(self, updates: dict):
        try:

            # Read existing data
            data = self.read_json_file()

            # Update data with provided updates
            data.update(updates)

            # Move the file pointer to the beginning of the file
            self._file.seek(0)

            # Clean added data
            self._file.truncate()
            # Write updated data back to the file
            self.write_json_file(data)
        except json.JSONDecodeError:
            raise CustomException("Error decoding JSON from the file")
        except PermissionError:
            raise CustomException("There is no permission to read this file")
        except IOError:
            raise CustomException("Error with the file content")
        except TypeError:
            raise CustomException("Invalid data type for JSON serialization")
        finally:
            self._file.close()

    def __getitem__(self, key):
        data = self.read_json_file()
        return data[key]
