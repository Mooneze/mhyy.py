from typing import TypeVar
from ._types import NotificationType, NotificationStatus


T = TypeVar("T", bound="Notification")


class Notification:
    def __init__(
            self,
            id_: str,
            status: NotificationStatus,
            type_: NotificationType,
            priority: int,
            source: str,
            desc: str,
            msg: str,
            created_at: str
    ):
        self._id = id_
        self._status = status
        self._type = type_
        self._priority = priority
        self._source = source
        self._desc = desc
        self._msg = msg
        self._created_at = created_at

    @classmethod
    def from_data_dict(cls, data: dict) -> T:
        return cls(
            id_=data['id'],
            status=NotificationStatus.get_status_by_name(data['status']),
            type_=NotificationType.get_type_by_name(data['type']),
            priority=data['priority'],
            source=data['source'],
            desc=data['desc'],
            msg=data['msg'],
            created_at=data['created_at']
        )

    @property
    def id(self):
        return self._id

    @property
    def status(self):
        return self._status

    @property
    def type(self):
        return self._type

    @property
    def priority(self):
        return self._priority

    @property
    def source(self):
        return self._source

    @property
    def desc(self):
        return self._desc

    @property
    def msg(self):
        return self._msg

    @property
    def create_at(self):
        return self._created_at
