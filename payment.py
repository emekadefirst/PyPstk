import json
import requests

class PaystackTransactionInitializer:
    def __init__(self, email, amount, secret_key, ref_id=None, status=None):
        self.email = email
        self.amount = amount
        self.status = status
        self.ref_id = ref_id
        self.secret_key = secret_key

class Pay(PaystackTransactionInitializer):    
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
        
        # Check for request success
        if response.status_code == 200:
            # Store the generated reference
            self.ref_id = response.json()['data']['reference']
            return response.json()
        else:
            # Handle errors gracefully
            print("Error:", response.text)
            return None
    
    def payment_status(self):
        # Use the stored reference
        if not self.ref_id:
            print("Error: Reference not found")
            return None
        
        url = f'https://api.paystack.co/transaction/verify/{self.ref_id}'
        headers = {
            'Authorization': f'Bearer {self.secret_key}'
        }
        response = requests.get(url, headers=headers)

        # Check for request success
        if response.status_code == 200:
            return response.json()
        else:
            # Handle errors gracefully
            print("Error:", response.text)
            return None

# Example usage
secret_key = "sk_test_daf386e7071c4613e54e4b71f43926409abd811e"
email = "customer@email.com"
amount = "20000"

# Initializing the transaction
paystack_initializer = Pay(email, amount, secret_key)
response = paystack_initializer.initialize_transaction()

if response:
    print(response)
    payment_status = paystack_initializer.payment_status()
    if payment_status:
        print(payment_status)
