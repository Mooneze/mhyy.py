import datetime


class WalletData:
    """
    用户的钱包数据
    """

    class _Coin:
        """
        米云币
        """

        def __init__(self, data: dict):
            self._coin = int(data["coin_num"])
            self._free_coin = int(data["free_coin_num"])
            self._limit = int(data["coin_limit"])

        @property
        def coin(self) -> int:
            """
            米云币数量
            """
            return self._coin

        @property
        def free(self) -> int:
            """
            免费米云币数量
            """
            return self._free_coin

        @property
        def limit(self) -> int:
            """
            米云币上限
            """
            return self._limit

    class _FreeTime:
        """
        免费时长
        """

        def __init__(self, data: dict):
            self._send_free_time = int(data["send_freetime"])
            self._free_time = int(data["free_time"])
            self._limit = int(data["free_time_limit"])
            self._over = int(data["over_freetime"])

        @property
        def sent(self) -> datetime.time:
            """
            每日登陆赠送的时长
            :return: 如果是首次请求(即签到动作)，则返回赠送的时长，否则为 `0`
            """
            return datetime.time(self._send_free_time // 60, self._send_free_time % 60)

        @property
        def total(self) -> datetime.time:
            """
            总共的免费时长
            """
            return datetime.time(self._free_time // 60, self._free_time % 60)

        @property
        def limit(self) -> datetime.time:
            """
            免费时长上限
            """
            return datetime.time(self._limit // 60, self._limit % 60)

        @property
        def overflow(self) -> datetime.time:
            """
            溢出的时长
            :return: 如果是首次请求(即签到动作), 则返回本次签到溢出的时长
            """
            return datetime.time(self._over // 60, self._over % 60)

    class _PlayCard:
        """
        畅玩卡
        """

        def __init__(self, data: dict):
            self._expire = data["expire"]
            self._message = data["msg"]
            self._short_message = data["short_msg"]

        @property
        def expire(self) -> str:
            """
            过期时间
            :return: 字符串形式的过期时间
            """
            return self._expire

        @property
        def message(self) -> str:
            """
            点击开通畅玩卡上面的信息
            :return: 提示信息
            """
            return self._message

        @property
        def status(self) -> str:
            """
            状态信息
            """
            return self._short_message

    def __init__(self, data: dict):
        self._coin = self._Coin(data["coin"])
        self._free_time = self._FreeTime(data["free_time"])
        self._play_card = self._PlayCard(data["play_card"])

    @property
    def coin(self):
        """
        米云币
        """
        return self._coin

    @property
    def free_time(self):
        """
        免费时长
        """
        return self._free_time

    @property
    def play_card(self):
        """
        畅玩卡
        """
        return self._play_card

    @property
    def is_signin(self) -> bool:
        """
        是否是每日签到动作
        :return: 是则为真
        """
        return self.free_time.sent != datetime.time(0, 0)
