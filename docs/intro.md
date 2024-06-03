<h1 style="text-align: center; font-size: 3rem; margin-top: -10px; margin-bottom: 10px">
    mhyy.py
</h1>

---

<div style="display:flex; justify-content: center; align-items: center; margin-top: -5px">
    <p>
        <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/mhyy.py">
        <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/mhyy.py">
    </p>
</div>

<div style="display:flex; justify-content: center; align-items: center; margin-top: 5px; margin-bottom: 5px">
    <em>米哈云游（云·原神、云·星穹铁道）签到方法及其他方法的API封装</em>
</div>

---

使用 pip 安装 mhyy.py :

```shell
pip install mhyy.py
```

像这样创建用户并填写 headers 后进行签到操作吧 :

```pycon
>>> from mhyy import User, Client, UserClientType
>>> user = User(
...     combo_token="x-rpc-combo_token",
...     sys_version="x-rpc-sys_version",
...     device_id="x-rpc-device_id",
...     device_name="x-rpc-device_name",
...     device_model="x-rpc-device_model",
...     client_type=UserClientType.Android
... )
>>> client = Client()
>>> r = client.get_wallet_data(user)
>>> r
WalletData(coin=CoinData(coin_num=0, free_coin_num=0, coin_limit=200000, ...))
>>> r.free_time.free_time
600
>>> r.free_time.send_freetime
15
>>> r.is_sign_in()
True
```

是的，mhyy.py 支持 云·原神、云·星穹铁道 以及它们的网页版。你无需填写某一位用户属于什么游戏，mhyy.py 将会自动识别并进行操作。

在上述操作中，你成功完成了从**定义用户**到**获取钱包信息**再到**判断是否进行了签到操作**的过程。

关于如何获取 Headers，请转到 [获取你的Headers](appendix/get_headers.md)

## 特性

得益于 [httpx](https://www.python-httpx.org/) 的优秀，mhyy.py 有足够的稳定性。

- 支持 云·原神、云·星穹铁道。
- 支持 多类型客户端。
- 支持 多种用户共用同一个客户端。
- 简易的 API 封装。

## 文档

如果你想要继续学习 mhyy.py 的有关知识，请转到 [快速入门](usage/quick_start.md)。

[API 参考](api/interface.md) 提供了mhyy.py API 参考。

## 依赖

mhyy.py 依赖于以下优秀的开源库。

- [`httpx`](https://github.com/encode/httpx/) mhyy.py 的底层实现。
- [`dataclasses-json`](https://github.com/lidatong/dataclasses-json) 用于封装数据类。

## 安装方式

> [!Note]
>
 >   mhyy.py 需要 python 3.8 及以上运行环境！

使用 pip 安装 mhyy.py :

```shell
$ pip install mhyy.py
```
