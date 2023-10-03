# 快速开始

从 pip 安装mhyy.py

```shell
pip install mhyy.py
```

现在让我们开始操作吧

```pycon
>>> from mhyy import Client, User
>>> client = Client()
>>> user = User(
...     combo_token="x-rpc-combo_token",
...     sys_version="x-rpc-sys_version",
...     device_id="x-rpc-device_id",
...     device_name="x-rpc-device_name",
...     device_model="x-rpc-device_model"
... )
>>> r = client.get_wallet(user)
>>> r
WalletData({'coin': {'coin_num': '1160', 'free_coin_num': '0', 'coin_limit': '150000', 'exchange': '10'}, ...)
>>> r.is_signin
True
>>> r.free_time.sent
datetime.time(0, 15)
>>> r.free_time.total
datetime.time(6, 10)
```

这样，你就完成了一个基础的签到操作
