import os
import sys


class Utils:
    def setup_environment(self, current_file, file_path, project_path):
        """
        Set up the environment by adding the project root to the system path
        and returning the path to the loaded file.
        """
        # Get the project root directory (three levels up)
        project_root = os.path.abspath(os.path.join(os.path.dirname(current_file), project_path))

        # Add the project root directory to sys.path
        sys.path.append(project_root)

        # Path to the configuration file (two levels up from the current file)
        file_path = os.path.abspath(os.path.join(project_root, file_path))

        return file_path
