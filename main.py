import requests
import json

YOUR_SECRET_KEY = 'enter your secret key here'

class Paystack:
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

paystack = Paystack(email="customer@email.com", first_name="Zero", last_name="Sum", phone="+2348123456789", secretkey=YOUR_SECRET_KEY)
response = paystack.create_customer()
print(response)
