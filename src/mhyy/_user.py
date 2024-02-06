import warnings
from typing import Optional
from ._types import UserChannel, UserClientType, GameType
from ._exceptions import ComboTokenInvalidError


class User:
    def __init__(
            self,
            combo_token: str,
            sys_version: str,
            device_id: str,
            device_name: str,
            device_model: str,
            *,
            game_type: Optional[GameType] = None,
            client_type: Optional[UserClientType] = UserClientType.Android,
            channel: Optional[UserChannel] = UserChannel.Official
    ):
        self._combo_token = combo_token
        self._sys_version = sys_version
        self._device_id = device_id
        self._device_name = device_name
        self._device_model = device_model
        self._client_type = client_type
        self._game_type = game_type
        self._channel = channel

        # Automatic detection of the game type.

        try:
            bi = self._combo_token.split(";bi=")[1]
        except IndexError:
            raise ComboTokenInvalidError(
                "An error occurred in the automatic detection of the game type, "
                "the 'bi' segment was not found in combo token."
            )

        detected_game_type = {
            "hk4e_cn": GameType.GenshinImpact,
            "hkrpg_cn": GameType.StarRail
        }[bi]

        if self._game_type is None:
            self._game_type = detected_game_type
        else:
            if self._game_type != detected_game_type:
                warnings.warn(
                    "The program detected a difference between the GameType you entered and the GameType it detected. "
                    "This time, it will use your input as the standard. So the data may be incorrect.”"
                    "Please pay attention to the GameType."
                )

    def get_user_headers(self):
        return {
            "x-rpc-combo_token": self._combo_token,
            "x-rpc-sys_version": self._sys_version,
            "x-rpc-device_id": self._device_id,
            "x-rpc-device_name": self._device_name,
            "x-rpc-device_model": self._device_model,
            # Client type in headers must be string.
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
    def game_type(self) -> GameType:
        return self._game_type

    @property
    def channel(self) -> UserChannel:
        return self._channel
