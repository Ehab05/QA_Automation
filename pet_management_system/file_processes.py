import json

from python_error_handlinig.custom_exception import CustomException


class FileProcesses:

    def read_json_file(self, file):
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            raise CustomException("Error decoding JSON from the file")
        except PermissionError:
            raise CustomException("There is no permission to read this file")
        except IOError:
            raise CustomException("Error with the file content")
        finally:
            file.close()

    def write_json_file(self, file, data):
        try:
            json.dump(data, file, indent=4)
            return "The JSON content was successfully written"
        except TypeError:
            raise CustomException("Invalid data type for JSON serialization")
        except PermissionError:
            raise CustomException("There is no permission to write to this file")
        except IOError:
            raise CustomException("Error with the file content")
        finally:
            file.close()

    def update_json_file(self, file, updates):
        try:
            with open(file, 'r+') as file:
                # Read existing data
                data = self.read_json_file(file)

                # Update data with provided updates
                data.update(updates)

                # Move the file pointer to the beginning of the file
                file.seek(0)

                # Clean added data
                file.truncate()
                # Write updated data back to the file
                self.write_json_file(file, data)
        except json.JSONDecodeError:
            raise CustomException("Error decoding JSON from the file")
        except PermissionError:
            raise CustomException("There is no permission to read this file")
        except IOError:
            raise CustomException("Error with the file content")
        except TypeError:
            raise CustomException("Invalid data type for JSON serialization")
        finally:
            file.close()
