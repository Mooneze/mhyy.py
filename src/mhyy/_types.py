from enum import IntEnum


class UserTypes(IntEnum):
    ANDROID_USER = 2


class SignInResultTypes(IntEnum):
    ERROR = -1
    SUCCESS = 0
    DONE = 1
    OVER_LIMIT = 2
