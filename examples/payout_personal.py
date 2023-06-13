from centapp.centapp import CentApp

token = ''
amount = 100
payout_account_id = ''

cent_app = CentApp(token)
res = cent_app.payout().personal_create(amount, payout_account_id)
print(res)
