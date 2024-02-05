from typing import Optional
from ._types import UserChannel, UserClientType


class User:
    def __init__(
            self,
            combo_token: str,
            sys_version: str,
            device_id: str,
            device_name: str,
            device_model: str,
            *,
            client_type: Optional[UserClientType] = UserClientType.Android,
            channel: Optional[UserChannel] = UserChannel.Official
    ):
        self._combo_token = combo_token
        self._sys_version = sys_version
        self._device_id = device_id
        self._device_name = device_name
        self._device_model = device_model
        self._client_type = client_type
        self._channel = channel

    def get_user_headers(self):
        return {
            "x-rpc-combo_token": self._combo_token,
            "x-rpc-sys_version": self._sys_version,
            "x-rpc-device_id": self._device_id,
            "x-rpc-device_name": self._device_name,
            "x-rpc-device_model": self._device_model,
            # Client type in headers must be string
            "x-rpc-client_type": str(self._client_type.value),
            "x-rpc-channel": self._client_type
        }

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
        return self._device_model

    @property
    def client_type(self) -> UserClientType:
        return self._client_type

    @property
    def channel(self) -> UserChannel:
        return self._channel
