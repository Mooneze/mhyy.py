from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True)
class CoinData:
    """
    用户的 原点 / 星云币 时长数据。

    Attributes:
        coin_num (int): 原点 / 星云币 数。
        free_coin_num (int): 免费 原点 / 星云币 数。
        coin_limit (int): 原点 / 星云币 的数量上限。
        exchange (int): 与原点时长的汇率。通常来说，10 原点 / 星云币 = 1 游戏时长。
    """
    coin_num: int
    free_coin_num: int
    coin_limit: int
    exchange: int


@dataclass_json
@dataclass(frozen=True)
class FreeTimeData:
    """
    用户的免费时长数据。

    Attributes:
        send_freetime (int): 若该用户是本日第一次登录，那么此处的值为每日赠送的免费时长 (min)。反之，此处恒为 0。
        free_time (int): 总免费时长 (min)。
        free_time_limit (int): 免费时长上限 (min)。
        over_freetime (int): 该用户是本日第一次登录且赠送的时长有一部分超出了免费时长上限，那么此处的值为溢出的免费时长 (min)。
    """
    send_freetime: int
    free_time: int
    free_time_limit: int
    over_freetime: int


@dataclass_json
@dataclass(frozen=True)
class StatusData:
    """
    未知数据
    """
    status: int
    msg: str
    total_time_status: int
    status_new: int


@dataclass_json
@dataclass(frozen=True)
class StatData:
    """
    未知数据
    """
    vip_point: str


@dataclass_json
@dataclass(frozen=True)
class PlayCardData:
    """
    用户的畅玩卡数据

    Attributes:
        expire (str): 畅玩卡过期时间
        msg (str): 畅玩卡信息
        short_msg (str): 畅玩卡短信息 / 状态
        play_card_limit (str): 未知
    """
    expire: str
    msg: str
    short_msg: str
    play_card_limit: str


@dataclass_json
@dataclass(frozen=True)
class WalletData:
    """
    用户的钱包数据。

    Attributes:
        coin (CoinData): 原点时长数据。
        free_time (FreeTimeData): 免费时长数据。
        status (StatusData): 未知。
        stat (StatData): 未知。
        play_card (PlayCardData): 畅玩卡数据。
    """
    coin: CoinData
    free_time: FreeTimeData
    status: StatusData
    stat: StatData
    play_card: PlayCardData

    def is_sign_in(self) -> bool:
        """
        判断本次行为是否为签到操作 (本日第一次登录)。

        Returns:
            若为 True，则本次行为是签到操作。
        """
        return self.free_time.send_freetime != 0
