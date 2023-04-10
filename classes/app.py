# app.py

account = {
    "holder_name": "John",
    "balance": 500,
    "type": "business",
}

def get_account_name(account_name):
    return account["holder_name"]


print(get_account_name(account))