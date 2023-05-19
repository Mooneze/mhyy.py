from enum import IntEnum


class UserType(IntEnum):
    AndroidUser = 2


class User:
    def __init__(
            self,
            combo_token: str,
            sys_version: str,
            device_id: str,
            device_name: str,
            device_model: str,
            user_type: UserType = UserType.AndroidUser
    ):
        self._combo_token = combo_token
        self._sys_version = sys_version
        self._device_id = device_id
        self._device_name = device_name
        self._device_model = device_model
        self._user_type = user_type

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
    def header(self) -> dict:
        """
        用户层的请求头
        :return: 发出 Web 请求时的 `Headers`
        """
        return {
            "x-rpc-combo_token": self._combo_token,
            "x-rpc-client_type": str(self._user_type.value),
            "x-rpc-sys_version": self._sys_version,
            "x-rpc-channel": "mihoyo",
            "x-rpc-device_id": self._device_id,
            "x-rpc-device_name": self._device_name,
            "x-rpc-device_model": self._device_model,
        }
