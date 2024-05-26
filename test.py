from pypstk.payment import Payment

email = "customer@email.com"
amount = "20000"
secret_key = "your secret_key from Paystack"

new_payment = Payment(email, amount, secret_key)
transaction_data = new_payment.initialize_transaction()
print(transaction_data)