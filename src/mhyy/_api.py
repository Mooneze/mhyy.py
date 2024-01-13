from ._client import ClientType
from ._user import UserChannel

class API:
    @staticmethod
    def get_launcher_key(client_type: ClientType) -> str:
        return {
            ClientType.GenshinImpact: "eYd89JmJ",
            ClientType.StarRail: "6KcVuOkbcqjJomjZ"
        }[client_type]

    @staticmethod
    def get_launcher_id(client_type: ClientType) -> str:
        return {
            ClientType.GenshinImpact: "18",
            ClientType.StarRail: "33"
        }[client_type]

    @staticmethod
    def get_game_version_url(client_type: ClientType) -> str:
        return {
            ClientType.GenshinImpact: "https://sdk-static.mihoyo.com/hk4e_cn/mdk/launcher/api/resource",
            ClientType.StarRail: "https://api-launcher.mihoyo.com/hkrpg_cn/mdk/launcher/api/resource"
        }[client_type]

    @staticmethod
    def get_app_id(client_type: ClientType) -> str:
        return {
            ClientType.GenshinImpact: "1953439974",
            ClientType.StarRail: "1953445976"
        }[client_type]

    @staticmethod
    def get_vendor_id(client_type: ClientType) -> str:
        return {
            ClientType.GenshinImpact: "1",
            ClientType.StarRail: "2"
        }[client_type]

    @staticmethod
    def get_cg_game_biz(client_type: ClientType) -> str:
        return {
            ClientType.GenshinImpact: "hk4e_cn",
            ClientType.StarRail: "hkrpg_cn"
        }[client_type]

    @staticmethod
    def get_op_biz(client_type: ClientType) -> str:
        return {
            ClientType.GenshinImpact: "clgm_cn",
            ClientType.StarRail: "clgm_hkrpg-cn"
        }[client_type]

    @staticmethod
    def get_cps(client_type: ClientType) -> str:
        return {
            ClientType.GenshinImpact: "cyydmihoyo",
            ClientType.StarRail: "gw_An_C"
        }[client_type]

    @staticmethod
    def get_channel_id(client_type: ClientType, user_channel: UserChannel) -> str:
        channels = {
            UserChannel.Official: {
                ClientType.GenshinImpact: "cyydmihoyo",
                ClientType.StarRail: "gw_An_C"
            }
        }
        return channels[user_channel][client_type]
