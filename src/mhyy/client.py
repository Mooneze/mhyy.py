import httpx

from .user import User, WalletData, SignInResult
from ._constants import URL


def get_latest_version() -> str:
    """
    Get the latest version
    :return: the latest version of the game
    """
    resp = httpx.get(URL.MHY_VERSION_URL).json()
    return resp["data"]["game"]["latest"]["version"]


class Client:
    def __init__(self, version: str = None):
        """
        :param version: the version of miHoYo Cloud Gaming Client
        """
        if version is None:
            self._version = get_latest_version()
        else:
            self._version = version

    def get_wallet_data(self, user: User) -> WalletData:
        """
        Get the wallet data
        :param user: The user performing the operation
        :return: The sign in result of the user
        """
        header = {
            'User-Agent': 'okhttp/4.9.0',
            'Referer': 'https://app.mihoyo.com'
        }
        header.update(user.headers)
        header["x-rpc-app_version"] = self._version
        r = httpx.get(URL.MHY_WALLET_URL, headers=header).json()
        return WalletData.from_wallet(user, r["data"])

    def get_notifications(self, user: User) -> list:
        """
        Get the notifications
        :param user: The user performing the operation
        :return: The notification list of the user
        """
        header = {
            'User-Agent': 'okhttp/4.9.0',
            'Referer': 'https://app.mihoyo.com'
        }
        header.update(user.headers)
        header["x-rpc-app_version"] = self._version
        r = httpx.get(URL.MHY_NOTIFICATION_URL).json()
        return r["data"]["list"]

    def sign_in(self, user: User) -> SignInResult:
        """
        Do sign in
        :param user: The user performing the operation
        :return: The wallet data of the user
        """
        return SignInResult(self.get_wallet_data(user))
