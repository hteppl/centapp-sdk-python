from centapp.centapp import CentApp

token = ''

cent_app = CentApp(token)
res = cent_app.merchant().balance()
print(res)
