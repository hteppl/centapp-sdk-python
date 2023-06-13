from centapp.centapp import CentApp

token = ''
amount = 100
shop_id = ''

cent_app = CentApp(token)
res = cent_app.bill().create(amount, shop_id)
print(res)
