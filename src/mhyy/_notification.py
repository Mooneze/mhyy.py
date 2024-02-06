from typing import TypeVar
from ._types import NotificationType, NotificationStatus


T = TypeVar("T", bound="Notification")


class Notification:
    """
    通知类。
    """
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

    def __repr__(self) -> str:
        return (f"Notification(id={self._id}, status={self._status}, type={self._type}, priority={self._priority}, "
                f"source={self._source}, desc={self._desc}, msg={self.msg}, created_at={self._created_at})")

    @classmethod
    def from_data_dict(cls, data: dict) -> T:
        """
        从特定的数据结构生成 Notification。

        Args:
            data (dict): 消息数据。

        Returns:
            包装后的消息数据。
        """
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
    def id(self) -> str:
        """
        通知 ID。

        Returns:
            该通知的 ID。
        """
        return self._id

    @property
    def status(self) -> NotificationStatus:
        """
        通知状态。

        Returns:
            该通知的通知状态。
        """
        return self._status

    @property
    def type(self) -> NotificationType:
        """
        通知种类。

        Returns:
            该通知的通知种类。
        """
        return self._type

    @property
    def priority(self) -> int:
        """
        作用未知，根据名称推测是通知的优先级。

        Returns:
            该通知的优先级。
        """
        return self._priority

    @property
    def source(self) -> str:
        """
        作用未知。

        Returns:
            一个字符串，作用未知。
        """
        return self._source

    @property
    def desc(self) -> str:
        """
        作用未知，根据名称推测是通知的描述。

        Returns:
            该通知的描述。
        """
        return self._desc

    @property
    def msg(self) -> str:
        """
        通知内容。

        Returns:
            一个字符串，包含了 json 文本格式的该通知的内容。
        """
        return self._msg

    @property
    def create_at(self):
        """
        通知创建时间。

        Returns:
            一个字符串，是秒级的时间戳 (10位)，描述了该通知何时被创建。
        """
        return self._created_at
