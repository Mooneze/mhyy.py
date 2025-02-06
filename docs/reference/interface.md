# API 参考

这里是 mhyy.py 的 API 参考！慢慢寻找吧！

### 索引

- [Client](#client)
- [GameType](#gametype)
- [Notification](#notification)
- [NotificationStatus](#notificationstatus)
- [NotificationType](#notificationtype)
- [User](#user)
- [UserChannel](#userchannel)
- [UserClientType](#userclienttype)
- [WalletData](#walletdata)

## Client {#client}

_mhyy.Client()_

> 米哈云游客户端。

`versions`: dict

> 所有游戏类型的版本号字典，若只想获取指定游戏类型的版本号，请使用 get_client_version() 方法。

`get_wallet_data`(self, user: [User](#user))

> 获取指定用户的钱包数据。
>
> **形参:**
>
> - user ([**User**](#user)): 发起请求的用户。
>
> **返回值:** [`WalletData`](#walletdata) - 该用户的钱包数据。

`get_notifications`(self, user: [User](#user), *, status: Optional[[NotificationStatus](#notificationstatus)] = None,
type_: Optional[[NotificationType](#notificationtype)] = None, is_sort: Optional[bool] = True)

> 获取指定用户的通知信息。
>
> **形参:**
>
> - user ([**User**](#User)): 发起请求的用户。
> - status (**Optional[[NotificationStatus](#notificationstatus)]**): 筛选指定的通知状态。
> - type_ (**Optional[[NotificationType](#notificationtype)]**): 筛选指定的通知种类。
> - Optional (**Optional[bool]**): 是否排序。
>
> **返回值:** `List[`[`Notification`](#notification)`]` - 一个列表，包含了指定用户的通知信息。

`get_client_version`(self, game_type: [GameType](#gametype))

> 获取指定游戏类型的版本号。
> 若未发送过对应游戏类型的网络请求，使用本方法将会更新对应版本版本号。
> 若想获取字典类型的所有版本号，请使用 versions 属性。
>
> **形参:**
>
> - game_type ([**GameType**](#gametype)): 游戏类型。
>
> **返回值:** `str` - 该游戏类型的版本号。

## GameType {#gametype}

_class mhyy.GameType_

> 游戏类型。

`GenshinImpact` = 0

> 云·原神。

`StarRail` = 1

> 云·星穹铁道。

`ZZZ` = 2

> 云·绝区零

## Notification {#notification}

> 通知类。

_class mhyy.Notification_
(id_: str, status: [NotificationStatus](#notificationstatus), type_:
[NotificationType](#notificationtype), priority: int, source: str, desc: str, msg: str, created_at: str)

`id`: str

> 通知 ID。

`status`: [NotificationStatus](#notificationstatus)

> 通知状态。

`type`: [NotificationType](#notificationtype)

> 通知种类。

`priority`: int

> 作用未知，根据名称推测是通知的优先级。

`source`: str

> 作用未知。

`desc`: str

> 作用未知，根据名称推测是通知的描述。

`msg`: str

> 一个字符串，包含了 json 文本格式的该通知的内容。

`create_at`: str

> 一个字符串，是秒级的时间戳 (10位)，描述了该通知何时被创建。

`from_data_dict`(cls, data: dict)

> 从特定的数据结构生成 Notification。
>
> **形参:**
>
> - data (**dict**): 消息数据。
>
> **返回值:** [`Notification`](#notification) - 包装后的消息数据。

## NotificationStatus {#notificationstatus}

_class mhyy.NotificationStatus_

> 通知状态。

`Read` = 'NotificationStatusRead'

> 已读。

`Unread` = 'NotificationStatusUnread'

> 未读。

`Undefined` = 'NotificationStatusUndefined'

> 未定义。

`get_status_by_name`(cls, status: str)

> 从字符串获取枚举成员。
>
> **形参:**
>
> - status (**str**): 成员字符串。
>
> **返回值:** [`NotificationStatus`](#notificationstatus) - 枚举成员。

## NotificationType {#notificationtype}

_class mhyy.NotificationType_

> 通知种类。

`Popup` = 'NotificationTypePopup'

> 弹窗通知。

`Undefined` = 'NotificationTypeUndefined'

> 未定义。

`get_type_by_name`(cls, type_: str)

> 从字符串获取枚举成员。
>
> **形参:**
>
> - status (**str**): 成员字符串。
>
> **返回值:** [`NotificationType`](#notificationtype) - 枚举成员。

## User {#user}

_class mhyy.User(combo_token: str, sys_version: str, device_id: str, device_name: str, device_model: str,
client_type: [UserClientType](#userclienttype), *, game_type: Optional[[GameType](#gametype)] = None, 
channel: Optional[[UserChannel](#userchannel)] = UserChannel.Official
)_

> 用户类。
>
> **形参:**
>
> - combo_token (**str**): 对应 headers 中的 x-rpc-combo_token。
> - sys_version (**str**): 对应 headers 中的 x-rpc-sys_version。
> - device_id (**str**): 对应 headers 中的 x-rpc-device_id。
> - device_name (**str**): 对应 headers 中的 x-rpc-device_name。
> - device_model (**str**): 对应 headers 中的 x-rpc-device_model。
> - client_type (**[UserClientType](#userclienttype)**): 用户的客户端种类。
> - game_type (**Optional[[GameType](#gametype)]**): 游戏类型，若为空则将会从 combo_token 中自动识别。
> - channel (**Optional[[UserChannel](#userchannel)]**): 用户的游戏渠道。

::: info

这里不提供成员的文档说明，因为他是形参的 Getter。

:::

`combo_token`: str

`sys_version`: str

`device_id`: str

`device_name`: str

`device_model`: str

`client_type`: str

`game_type`: [GameType](#gametype)

`channel`: [UserChannel](#userchannel)

`get_user_headers`(self)

> 获取该用户的 headers。
>
> **返回值:** dict - 字典格式的该用户的 headers。

## UserChannel {#userchannel}

_class mhyy.UserChannel_

> 游戏渠道。

::: info

目前 mhyy.py 仅支持官方服务器的操作。

:::

`Official` = 0

> 官方服。

## UserClientType {#userclienttype}

_class mhyy.UserClientType_

> 客户端类型。

`Android` = 2

> 安卓。

`PCWeb` = 16

> PC 网页版。

## WalletData {#walletdata}

_class mhyy.WalletData_

::: info

事实上，mhyy.WalletData包含五个子类，分别是
`mhyy.CoinData`、`mhyy.FreeTimeData`、`mhyy.StatusData`、
`mhyy.StatData`、`mhyy.PlayCardData`。

但这些成员子类都没有导出且 `mhyy.WalletData` 与他的成员子类都是 `dataclass`。
没有构造函数，仅供读取数据。

所以在本文档中不会描述其五个子类，仅当作类属性描写。

:::

`total_time`: int

> 包含了付费时长和免费时长的总时长。

### `coin`

> 用户的 原点 / 星云币 时长数据。

`coin.coin_num`: int

> 原点 / 星云币 数。

`coin.free_coin_num`: int

> 免费 原点 / 星云币 数。

`coin.coin_limit`: int

> 原点 / 星云币 的数量上限。

`coin.exchange`: int

> 与原点时长的汇率。通常来说，10 原点 / 星云币 = 1 游戏时长。

### `free_time`

> 用户的免费时长数据。

`free_time.send_freetime`: int

> 若该用户是本日第一次登录，那么此处的值为每日赠送的免费时长 (min)。反之，此处恒为 0。

`free_time.free_time`: int

> 总免费时长 (min)。

`free_time.free_time_limit`: int

> 免费时长上限 (min)。

`free_time.over_freetime`: int

> 该用户是本日第一次登录且赠送的时长有一部分超出了免费时长上限，那么此处的值为溢出的免费时长 (min)。

### `status`

> 未知数据

::: warning

这是一条未知的数据，具体内容待补充。

:::

`status.status`: int

`status.msg`: str

`status.total_time_status`: int

`status.status_new`: int

### `stat`

> 未知数据

::: warning

这是一条未知的数据，具体内容待补充。

:::

`vip_point`: str

### `play_card`

> 用户的畅玩卡数据

`play_card.expire`: str

> 畅玩卡过期时间（格式未知）

::: warning

这是一条未知的数据，请谨慎使用。

:::

`play_card.msg`: str

> 畅玩卡信息

`play_card.short_msg`: str

> 畅玩卡短信息 / 状态

`play_card.play_card_limit`: str

> 未知

::: warning

这是一条未知的数据，具体内容待补充。

:::

`remaining_sec`: str

> 未知

::: warning

这是一条未知的数据，具体内容待补充。

:::

`play_card_tag`: str

> 未知

::: warning

这是一条未知的数据，具体内容待补充。

:::
