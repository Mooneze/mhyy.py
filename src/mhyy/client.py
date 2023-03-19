import httpx

from .user import User, WalletData, SignInResult
from ._constants import URL
from ._types import NotificationTypes, NotificationStatus


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

    @property
    def version(self):
        return self._version

    def get_wallet_data(self, user: User) -> WalletData:
        """
        Get the wallet data
        :param user: The user performing the operation, should be a User
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

    def get_notifications(
            self,
            user: User,
            *,
            notification_status: NotificationStatus = None,
            notification_type: NotificationTypes = None,
            is_sort: bool = False
    ) -> list:
        """
        Get the notifications
        :param user: The user performing the operation, should be a User
        :param notification_status: The status of the notification, should be a type of NotificationStatus
        :param notification_type: The type of the notification, should be a type of NotificationTypes
        :param is_sort: Whether the returned results are displayed from old to new, should be a bool
        :return: The notification list of the user
        """
        header = {
            'User-Agent': 'okhttp/4.9.0',
            'Referer': 'https://app.mihoyo.com'
        }
        header.update(user.headers)
        header["x-rpc-app_version"] = self._version
        params = {}

        if notification_status:
            params["status"] = notification_status.value
        if notification_type:
            params["type"] = notification_type.value

        params["is_sort"] = str(is_sort).lower()
        r = httpx.get(URL.MHY_NOTIFICATION_URL, params=params, headers=header).json()
        return r["data"]["list"]

    def sign_in(self, user: User) -> SignInResult:
        """
        Do sign in
        :param user: The user performing the operation, should be a User
        :return: The wallet data of the user
        """
        return SignInResult(self.get_wallet_data(user))
