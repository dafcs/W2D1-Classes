

class BankAccount:
    def __init__(self, input_holder_name, input_balance, input_type):
        self.holder_name = input_holder_name #the property of "holder_name" 
        self.balance = input_balance
        self.type = input_type
        self._rates = {
            "personal" :10,
            "business":50,
            "gold":100
        }


    def pay_in(self,amount):
        self.balance += amount
    
    def pay_monthly_fee(self):
        if self.balance -= self._rates[self.type]


