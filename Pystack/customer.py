import requests
import json

YOUR_SECRET_KEY = 'sk_test_2b514ab5752a617278f1460e22924c782e8f4999'

class Customer:
    def __init__(self, email, first_name, last_name, phone, secretkey):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.secretkey = secretkey
        
    def create_customer(self):
        url = "https://api.paystack.co/customer"
        headers = {
            "Authorization": "Bearer " + self.secretkey,
            "Content-Type": "application/json"
        }
        data = {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()


