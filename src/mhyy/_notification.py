import enum
import warnings
from ._exception import UndefinedNameWarning


class NotificationStatus(enum.StrEnum):
    UNREAD = "NotificationStatusUnread"
    READ = "NotificationStatusRead"
    UNDEFINED = "NotificationStatusUndefined"


class NotificationType(enum.StrEnum):
    POPUP = "NotificationTypePopup"
    UNDEFINED = "NotificationTypeUndefined"


class Notification:
    def __init__(self, data: dict):
        self._id = data["id"]

        if data["status"] not in NotificationStatus:
            self._status = NotificationStatus.UNDEFINED
            warnings.warn(f'The name {data["status"]} is undefined.', UndefinedNameWarning)
        else:
            self._status = NotificationStatus(data["status"])

        if data["type"] not in NotificationType:
            self._type = NotificationType.UNDEFINED
            warnings.warn(f'The name {data["type"]} is undefined.', UndefinedNameWarning)
        else:
            self._type = NotificationType(data["type"])

        self._priority = data["priority"]
        self._source = data["source"]
        self._desc = data["desc"]
        self._msg = data["msg"]
        self._created_at = data["created_at"]
