import random
import string

def generate_email():
    return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@test.com"