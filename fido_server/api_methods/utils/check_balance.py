from api_methods.exceptions.errors import UserDataNotFound
from api_methods.models import Client
import random

def check_user_balance(phone_number, otp_id):
    
    #  generate random account balance
    first = random.choice(range(1, 10))
    leftover = set(range(10)) - {first}
    rest = random.sample(leftover, 5)
    digits = [first] + rest
    two_digits = "".join(map(str, digits))
    balance = round(int(two_digits) / 100, 2)

    
    try:
        Client.objects.get(phone_number=phone_number, otp=otp_id)
    except Client.DoesNotExist:
        raise UserDataNotFound
    
    return balance
    