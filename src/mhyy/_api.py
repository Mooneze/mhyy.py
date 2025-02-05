from ._types import GameType, UserChannel, UserClientType


class API:
    @staticmethod
    def get_launcher_id(game_type: GameType) -> str:
        return {
            GameType.GenshinImpact: "umfgRO5gh5",
            GameType.StarRail: "6P5gHMNyK3",
            GameType.ZZZ: "jGHBHlcOq1",
        }[game_type]

    @staticmethod
    def get_app_id(game_type: GameType, client_type: UserClientType) -> str:
        return {
            UserClientType.Android: {
                GameType.GenshinImpact: "1953439974",
                GameType.StarRail: "1953445976",
                GameType.ZZZ: "1953458679",
            },
            UserClientType.PCWeb: {
                GameType.GenshinImpact: "4",
                GameType.StarRail: "8"
            }
        }[client_type][game_type]

    @staticmethod
    def get_vendor_id(game_type: GameType, client_type: UserClientType) -> str:
        return {
            UserClientType.Android: {
                GameType.GenshinImpact: "1",
                GameType.StarRail: "2",
                GameType.ZZZ: "2",
            },
            UserClientType.PCWeb: {
                GameType.GenshinImpact: "2",
                GameType.StarRail: "2"
            }
        }[client_type][game_type]

    @staticmethod
    def get_cg_game_biz(game_type: GameType) -> str:
        return {
            GameType.GenshinImpact: "hk4e_cn",
            GameType.StarRail: "hkrpg_cn",
            GameType.ZZZ: "nap_cn",
        }[game_type]

    @staticmethod
    def get_op_biz(game_type: GameType) -> str:
        return {
            GameType.GenshinImpact: "clgm_cn",
            GameType.StarRail: "clgm_hkrpg-cn",
            GameType.ZZZ: "clgm_nap-cn",
        }[game_type]

    @staticmethod
    def get_cps(game_type: GameType, client_type: UserClientType) -> str:
        return {
            UserClientType.Android: {
                GameType.GenshinImpact: "mihoyo",
                GameType.StarRail: "mihoyo",
                GameType.ZZZ: "oosnsdyu_C",
            },
            UserClientType.PCWeb: {
                GameType.GenshinImpact: "pc_default",
                GameType.StarRail: "pc_official"
            }
        }[client_type][game_type]

    @staticmethod
    def get_channel_id(game_type: GameType, user_channel: UserChannel) -> str:
        return {
            UserChannel.Official: {
                GameType.GenshinImpact: "mihoyo",
                GameType.StarRail: "mihoyo",
                GameType.ZZZ: "oosnsdyu_C",
            }
        }[user_channel][game_type]

    @staticmethod
    def get_wallet_data_url(game_type: GameType) -> str:
        return {
            GameType.GenshinImpact: "https://api-cloudgame.mihoyo.com/hk4e_cg_cn/wallet/wallet/get",
            GameType.StarRail: "https://cg-hkrpg-api.mihoyo.com/hkrpg_cn/cg/wallet/wallet/get",
            GameType.ZZZ: "https://cg-nap-api.mihoyo.com/nap_cn/cg/wallet/wallet/get"
        }[game_type]

    @staticmethod
    def get_notifications_url(game_type: GameType) -> str:
        return {
            GameType.GenshinImpact: "https://api-cloudgame.mihoyo.com/hk4e_cg_cn/gamer/api/listNotifications",
            GameType.StarRail: "https://cg-hkrpg-api.mihoyo.com/hkrpg_cn/cg/gamer/api/listNotifications",
            GameType.ZZZ: "https://cg-nap-api.mihoyo.com/nap_cn/cg/gamer/api/listNotifications"
        }[game_type]
