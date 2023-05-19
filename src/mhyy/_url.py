API_CLOUDGAME = "https://api-cloudgame.mihoyo.com"
SDK_STATIC = "https://sdk-static.mihoyo.com"


class APICloudGame:
    WALLET = API_CLOUDGAME + "/hk4e_cg_cn/wallet/wallet/get"
    NOTIFICATION = API_CLOUDGAME + "/hk4e_cg_cn/gamer/api/listNotifications"


class APIStatic:
    VERSION = SDK_STATIC + "/hk4e_cn/mdk/launcher/api/resource?key=eYd89JmJ&launcher_id=18"
