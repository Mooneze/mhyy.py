from ._types import GameType, UserChannel


class API:
    @staticmethod
    def get_launcher_key(game_type: GameType) -> str:
        return {
            GameType.GenshinImpact: "eYd89JmJ",
            GameType.StarRail: "6KcVuOkbcqjJomjZ"
        }[game_type]

    @staticmethod
    def get_launcher_id(game_type: GameType) -> str:
        return {
            GameType.GenshinImpact: "18",
            GameType.StarRail: "33"
        }[game_type]

    @staticmethod
    def get_game_version_url(game_type: GameType) -> str:
        return {
            GameType.GenshinImpact: "https://sdk-static.mihoyo.com/hk4e_cn/mdk/launcher/api/resource",
            GameType.StarRail: "https://api-launcher.mihoyo.com/hkrpg_cn/mdk/launcher/api/resource"
        }[game_type]

    @staticmethod
    def get_app_id(game_type: GameType) -> str:
        return {
            GameType.GenshinImpact: "1953439974",
            GameType.StarRail: "1953445976"
        }[game_type]

    @staticmethod
    def get_vendor_id(game_type: GameType) -> str:
        return {
            GameType.GenshinImpact: "1",
            GameType.StarRail: "2"
        }[game_type]

    @staticmethod
    def get_cg_game_biz(game_type: GameType) -> str:
        return {
            GameType.GenshinImpact: "hk4e_cn",
            GameType.StarRail: "hkrpg_cn"
        }[game_type]

    @staticmethod
    def get_op_biz(game_type: GameType) -> str:
        return {
            GameType.GenshinImpact: "clgm_cn",
            GameType.StarRail: "clgm_hkrpg-cn"
        }[game_type]

    @staticmethod
    def get_cps(game_type: GameType) -> str:
        return {
            GameType.GenshinImpact: "cyydmihoyo",
            GameType.StarRail: "gw_An_C"
        }[game_type]

    @staticmethod
    def get_channel_id(user_channel: UserChannel, game_type: GameType) -> str:
        channels = {
            UserChannel.Official: {
                GameType.GenshinImpact: "cyydmihoyo",
                GameType.StarRail: "gw_An_C"
            }
        }
        return channels[user_channel][game_type]

    @staticmethod
    def get_wallet_data_url(game_type: GameType) -> str:
        return {
            GameType.GenshinImpact: "https://api-cloudgame.mihoyo.com/hk4e_cg_cn/wallet/wallet/get",
            GameType.StarRail: "https://cg-hkrpg-api.mihoyo.com/hkrpg_cn/cg/wallet/wallet/get"
        }[game_type]

    @staticmethod
    def get_notifications_url(game_type: GameType) -> str:
        return {
            GameType.GenshinImpact: "https://api-cloudgame.mihoyo.com/hk4e_cg_cn/gamer/api/listNotifications",
            GameType.StarRail: "https://cg-hkrpg-api.mihoyo.com/hkrpg_cn/cg/gamer/api/listNotifications"
        }[game_type]
