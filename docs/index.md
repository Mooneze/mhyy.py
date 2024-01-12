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
$ pip install mhyy.py
```

像这样修改你的 headers 后进行签到操作吧 :

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
