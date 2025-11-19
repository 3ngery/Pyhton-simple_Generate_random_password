import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
