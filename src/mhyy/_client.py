from enum import Enum
from typing import Optional
from ._types import ClientType
from ._api import API
from ._user import User
from ._exceptions import WebRequestError
from ._wallet import WalletData
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
    def __init__(self, client_type: ClientType):
        self._client_type = client_type
        self._client = httpx.Client()
        self._version = None
        self._status = ClientStatus.UNOPENED

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

    def _update_version(self) -> None:
        version_url = API.get_game_version_url(self._client_type)
        resp = self._client.get(version_url, params={
            "key": API.get_launcher_key(self._client_type),
            "launcher_id": API.get_launcher_id(self._client_type)
        }).json()
        self._version = resp["data"]["game"]["latest"]["version"]

    def _get_common_headers(self) -> dict:
        return {
            "x-rpc-app_version": self._version,
            "x-rpc-app_id": API.get_app_id(self._client_type),
            "x-rpc-vendor_id": API.get_vendor_id(self._client_type),
            "x-rpc-cg_game_biz": API.get_cg_game_biz(self._client_type),
            "x-rpc-op_biz": API.get_op_biz(self._client_type),
            "x-rpc-cps": API.get_cps(self._client_type)
        }

    def _user_web_get(self, user: User, url: str, params: Optional[dict] = None) -> httpx.Response:
        if self._status == ClientStatus.CLOSED:
            raise RuntimeError("Cannot send a request, as the client has been closed.")

        if self._version is None:
            self._update_version()

        if self._status != ClientStatus.OPENED:
            self._status = ClientStatus.OPENED

        headers: dict = self._get_common_headers()

        user_headers: dict = user.get_user_headers()
        user_headers["x-rpc-channel"] = API.get_channel_id(user.channel, self.client_type)

        headers.update(user_headers)

        resp = self._client.get(url, headers=headers, params=params)

        if resp.status_code != 200:
            raise WebRequestError(
                f"An error occurred in the network request, status code: {resp.status_code}",
                resp.status_code
            )

        return resp

    def get_wallet_data(self, user: User) -> WalletData:
        r = self._user_web_get(user, API.get_wallet_data_url(self._client_type)).json()
        return WalletData.from_dict(r['data'])

    @property
    def client_type(self) -> ClientType:
        return self._client_type

    @property
    def version(self):
        return self._version


class GenshinImpactClient(Client):
    def __init__(self):
        super().__init__(ClientType.GenshinImpact)


class StarRailClient(Client):
    def __init__(self):
        super().__init__(ClientType.StarRail)
