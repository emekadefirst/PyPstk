import json
import requests

class Subscription:
    def __init__(self, name, interval, amount, secret_key):
        self.name = name
        self.interval = interval
        self.amount = amount
        self.secret_key = secret_key
        
    def initialize_payment(self):
        url = "https://api.paystack.co/plan"
        
        headers = {
            "Authorization": "Bearer " + self.secret_key,
            "Content-Type": "application/json"
        }
        
        data = {
            "name": self.name,
            "interval": self.interval,
            "amount": self.amount
        }
        
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            self.ref_id = response.json()['data']['plan_code']
            print("Payment initialization successful. Reference ID:", self.ref_id)
        else:
            print("Payment initialization failed:", response.text)
            
    def payment_status(self):
        if not self.ref_id:
            print("Error: Reference ID not found. Payment not initialized.")
            return None
        
        url = f'https://api.paystack.co/plan/{self.ref_id}'
        headers = {
            'Authorization': f'Bearer {self.secret_key}'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print("Payment status:", response.json())
        else:
            print("Error:", response.text)


# Sample usage
pay = Subscription("Monthly Retainer", "monthly", 500000, "sk_test_daf386e7071c4613e54e4b71f43926409abd811e")
pay.initialize_payment()
pay.payment_status()
