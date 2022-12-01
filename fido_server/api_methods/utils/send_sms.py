#!/usr/bin/env python
import os
from urllib.request import urlopen
from urllib.parse import urlencode
import json
from api_methods.exceptions.errors import ProcessNotFinished
from api_methods.models import Client
import sms
import random


# def send_sms(phone,message):
#     api_key = os.getenv('API_KEY')
#     print("api_key", api_key)
#     sender_id = os.getenv('SENDER_ID')
#     #parameters to send SMS
#     params = {
#         "api_key": api_key,
#     }
#     # params = {\"apikey\":api_key,\"destination\":phone,\"message\":message,\"source\":sender_id,\"dlr\":0,\"type\":0,\"time\":date_time}

#     #prepare your url
#     url = 'https://sms.textcus.com/api/send?'+ urlencode(params)

#     content = urlopen(url).read()
#     print(json.loads(content))
#     #content contains the response from TextCus
#     return json.loads(content)

# # #Defining variables to be used inside function
# # api_key = '9OqfypgGXyAUx7422qylPLGrJxz17Nsmq' #Remember to put your account API Key here
# # phone = '23324XXXXXXX' #International format (233) excluding the (+)
# # message = 'This is just a test on TextCus!'
# # sender_id = 'TextCus' #11 Characters maximum
# # date_time = "2017-05-02 00:59:00"


def send_otp_sms(phone):

    first = random.choice(range(1, 10))
    leftover = set(range(10)) - {first}
    rest = random.sample(leftover, 3)
    digits = [first] + rest
    four_digits = "".join(map(str, digits))

    message = "Your OTP for the serivce is: " + four_digits
    
    try:
        client = Client.objects.get(phone_number=phone)
        client.otp = four_digits
        client.save()
    except Client.DoesNotExist:
        Client.objects.create(phone_number=phone, otp=four_digits)
        
    with sms.get_connection() as connection:
        sms.Message(
            message,
            "+23444444888",
            [phone],
            connection=connection,
        ).send()
