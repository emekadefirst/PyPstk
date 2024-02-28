import json
import requests

class PaystackTransactionInitializer:
    def __init__(self, email, amount, secret_key):
        self.email = email
        self.amount = amount
        self.secret_key = secret_key

class pay(PaystackTransactionInitializer):    
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
    
    def payment_status(self, reference):
        url = f'https://api.paystack.co/transaction/verify/{reference}'
        headers = {
            'Authorization': f'Bearer {self.secret_key}'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print(response.json())
        else:
            print("Error:", response.text)

secret_key = "sk_test_daf386e7071c4613e54e4b71f43926409abd811e"
email = "customer@email.com"
amount = "20000"

# Initializing the transaction
paystack_initializer = pay(email, amount, secret_key)
response = paystack_initializer.initialize_transaction()
print(response)

reference = response['data']['reference']
paystack_initializer.payment_status(reference)
