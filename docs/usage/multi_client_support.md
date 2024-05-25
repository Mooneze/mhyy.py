在 `2.1.0` 版本中，我们添加了 mhyy.py 的第二种客户端类型——
[PCWeb](../api/interface.md#userclienttype)

因此，你可以直接从 云·原神 或 云·星穹铁道 的网页版获取你的 headers。

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