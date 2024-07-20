class ActivityEntry:
    def __init__(self, activity_from_config):
        self._id = activity_from_config["id"]
        self._title = activity_from_config["title"]
        self._duedate = activity_from_config["dueDate"]
        self._completed = activity_from_config["completed"]

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
