# <img src="https://raw.githubusercontent.com/hteppl/centapp-sdk-python/master/docs/logo-main.svg" alt="logo-main" height="66">

[![LICENSE](https://img.shields.io/pypi/l/centapp)](https://pypi.org/project/centapp)
[![Supported Versions](https://img.shields.io/pypi/pyversions/requests.svg)](https://pypi.org/project/centapp)
[![PyPI Version](https://img.shields.io/pypi/v/centapp?color=%23e04f1f)](https://pypi.org/project/centapp)

#### Python client library for interacting with [CentApp](https://cent.app/) API.

You can find more information on the official [CentApp website](https://cent.app/).

README also available in:

- [Русский](https://github.com/hteppl/centapp-sdk-python/blob/master/docs/README_ru.md)

## Installing

CentApp SDK is available on PyPI:

```console
$ python -m pip install centapp
```

CentApp SDK officially supports Python 3.7+.

## API Version and Reference

`Base api url: https://cent.app/api/v1`

API reference and official docs: https://cent.app/en/reference/api

The list of available modules:

- /api/v1/bill/
- /api/v1/payment/
- /api/v1/merchant/
- /api/v1/payout/

## API Examples

You can find more examples [in examples folder](https://github.com/hteppl/centapp-sdk-python/tree/master/examples).

**Bill creation example:**

```python
from centapp import centapp

token = ''
amount = 100
shop_id = ''

cent_app = centapp.CentApp(token)
res = cent_app.bill().create(amount, shop_id)
print(res)
```

**Merchant balance example:**

```python
from centapp import centapp

token = ''

cent_app = centapp.CentApp(token)
res = cent_app.merchant().balance()
print(res)
```

