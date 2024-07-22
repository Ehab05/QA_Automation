from API_test_project_part_b.infra.config_provider import ConfigProvider
from API_test_project_part_b.infra.utils import Utils


class ActivityEntry:
    def __init__(self):
        self._config = ConfigProvider().load_from_file("../../fake_rest_config.json")
        self._id = Utils().generate_random_number_within_range(tuple(self._config["activity_id_range"]))
        self._title = Utils().generate_random_string(self._config["activity_title_length"])
        self._duedate = Utils().generate_random_iso_datetime()
        self._completed = Utils().random_boolean()



    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def duedate(self):
        return self._dueDate

    @property
    def completed(self):
        return self._completed

    def activity_to_dict(self):
        return {
            "id": self._id,
            "title": self._title,
            "dueDate": self._duedate,
            "completed": self._completed

        }

    def get_invalid_activity(self):
        return {
            "id": self._title,
            "title": self._id,
            "dueDate": self._duedate,
            "completed": self._completed
        }

    def updated_activity(self, activity_id):
        return {
            "id": activity_id,
            "title": self._title,
            "dueDate": self._duedate,
            "completed": self._completed
         }


