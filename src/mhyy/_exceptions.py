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


class APIRequestError(RuntimeError):
    def __init__(self, message: str, ret_code: int):
        self._message = message
        self._ret_code = ret_code

    @property
    def message(self):
        return self._message

    @property
    def ret_code(self):
        return self._ret_code


class ComboTokenInvalidError(RuntimeError):
    def __init__(self, message: str):
        self._message = message

    @property
    def message(self):
        return self._message
