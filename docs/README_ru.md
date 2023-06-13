# <img src="https://raw.githubusercontent.com/hteppl/centapp-sdk-python/master/docs/logo-main.svg" alt="logo-main" height="66">

[![LICENSE](https://img.shields.io/pypi/l/centapp)](https://pypi.org/project/centapp)
[![Supported Versions](https://img.shields.io/pypi/pyversions/requests.svg)](https://pypi.org/project/centapp)
[![PyPI Version](https://img.shields.io/pypi/v/centapp?color=%23e04f1f)](https://pypi.org/project/centapp)

#### Клиент для взаимодействия с АПИ платежной системы [CentApp](https://cent.app/).

Больше информации о методах на [сайте CentApp](https://cent.app/).

## Установка

CentApp SDK доступен для скачивания через PyPI:

```console
$ python -m pip install centapp
```

CentApp SDK поддерживает Python 3.7+.

## Версия API

`Основной эндпоинт: https://cent.app/api/v1`

Описание работы API и список методов: https://cent.app/en/reference/api

Список доступных модулей:

- /api/v1/bill/
- /api/v1/payment/
- /api/v1/merchant/
- /api/v1/payout/

## Примеры Использования

Больше примеров можно найти в [папке с примерами](https://github.com/hteppl/centapp-sdk-python/tree/master/examples).

**Пример создания платежа:**

```python
token = ''
amount = 100
shop_id = ''

cent_app = CentApp(token)
res = cent_app.bill().create(amount, shop_id)
print(res)
```

**Пример получения баланса мерчанта:**

```python
token = ''

cent_app = CentApp(token)
res = cent_app.merchant().balance()
print(res)
```

