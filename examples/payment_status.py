from centapp.centapp import CentApp

token = ''
payment_id = ''

cent_app = CentApp(token)
res = cent_app.payment().status(payment_id)
print(res)
