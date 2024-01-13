class WebRequestError(RuntimeError):
    def __init__(self, message: str, status_code: int):
        self._message = message
        self._status_code = status_code

    @property
    def message(self):
        return self._message

    @property
    def status_code(self):
        return self._status_code
