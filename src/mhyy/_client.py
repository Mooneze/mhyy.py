from enum import Enum
from typing import Optional, List
from ._types import GameType, NotificationType, NotificationStatus
from ._api import API
from ._user import User
from ._exceptions import WebRequestError, APIRequestError
from ._wallet import WalletData
from ._notification import Notification
import httpx


class ClientStatus(Enum):
    # UNOPENED:
    #   The client has been instantiated, but has not been used to send a web request,
    #   or been opened by entering the context of a `with` block.
    UNOPENED = 0
    # OPENED:
    #   The client has either sent a web request, or is within a `with` block.
    OPENED = 1
    # CLOSED:
    #   The client has either exited the `with` block, or `close()` has been called explicitly.
    CLOSED = 2


class Client:
    """
    米哈云游客户端。
    """

    def __init__(self):
        self._client: httpx.Client = httpx.Client()
        self._status: ClientStatus = ClientStatus.UNOPENED
        # The version will be updated on the first request from the corresponding game.
        self._versions: dict = {
            GameType.GenshinImpact: None,
            GameType.StarRail: None
        }

    def __enter__(self):
        if self._status != ClientStatus.UNOPENED:
            msg = {
                ClientStatus.OPENED: "Cannot open a client instance more than once.",
                ClientStatus.CLOSED: "Cannot reopen a client instance, once it has been closed.",
            }[self._status]
            raise RuntimeError(msg)

        self._status = ClientStatus.OPENED
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._status = ClientStatus.CLOSED
        self._client.close()

    def _update_version(self, game_type: GameType) -> None:
        """
        更新客户端版本。

        Args:
            game_type (GameType): 要更新的客户端类型。
        """
        version_url = API.get_game_version_url(game_type)

        resp = self._client.get(version_url, params={
            "key": API.get_launcher_key(game_type),
            "launcher_id": API.get_launcher_id(game_type)
        }).json()

        self._versions[game_type] = resp["data"]["game"]["latest"]["version"]

    def _get_common_headers(self, game_type: GameType) -> dict:
        """
        获取指定游戏类型的 headers 常量。

        Args:
            game_type (GameType): 需要获取 headers 的游戏类型。

        Returns:
            一个字典，包含了指定游戏的 headers。
        """
        return {
            "x-rpc-app_version": self._versions[game_type],
            "x-rpc-app_id": API.get_app_id(game_type),
            "x-rpc-vendor_id": API.get_vendor_id(game_type),
            "x-rpc-cg_game_biz": API.get_cg_game_biz(game_type),
            "x-rpc-op_biz": API.get_op_biz(game_type),
            "x-rpc-cps": API.get_cps(game_type)
        }

    def _user_web_get(self, user: User, url: str, params: Optional[dict] = None) -> httpx.Response:
        """
        附带用户 headers 的 get 类型请求。

        Args:
            user (User): 发起请求的用户。
            url (str): 目标 URL。
            params (Optional[dict]): 可选的参数。

        Returns:
            httpx 库的 Response 类。
        """

        # Check the client state.
        if self._status == ClientStatus.CLOSED:
            raise RuntimeError("Cannot send a request, as the client has been closed.")

        # Check version.
        if self._versions[user.game_type] is None:
            self._update_version(user.game_type)

        # Update client state.
        if self._status != ClientStatus.OPENED:
            self._status = ClientStatus.OPENED

        # Get the special common headers of the game.
        headers: dict = self._get_common_headers(user.game_type)

        user_headers: dict = user.get_user_headers()
        user_headers["x-rpc-channel"] = API.get_channel_id(user.channel, user.game_type)

        headers.update(user_headers)

        resp = self._client.get(url, headers=headers, params=params)

        if resp.status_code != 200:
            raise WebRequestError(
                f"An error occurred in the network request, status code: {resp.status_code}",
                resp.status_code
            )

        return resp

    def get_wallet_data(self, user: User) -> WalletData:
        """
        获取指定用户的钱包数据。

        Args:
            user (User): 发起请求的用户。

        Returns:
            该用户的钱包数据。
        """
        r = self._user_web_get(user, API.get_wallet_data_url(user.game_type)).json()
        if r['retcode'] != 0:
            raise APIRequestError(r['message'], r['retcode'])
        return WalletData.from_dict(r['data'])

    def get_notifications(
            self,
            user: User,
            *,
            status: Optional[NotificationStatus] = None,
            type_: Optional[NotificationType] = None,
            is_sort: Optional[bool] = True
    ) -> List[Notification]:
        """
        获取指定用户的通知信息。

        Args:
            user (User): 发起请求的用户。
            status (Optional[NotificationStatus]): 筛选指定的通知状态。
            type_ (Optional[NotificationType]): 筛选指定的通知种类。
            is_sort (Optional[bool]): 是否排序。

        Returns:
            一个列表，包含了指定用户的指定通知。
        """

        # Build params.

        params = {
            "is_sort": is_sort
        }

        # Optional params.
        if status:
            params["status"] = status.value
        if type_:
            params["type"] = type_.value

        r = self._user_web_get(
            user,
            API.get_notifications_url(user.game_type),
            params=params
        ).json()

        if r['retcode'] != 0:
            raise APIRequestError(r['message'], r['retcode'])

        notifications = []

        for notification_data in r['data']['list']:
            notifications.append(Notification.from_data_dict(notification_data))

        return notifications

    def get_client_version(self, game_type: GameType) -> str:
        """
        获取指定游戏类型的版本号，若想获取字典类型的所有版本号，请使用 versions 属性。

        Args:
            game_type (GameType): 游戏类型。

        Returns:
            该游戏类型的版本号。
        """
        return self._versions[game_type]

    @property
    def versions(self) -> dict:
        """
        所有游戏类型的版本号字典，若只想获取指定游戏类型的版本号，请使用 get_client_version() 方法。
        """
        return self._versions
