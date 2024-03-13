import base64
import pyotp

otp_uri = "otpauth://totp/PyPI:Emekadefirst?digits=6&secret=KN3DGJUB4M3TFWJGPLGEHU76AURE6PIU&algorithm=SHA1&issuer=PyPI&period=30"

# Extract secret key from URI
secret_key_base32 = otp_uri.split("secret=")[1].split("&")[0]

# Decode Base32 secret key
secret_key_bytes = base64.b32decode(secret_key_base32.upper())

# Create TOTP object
totp = pyotp.TOTP(secret_key_bytes)

# Generate 6-digit code
six_digit_code = totp.now()

print("6-digit code:", six_digit_code)
