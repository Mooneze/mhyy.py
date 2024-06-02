# 多客户端支持
在 `2.1.0` 版本中，我们添加了 mhyy.py 的第二种客户端类型——
[PCWeb](../api/interface.md#userclienttype)

事实上，你可以在 [UserClientType](../api/interface.md#userclienttype) 中找到
你所对应平台的 `client_type` 值。

!!! Tips

    请确保你的 Headers 与用户字段的 client_type 相对应。

    若你还没有获取 Headers，请转到 [获取你的 Headers](../appendix/get_headers.md)

## 米哈云游网页版

你可以直接从 云·原神 或 云·星穹铁道 的网页版获取你的 Headers。

所以你可以这样定义你在云游戏网页版的用户：

```python
from mhyy import User, UserClientType

user = User(
    combo_token="x-rpc-combo_token",
    sys_version="x-rpc-sys_version",
    device_id="x-rpc-device_id",
    device_name="x-rpc-device_name",
    device_model="x-rpc-device_model",
    client_type=UserClientType.PCWeb
)
```

其中 `client_type` 是该用户 Headers 所对应的平台。

## 安卓版

同上，安卓版应该如此定义。

```python
from mhyy import User, UserClientType

user = User(
    combo_token="x-rpc-combo_token",
    sys_version="x-rpc-sys_version",
    device_id="x-rpc-device_id",
    device_name="x-rpc-device_name",
    device_model="x-rpc-device_model",
    client_type=UserClientType.Android
)
```
