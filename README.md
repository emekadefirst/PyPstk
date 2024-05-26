# Pystack

This Python package provides a set of classes to interact with the Paystack API for handling transactions, customers, subscriptions, and webhooks.

## Installation

To use this package, you need to have Python installed. You can install the package using pip:

```
pip install pystack
```

## Usage

### 1. Payment

```python
from payment import Pay

# Initialize payment
email = "customer@email.com"
amount = "20000"
secret_key = "sk_test_6215942a0765956d18f05e4f52a12a6a8902cee2"

new_payment = Pay(email, amount, secret_key)
transaction_data = new_payment.initialize_transaction()
print(transaction_data)

# Sample output:
# {'status': True, 'message': 'Authorization URL created', 'data': {'authorization_url': 'https://checkout.paystack.com/1hxv7un'}}
```


### 3. Subscription

```python
from subscription import Subscription

# Initialize subscription payment
name = "Monthly Retainer"
interval = "monthly"
amount = 500000
secret_key = "sk_test_daf386e7071c4613e54e4b71f43926409abd811e"

pay_subscription = Subscription(name, interval, amount, secret_key)
pay_subscription.initialize_payment()
pay_subscription.payment_status()
```

### 4. Webhook

```python
from webhook import Hook

# Check webhook status
reference = "YOUR_REFERENCE"
secret_key = "YOUR_SECRET_KEY"

hook = Hook(reference, secret_key)
status = hook.status()
print(status)
```

## Contributors

- [Emekadefirst](https://github.com/emekadefirst)
- I used [Olabode](https://github.com/Olabode-cmd) template to test this in an api

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
