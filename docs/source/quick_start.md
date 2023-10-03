# 快速开始

## 依赖

mhyy.py 依赖 Python3 运行环境，请确保你的 Python 版本大于 3.7.

## 安装

mhyy.py 已在 [pypi](https://pypi.org/project/mhyy.py/) 中发布，你可以通过下面的命令安装 mhyy.py

```shell
pip install mhyy.py
```

## 简单使用

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

这样，你就完成了一个基础的签到操作。

其中`r.is_signin`是判断这次操作是否为签到的主要依据。
例程中结果为`True`则代表该操作为签到操作。反之，如果结果为`False`，则为一般获取资产的操作。

详细内容可以参考 [WalletData](document.html#walletdata) 一节
