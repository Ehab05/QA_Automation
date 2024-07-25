class ResponseWrapper:
    def __init__(self, ok, status_code, data):
        self._ok = ok
        self._status_code = status_code
        self._data = data

    def success(self):
        return self.ok and 200 <= self._status_code <= 300

    @property
    def ok(self):
        return self._ok

    @property
    def status_code(self):
        return self._status_code

    @property
    def data(self):
        return self._data
