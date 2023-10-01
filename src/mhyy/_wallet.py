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
            self._data = data

        def __repr__(self) -> str:
            return f"WalletData._Coin({self._data})"

        def __str__(self) -> str:
            return f"WalletData.Coin[coin: {self.coin}, free: {self.free}, limit: {self.limit}]"

        @property
        def coin(self) -> int:
            """
            米云币数量
            """
            return int(self._data["coin_num"])

        @property
        def free(self) -> int:
            """
            免费米云币数量
            """
            return int(self._data["free_coin_num"])

        @property
        def limit(self) -> int:
            """
            米云币上限
            """
            return int(self._data["coin_limit"])

    class _FreeTime:
        """
        免费时长
        """

        def __init__(self, data: dict):
            self._data = data

        def __repr__(self) -> str:
            return f"WalletData._Freetime({self._data})"

        def __str__(self) -> str:
            return (f"WalletData.Freetime["
                    f"sent: {self.sent}, total: {self.total}, "
                    f"limit: {self.limit}, overflow: {self.overflow}]")

        @property
        def sent(self) -> datetime.time:
            """
            每日登陆赠送的时长
            :return: 如果是首次请求(即签到动作)，则返回赠送的时长，否则为 `0`
            """
            send_free_time = int(self._data["send_freetime"])
            return datetime.time(send_free_time // 60, send_free_time % 60)

        @property
        def total(self) -> datetime.time:
            """
            总共的免费时长
            """
            free_time = int(self._data["free_time"])
            return datetime.time(free_time // 60, free_time % 60)

        @property
        def limit(self) -> datetime.time:
            """
            免费时长上限
            """
            limit = int(self._data["free_time_limit"])
            return datetime.time(limit // 60, limit % 60)

        @property
        def overflow(self) -> datetime.time:
            """
            溢出的时长
            :return: 如果是首次请求(即签到动作), 则返回本次签到溢出的时长
            """
            over = int(self._data["over_freetime"])
            return datetime.time(over // 60, over % 60)

    class _PlayCard:
        """
        畅玩卡
        """

        def __init__(self, data: dict):
            self._data = data

        def __repr__(self) -> str:
            return f"WalletData._PlayCard(f{self._data})"

        def __str__(self) -> str:
            return f"WalletData.PlayCard[expire: {self.expire}, message: {self.message}, status: {self.status}]"

        @property
        def expire(self) -> str:
            """
            过期时间
            :return: 字符串形式的过期时间
            """
            return self._data["expire"]

        @property
        def message(self) -> str:
            """
            点击开通畅玩卡上面的信息
            :return: 提示信息
            """
            return self._data["msg"]

        @property
        def status(self) -> str:
            """
            状态信息
            """
            return self._data["short_msg"]

    def __init__(self, data: dict):
        self._data = data
        self._coin = self._Coin(data["coin"])
        self._free_time = self._FreeTime(data["free_time"])
        self._play_card = self._PlayCard(data["play_card"])

    def __repr__(self) -> str:
        return f"WalletData({self._data})"

    def __str__(self) -> str:
        return f"WalletData[Coin: {self.coin}, FreeTime: {self.free_time}, PlayCard: {self.play_card}]"

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
        # 这里的逻辑是如果给的免费时间为 0 就不是第一次上线了
        return self.free_time.sent != datetime.time(0, 0)
