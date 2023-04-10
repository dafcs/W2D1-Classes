# app.py
from modules.bank_account import *

# account = {
#     "holder_name": "John",
#     "balance": 500,
#     "type": "business",
# }

# print(get_account_name(account))


bank_account = BankAccount("John",-100,"personal")
bank_account1 = BankAccount("Bob",302,"personal")
bank_account.pay_in(1000)
# print(bank_account.holder_name)

# bank_account.holder_name = "Pantera"
# print(bank_account.holder_name)

# print(bank_account.balance)

bank_account.pay_monthly_fee()
print(bank_account.balance)

