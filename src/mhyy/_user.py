from typing import Optional
from enum import Enum


class UserClientType(Enum):
    Android = 2


class UserChannel(Enum):
    Official = 0


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
            "x-rpc-client_type": self._client_type.value,
            "x-rpc-channel": self._client_type
        }

    @property
    def combo_token(self):
        return self._combo_token

    @property
    def sys_version(self):
        return self._sys_version

    @property
    def device_id(self):
        return self._device_id

    @property
    def device_name(self):
        return self._device_name

    @property
    def device_model(self):
        return self._device_model

    @property
    def client_type(self):
        return self._client_type

    @property
    def channel(self):
        return self._channel
