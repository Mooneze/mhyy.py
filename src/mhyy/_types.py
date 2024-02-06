from enum import Enum
from typing import TypeVar


class GameType(Enum):
    GenshinImpact = 0
    StarRail = 1


class UserClientType(Enum):
    Android = 2


class UserChannel(Enum):
    Official = 0


T = TypeVar("T", bound="NotificationStatus")


class NotificationStatus(Enum):
    Read = "NotificationStatusRead"
    Unread = "NotificationStatusUnread"

    Undefined = "NotificationStatusUndefined"

    @classmethod
    def get_status_by_name(cls, status: str) -> T:
        for member in cls:
            if member.value == status:
                return member
        return cls.Undefined


V = TypeVar("V", bound="NotificationType")


class NotificationType(Enum):
    Popup = "NotificationTypePopup"

    Undefined = "NotificationTypeUndefined"

    @classmethod
    def get_type_by_name(cls, type_: str) -> V:
        for member in cls:
            if member.value == type_:
                return member
        return cls.Undefined
