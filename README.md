# mhyy.py

![LICENSE](https://img.shields.io/github/license/GuangChen2333/mhyy.py?style=flat-square)
![PyP](https://img.shields.io/pypi/v/mhyy.py?style=flat-square)
![Python](https://img.shields.io/pypi/pyversions/mhyy.py?style=flat-square)
![STARS](https://img.shields.io/github/stars/GuangChen2333/mhyy.py?style=flat-square)

Python 米哈云游（云原神）签到功能与相关方法的API

## 快速开始

- 从 `PyPi` 安装 `mhyy.py`

```shell
pip install mhyy.py
```

- 签到功能的实现

```python
from mhyy import User, Client

# 实例化一个客户端~
client = Client()

# 当然要有用户啦！
user = User(
    combo_token="",  # 对应 Headers 中的 x-rpc-combo_token
    sys_version="",  # 对应 Headers 中的 x-rpc-sys_version
    device_id="",  # 对应 Headers 中的 x-rpc-device_id
    device_name="",  # 对应 Headers 中的 x-rpc-device_name
    device_model="",  # 对应 Headers 中的 x-rpc-device_model
    nickname=""  # 这个是便于识别的昵称，选填~
)

# 执行签到并返回一个 SignInResult 对象
r = client.sign_in(user)

# 打印 SignInResult 返回的签到结果，结果是枚举 SignInResultTypes 的一个对象
print(r.result.name)
```

## 文档

关于文档中的 `对象方法` 一栏，若无特殊说明，均为动态方法

### 关于 Client

Client 是一个虚拟的客户端对象，用于执行一系列操作

#### 构造器:

`Client(version: str = None)`

对于其中的 version 字段，若不指定，则为最新版本

#### 对象属性:

- `vesion: str` -> 客户端版本

#### 对象方法:

- `get_wallet_data(user: User) -> WalletData` -> 获取用户的钱包信息
- `get_notifications(user: User) -> list`
- -  -> 获取用户的通知，其中，含有形参
- - `notification_status: NotificationStatus`, 
- - `notification_type: NotificationTypes`, 
- - `is_sort: bool = False`

### 关于 SignInResult

SignInResult 是一个只读对象，用于返回签到结果

#### 对象属性:

- `result: SignInResultTypes` -> 签到结果
- `wallet_data: WalletData` -> 你的钱包数据
- `user: User` -> 所属用户

### 关于 WalletData

WalletData 是一个只读对象，用于返回你的钱包数据

#### 对象属性:

- `coin: int` -> 米云币
- `free_time: int` -> 免费时长（分钟）
- `send_free_time: int` -> 新增的免费时长（分钟）
- `is_play_card: bool` -> 是否是畅玩卡
- `coin_limit: int` -> 米云币上限
- `free_time_limit: int` -> 免费时长上限（分钟）
- `user: User` -> 所属用户

#### 对象方法

- `free_date_time() -> datetime.time` -> 获取免费时长对象
- `coin_date_time() -> datetime.time` -> 获取付费时长（米云币时长）对象