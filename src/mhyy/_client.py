import enum
import typing

import httpx

from ._constants import URL

T = typing.TypeVar("T", bound="Client")


class ClientState(enum.StrEnum):
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
    def __init__(self):
        self._client = httpx.Client()
        self._status = ClientState.UNOPENED
        version_rep = self._client.get(URL.LAUNCHER_VERSION_URL)
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
