import warnings
import datetime
from enum import Enum
from ._exception import UndefinedNameWarning


class NotificationStatus(Enum):
    UNREAD = "NotificationStatusUnread"
    READ = "NotificationStatusRead"
    UNDEFINED = "NotificationStatusUndefined"


class NotificationType(Enum):
    POPUP = "NotificationTypePopup"
    UNDEFINED = "NotificationTypeUndefined"


class Notification:
    def __init__(self, data: dict):
        self._data = data

        if data["status"] not in [status.value for status in NotificationStatus]:
            self._status = NotificationStatus.UNDEFINED
            warnings.warn(f'The name {data["status"]} is undefined.', UndefinedNameWarning)
        else:
            self._status = NotificationStatus(data["status"])

        if data["type"] not in [ntype.value for ntype in NotificationType]:
            self._type = NotificationType.UNDEFINED
            warnings.warn(f'The name {data["type"]} is undefined.', UndefinedNameWarning)
        else:
            self._type = NotificationType(data["type"])

    def __repr__(self) -> str:
        return f"Notification({self._data})"

    def __str__(self) -> str:
        return f"Notification<{self.msg}>"

    @property
    def id(self) -> str:
        return self._data["id"]

    @property
    def status(self) -> NotificationStatus:
        return self._status

    @property
    def type(self) -> NotificationType:
        return self._type

    @property
    def priority(self) -> int:
        return self._data["priority"]

    @property
    def source(self) -> str:
        return self._data["source"]

    @property
    def desc(self) -> str:
        return self._data["desc"]

    @property
    def msg(self) -> str:
        return self._data["msg"]

    @property
    def created_at(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(int(self._data["created_at"]))
