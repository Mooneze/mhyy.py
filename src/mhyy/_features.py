import json
from typing import Any


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
