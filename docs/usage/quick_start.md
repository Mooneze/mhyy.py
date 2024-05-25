首先，我们假设你已经安装好了 mhyy.py，如果你还没有，请参见 [安装方式](../index.md#_4) 小节。

让我们先导入 mhyy.py。

```pycon
>>> import mhyy
```

## 定义一个用户

在进行这一步之前，你要通过 **抓包** 等方式获取用户的 headers 信息。

若你已经拥有了你的 headers，像这样定义一个用户吧:

```pycon
>>>user = mhyy.User(
...     combo_token="x-rpc-combo_token",
...     sys_version="x-rpc-sys_version",
...     device_id="x-rpc-device_id",
...     device_name="x-rpc-device_name",
...     device_model="x-rpc-device_model",
...     client_type=mhyy.UserClientType.Android
... )
```

至此，你已经完成了定义用户的操作。

这里的 `client_type` 是根据你的抓包客户端来选择的，如果你的客户端是云·原神（星穹铁道）
网页版，请选择`mhyy.UserClientType.PCWeb`。

参见 [多客户端支持](./multi_client_support.md)。

## 定义一个客户端并进行客户端操作

这一步你并不需要准备任何东西，你只需要像这样：

```pycon
>>> client = mhyy.Client()
```

至此，你已经完成了客户端的定义。

!!! Tip

    在进行客户端操作前，你需要先了解一下：

    在 mhyy.py 中不同种游戏是共同使用一个客户端的，那意味着你可以使用同一个客户端对不同游戏种类的不同用户进行操作。

    游戏种类将由 mhyy.py 根据 `combo_token` 自动判断或由你自己填写。

    参见 [User](../api/interface.md#user)、[GameType](../api/interface.md#gametype)


### 获取钱包信息 / 签到

这可能是使用 mhyy.py 最多的场景了，你只需要像这样：

```pycon
>>> wallet = client.get_wallet_data(user=user)
```

就可以将这个用户的钱包信息储存到 `wallet` 变量中。

这个操作适用于获取该用户的获取钱包信息或者白嫖每天赠送的 15 分钟免费时长。

!!! Note

    只有每天第一次进行 获取钱包信息 / 签到 操作才能视为签到操作

    你可以使用这个代码来判断：

    [`wallet.is_sign_in()`](../api/interface.md#walletdata) 将会返回本次操作是否为签到操作。

具体返回的内容请参考开发人员接口中的 [WalletData](../api/interface.md#walletdata) 小结。

### 获取通知列表

这个操作用于获取指定用户的通知信息，像这样：

```pycon
>>> notifications = client.get_notifications(user=user)
```

就可以获取该用户的所有通知。

如果你只想获得**未读**通知，你需要修改一下你的代码：

```pycon
>>> notifications = client.get_notifications(user=user, status=mhyy.NotificationStatus.Unread)
```

至此，你已经学会了 mhyy.py 的核心用法，具体客户端操作请参考开发人员接口中的 [Client](../api/interface.md#client) 小节。