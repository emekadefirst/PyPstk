import json
import http.client


class Payment:
    def __init__(self, email, amount, secret_key):
        self.email = email
        self.amount = amount
        self.secret_key = secret_key
            
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
        
        if response.status == 200:
            response_data = json.loads(response.read().decode("utf-8"))
            ref_id = response_data['data']['reference']
            auth_url =  response_data['data']['authorization_url']
            data = {
                "references": ref_id,
                "url": auth_url,
            }
            return data
        else:
            print("Error:", response.reason)
            return None
            
    def _http_request(self, method, url, headers, body=None):
        connection = http.client.HTTPSConnection("api.paystack.co")
        connection.request(method, url, body, headers)
        return connection.getresponse()