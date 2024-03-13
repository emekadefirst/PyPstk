from payment import Pay
from webhook import Hook

key = "sk_test_6215942a0765956d18f05e4f52a12a6a8902cee2"
email = "customer@email.com"
amount = "20000"

# Initialize transaction
new = Pay(email, amount, key)
transaction_data = new.initialize_transaction()
print(transaction_data)
reference = transaction_data['data']['reference']  # Correctly accessing reference from the returned dictionary

# Get transaction status
status = Hook(reference, key)
print(status.status())
