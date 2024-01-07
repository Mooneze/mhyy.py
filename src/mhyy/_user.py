import enum


class UserType(enum.Enum):
    AndroidUser = 2


class UserChannel(enum.Enum):
    Mihoyo = "cyydmihoyo"


class UserCGGameBiz(enum.Enum):
    CN = "hk4e_cn"


class UserOpBiz(enum.Enum):
    CN = "clgm_cn"


class UserCps(enum.Enum):
    Mihoyo = "cyydmihoyo"


class User:
    def __init__(
            self,
            combo_token: str,
            sys_version: str,
            device_id: str,
            device_name: str,
            device_model: str,
            *,
            user_type: UserType = UserType.AndroidUser,
            channel: UserChannel = UserChannel.Mihoyo,
            cg_game_biz: UserCGGameBiz = UserCGGameBiz.CN,
            op_biz: UserOpBiz = UserOpBiz.CN,
            cps: UserCps = UserCps.Mihoyo,
            language: str = "zh-cn"
    ):
        self._combo_token = combo_token
        self._sys_version = sys_version
        self._device_id = device_id
        self._device_name = device_name
        self._device_model = device_model
        self._user_type = user_type
        self._channel = channel
        self._cg_game_biz = cg_game_biz
        self._op_biz = op_biz
        self._cps = cps
        self._language = language

    def __str__(self) -> str:
        return (f"User[combo_token: {self._combo_token}, sys_version: {self._sys_version}, "
                f"device_id: {self._device_id}, device_name: {self._device_name}, "
                f"device_model: {self._device_model}, user_type: {self._user_type.name}, "
                f"channel: {self._channel.name}, cg_game_biz: {self._cg_game_biz.name}, "
                f"op_biz: {self._op_biz.name}, cps: {self._cps}, language: {self._language}]")

    def __repr__(self) -> str:
        return (f"User(combo_token={self._combo_token}, sys_version={self._sys_version}, device_id={self._device_id}, "
                f"device_name={self._device_name}, device_model={self._device_model}, "
                f"user_type={self._user_type}, channel={self._channel}, "
                f"cg_game_biz={self._cg_game_biz}, op_biz={self._op_biz}, "
                f"cps={self._cps}, language={self._language})")

    @property
    def combo_token(self) -> str:
        return self._combo_token

    @property
    def sys_version(self) -> str:
        return self._sys_version

    @property
    def device_id(self) -> str:
        return self._device_id

    @property
    def device_name(self) -> str:
        return self._device_name

    @property
    def device_model(self) -> str:
        return self.device_model

    @property
    def user_type(self) -> UserType:
        return self._user_type

    @property
    def channel(self) -> UserChannel:
        return self._channel

    @property
    def cps(self) -> UserCps:
        return self._cps

    @property
    def cg_game_biz(self) -> UserCGGameBiz:
        return self.cg_game_biz

    @property
    def language(self) -> str:
        return self._language

    @property
    def op_biz(self) -> UserOpBiz:
        return self._op_biz

    @property
    def header(self) -> dict:
        """
        用户层的请求头
        :return: 发出 Web 请求时的 `Headers`
        """
        return {
            "x-rpc-combo_token": self._combo_token,
            "x-rpc-client_type": str(self._user_type.value),
            "x-rpc-sys_version": self._sys_version,
            "x-rpc-channel": self._channel.value,
            "x-rpc-cps": self._cps.value,
            "x-rpc-cg_game_biz": self._cg_game_biz.value,
            "x-rpc-device_id": self._device_id,
            "x-rpc-device_name": self._device_name,
            "x-rpc-device_model": self._device_model,
            "x-rpc-language": self._language,
            "x-rpc-op_biz": self._op_biz.value
        }
