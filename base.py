import json
import requests

class PaystackTransactionInitializer:
    def __init__(self, email, amount, secret_key):
        self.email = email
        self.amount = amount
        self.secret_key = secret_key

    def initialize_transaction(self):
        url = "https://api.paystack.co/transaction/initialize"
        headers = {
            "Authorization": "Bearer " + self.secret_key,
            "Content-Type": "application/json"
        }
        data = {
            "email": self.email,
            "amount": self.amount
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()


secret_key = "enter your secret key here "
email = "customer@email.com"
amount = "20000"

# Initializing the transaction
paystack_initializer = PaystackTransactionInitializer(email, amount, secret_key)
response = paystack_initializer.initialize_transaction()
print(response)
