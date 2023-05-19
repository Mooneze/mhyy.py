import enum
import typing

import httpx

from ._url import APIStatic, APICloudGame
from ._wallet import WalletData
from ._user import User
from ._exception import WebRequestError, APIError

T = typing.TypeVar("T", bound="Client")


class ClientState(enum.IntEnum):
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
    def __init__(self: T):
        self._client = httpx.Client()
        self._status = ClientState.UNOPENED
        version_rep = self._client.get(APIStatic.VERSION)
        self._version = version_rep.json()["data"]["game"]["latest"]["version"]

    def __enter__(self: T) -> T:
        if self._state != ClientState.UNOPENED:
            msg = {
                ClientState.OPENED: "Cannot open a client instance more than once.",
                ClientState.CLOSED: "Cannot reopen a client instance, once it has been closed.",
            }[self._state]
            raise RuntimeError(msg)

        self._state = ClientState.OPENED
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._status = ClientState.CLOSED
        self._client.close()

    def close(self) -> None:
        self._status = ClientState.CLOSED
        self._client.close()

    @property
    def is_closed(self) -> bool:
        return self._status == ClientState.CLOSED

    @property
    def status(self) -> ClientState:
        return self._status

    @property
    def version(self) -> str:
        return self._version

    def get_wallet(self, user: User) -> WalletData:
        headers = {
            "x-rpc-app_version": self._version,
            "x-rpc-app_id": "1953439974",
            "x-rpc-vendor_id": "1",
            "Referer": "https://app.mihoyo.com"
        }
        headers.update(user.header)
        resp = self._client.get(APICloudGame.WALLET, headers=headers)
        if resp.status_code != 200:
            raise WebRequestError(f"Status code: {resp.status_code}")
        resp_data = resp.json()
        if resp_data["retcode"] != 0:
            raise APIError(f"Retcode: {resp_data['retcode']}, Message: {resp_data['message']}")
        return WalletData(resp_data["data"])

