from enum import IntEnum, StrEnum


class UserTypes(IntEnum):
    ANDROID_USER = 2


class SignInResultTypes(IntEnum):
    ERROR = -1
    SUCCESS = 0
    DONE = 1
    OVER_LIMIT = 2


class NotificationStatus(StrEnum):
    UNREAD = "NotificationStatusUnread"
    READ = "NotificationStatusRead"


class NotificationTypes(StrEnum):
    POPUP = "NotificationTypePopup"
