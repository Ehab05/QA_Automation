class BookEntry:
    def __init__(self, book_from_config):
        self._id = book_from_config["id"]
        self._title = book_from_config["title"]
        self._description = book_from_config["description"]
        self._pageCount = book_from_config["pageCount"]
        self._excerpt = book_from_config["excerpt"]
        self._publishDate = book_from_config["publishDate"]

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def pageCount(self):
        return self._pageCount

    @property
    def excerpt(self):
        return self._excerpt

    @property
    def publishDate(self):
        return self._publishDate

    def book_to_dict(self):
        return {
            "id": self._id,
            "title": self._title,
            "description": self._description,
            "pageCount": self._pageCount,
            "excerpt": self._excerpt,
            "publishDate": self._publishDate
        }
