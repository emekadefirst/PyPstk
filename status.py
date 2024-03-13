import json
import http.client

class Verify():
    def __init__(self, reference, secret_key):
        self.reference = reference
        self.secret_key = secret_key
        
    def status(self):
        url = f"/transaction/verify/{self.reference}"
        headers = {
            "Authorization": "Bearer " + self.secret_key
        }
        response = self._http_request("GET", url, headers)
        response_text = response.read().decode("utf-8")  # Read response content
        print(response_text)

        if response.status == 200:
            data = json.loads(response_text)
            gateway_response = data.get('data', {}).get('gateway_response')
            if gateway_response == "Successful":
                return "successful"
            elif gateway_response == "The transaction was not completed":
                return "pending"
            else:
                return "failed"
        else:
            return "failed"
    
    def _http_request(self, method, url, headers, body=None):
        connection = http.client.HTTPSConnection("api.paystack.co")
        connection.request(method, url, body, headers)
        return connection.getresponse()
