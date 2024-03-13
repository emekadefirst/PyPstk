import json
import http.client

class PaystackTransactionInitializer:
    def __init__(self, email, amount, secret_key, ref_id=None, status=None):
        self.email = email
        self.amount = amount
        self.status = status
        self.ref_id = ref_id
        self.secret_key = secret_key

class Pay(PaystackTransactionInitializer):    
    def initialize_transaction(self):
        url = "/transaction/initialize"
        data = {
            "email": self.email,
            "amount": self.amount
        }
        headers = {
            "Authorization": "Bearer " + self.secret_key,
            "Content-Type": "application/json"
        }
        response = self._http_request("POST", url, headers, json.dumps(data))
        
        # Check for request success
        if response.status == 200:
            response_data = json.loads(response.read().decode("utf-8"))  # Read response data
            # Store the generated reference
            self.ref_id = response_data['data']['reference']
            return response_data
        else:
            # Handle errors gracefully
            print("Error:", response.reason)
            return None
            
    def _http_request(self, method, url, headers, body=None):
        connection = http.client.HTTPSConnection("api.paystack.co")
        connection.request(method, url, body, headers)
        return connection.getresponse()