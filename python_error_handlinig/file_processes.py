from python_error_handlinig.custom_exception import CustomException


class FileProcesses:

    def read_file(self, file):
        try:
            content = file.read()
            return content
        except PermissionError:
            raise CustomException(f"There is no permission to read this file")
        except IOError:
            raise CustomException(f"Error with the file content")
        finally:
            file.close()

    def write_file(self, file, content):
        try:
            file.write(content)
            return f"The content was successfully written: {content}"
        except PermissionError:
            raise CustomException(f"There is no permission to write to this file")
        except IOError:
            raise CustomException(f"Enter valid content to write")
        finally:
            file.close()
