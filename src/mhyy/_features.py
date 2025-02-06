import json
from typing import Any
from datetime import datetime


class JSONString(str):
    """
    JSON 格式的字符串。
    """

    def __new__(cls, value: str = ''):
        """
        从 JSON 格式的字符串创建 JSONString。

        Args:
            value (str): JSON 格式的字符串。

        Raises:
            JSONDecodeError: 若字符串不是 JSON 格式。
        """
        instance: str = super().__new__(cls, value)

        instance._json = json.loads(instance)

        return instance

    def json(self) -> Any:
        """
        将 JSONString 反序列化为一个 Python 对象。

        Returns:
            一个 Python 对象。
        """
        return self._json


class TimestampString(str):
    """
    时间戳格式的字符串
    """

    def __new__(cls, value: str = ''):
        """
        从时间戳格式的字符串创建 TimestampString。

        Args:
            value (str): 时间戳格式的字符串。
        """
        instance: str = super().__new__(cls, value)

        instance._time = datetime.fromtimestamp(int(value))

        return instance

    def to_time(self) -> datetime:
        """
        将 TimestampString 转换成 Datetime。

        Returns:
            对应时间戳的 Datetime。

        """
        return self._time
