from enum import Enum
from typing import TypeVar


class GameType(Enum):
    """
    游戏类型。

    Attributes:
        GenshinImpact: 云·原神。
        StarRail: 云·星穹铁道。
    """
    GenshinImpact = 0
    StarRail = 1


class UserClientType(Enum):
    """
    客户端类型。

    Attributes:
        Android: 安卓。
    """
    Android = 2


class UserChannel(Enum):
    """
    游戏渠道。

    Attributes:
        Official: 官方服。
    """
    Official = 0


T = TypeVar("T", bound="NotificationStatus")


class NotificationStatus(Enum):
    """
    通知状态。

    Attributes:
        Read: 已读。
        Unread: 未读。
        Undefined: 未定义。
    """
    Read = "NotificationStatusRead"
    Unread = "NotificationStatusUnread"

    Undefined = "NotificationStatusUndefined"

    @classmethod
    def get_status_by_name(cls, status: str) -> T:
        """
        从字符串获取枚举成员。

        Args:
            status (str): 成员字符串。

        Returns:
            枚举成员。
        """
        for member in cls:
            if member.value == status:
                return member
        return cls.Undefined


V = TypeVar("V", bound="NotificationType")


class NotificationType(Enum):
    """
    通知种类。

    Attributes:
        Popup: 弹窗通知。
        Undefined: 未定义。
    """
    Popup = "NotificationTypePopup"

    Undefined = "NotificationTypeUndefined"

    @classmethod
    def get_type_by_name(cls, type_: str) -> V:
        """
        从字符串获取枚举成员。

        Args:
            type_ (str): 成员字符串。

        Returns:
            枚举成员。
        """
        for member in cls:
            if member.value == type_:
                return member
        return cls.Undefined
