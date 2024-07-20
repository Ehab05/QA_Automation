class AuthorEntry:
    def __init__(self, author_from_config):
        self._id = author_from_config["id"]
        self._idbook = author_from_config["idBook"]
        self._first_name = author_from_config["firstName"]
        self._last_name = author_from_config["lastName"]

    @property
    def id(self):
        return self._id

    @property
    def idbook(self):
        return self._idbook

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def author_to_dict(self):
        return {
            "id": self._id,
            "idBook": self._idbook,
            "firstName": self._first_name,
            "lastName": self._last_name
        }
