import re
import hashlib
import secrets

def validate_email(email):
    # Regular expression pattern for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def generate_password_hash(password):
    # Generate a salt for password hashing
    salt = secrets.token_hex(8)
    # Combine the password and salt and hash them using SHA-256
    hashed_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    # Return the hashed password and salt
    return hashed_password, salt

def verify_password(plain_password, hashed_password, salt):
    # Hash the plain password with the provided salt
    hashed_plain_password = hashlib.sha256((plain_password + salt).encode('utf-8')).hexdigest()
    # Compare the hashed plain password with the stored hashed password
    return hashed_plain_password == hashed_password
