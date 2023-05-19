class WebRequestError(RuntimeError):
    def __init__(self, message):
        self.message = message


class APIError(RuntimeError):
    def __init__(self, message):
        self.message = message
