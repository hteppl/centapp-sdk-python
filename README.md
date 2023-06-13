# <img src="https://raw.githubusercontent.com/hteppl/centapp-sdk-python/master/docs/logo-main.svg" alt="logo-main" height="66">

#### Python client library for interacting with [CentApp](https://cent.app/) API.

You can find more information on the official [CentApp website](https://cent.app/).

README also available in:

- [Русский](https://raw.githubusercontent.com/hteppl/centapp-sdk-python/master/docs/README_ru.md)

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
token = ''
amount = 100
shop_id = ''

cent_app = CentApp(token)
res = cent_app.bill().create(amount, shop_id)
print(res)
```

**Merchant balance example:**

```python
token = ''

cent_app = CentApp(token)
res = cent_app.merchant().balance()
print(res)
```

