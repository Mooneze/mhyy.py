# 快速开始 {#quick-start}

## 安装 {#installation}

### 前置准备 {#prerequisites}

- [Python](https://www.python.org/) 3.8 及以上版本。

mhyy.py 已托管到 pypi，你可以通过 `pip` 来安装它。

::: code-group

```shell [pip]
$ pip install mhyy.py
```

```shell [uv]
$ uv pip install mhyy.py
```

:::

### 在项目中使用 mhyy.py {#use-mhyy-py}

```python
import mhyy
```

::: details 使用另一种导入方式？

对于大多数情况，你可以使用如下方法：

```python
from mhyy import Client, User, UserClientType
```

:::

## 迈出第一步 {#your-first-step}

本小节将以实现签到并获取当前总余额时间之功能为题，向你介绍如何使用 mhyy.py。

### 定义一个客户端吧 {#define-client}

在 mhyy.py中，无论什么游戏，所有操作都是基于客户端 (Client) 的。像这样定义你的客户端吧：

```python
client = mhyy.Client()
```

### 定义一个用户吧 {#define-user}

客户端需要用户才知道谁需要执行操作，像这样：

```python
user = mhyy.User(
    combo_token="x-rpc-combo_token",
    sys_version="x-rpc-sys_version",
    device_id="x-rpc-device_id",
    device_name="x-rpc-device_name",
    device_model="x-rpc-device_model",
    client_type=mhyy.UserClientType.PCWeb
)
```

其中的 `combo_token`, `sys_version`, `device_id`, `device_name`,
`device_model` 都需要你通过抓包来获取。

你也可以通过 [Easy-MHYY](https://github.com/Mooneze/Easy-MHYY) 来获取适用于 `mhyy.UserClientType.PCWeb`
的这些字段。

需要注意的是，`client_type` 需要根据你抓包的平台进行切换，目前支持的平台有:

- Android 端: `mhyy.UserClientType.Android`
- PC 网页端: `mhyy.UserClientType.PCWeb`

### 进行签到吧 {#let-us-sign-in}

在米哈云游的逻辑中，签到操作是获取钱包 (Wallet) 操作的一部分。因此，如果我们想要签到，
我们就需要获取我们的钱包 (Wallet)。

我们封装了获取钱包 (Wallet) 的方法 `Client.get_wallet_data() -> WalletData`，像这样获取用户的钱包吧：

```python
r = client.get_wallet_data(user)
```

在这步操作中，我们将用户的钱包信息装进了 `r` 这个变量中。

你也可以通过执行 `WalletData.is_sign_in() -> bool`，来判断本次是否进行了签到。

```python
if r.is_sign_in():
    print("进行了签到。") 
```

### 获得时长信息吧

现在距离我们的目标只差了一步, 通过获取 `WalletData.total_time -> int` 可以获取你的账户内总时长，即付费时长 + 免费时长。

也可以获取 `WalletData.coin.coin_num -> int` 和 `WalletData.free_time.free_time -> int` 来分别获取它们。

像这样输出你的结果吧：

```python
print(f"总时长: {r.total_time}, 付费时长: {r.coin.coin_num}, 免费时长: {r.free_time.free_time}")
```

你也可以通过 `WalletData.free_time.send_freetime -> int` 来完善你的签到操作输出：

```python
if r.is_sign_in():
    print(f"进行了签到，新增免费时长: {r.free_time.send_freetime}") 
```

::: details 完整示例？

```python
# 现在，让我们复习一下吧。
import mhyy  # 导入 mhyy.py

client = mhyy.Client()  # 实例化 Client
user = mhyy.User(
    combo_token="x-rpc-combo_token",
    sys_version="x-rpc-sys_version",
    device_id="x-rpc-device_id",
    device_name="x-rpc-device_name",
    device_model="x-rpc-device_model",
    client_type=mhyy.UserClientType.PCWeb
)  # 实例化 User

r = client.get_wallet_data(user)  # 获取钱包信息

if r.is_sign_in():  # 判断是否进行了签到
    print(f"进行了签到，新增免费时长: {r.free_time.send_freetime}")

print(f"总时长: {r.total_time}, 付费时长: {r.coin.coin_num}, 免费时长: {r.free_time.free_time}")
```

:::

::: tip 想要探寻更多？

跳到 [API参考](../reference/interface.md)。

:::
