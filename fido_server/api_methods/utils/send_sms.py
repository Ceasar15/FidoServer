#!/usr/bin/env python
import os
from api_methods.exceptions.errors import ProcessNotFinished
from api_methods.models import Client
import sms
import random
import requests
from sms.backends.base import BaseSmsBackend


api_key = os.getenv("API_KEY")
sender_id = os.getenv("SENDER_ID")

class CustomSmsBackend(BaseSmsBackend):
    def __init__(self, fail_silently: bool = False,*args, **kwargs) -> None:
        self.fail_silently = fail_silently
        super().__init__(*args, **kwargs)
        
    def send_messages(self, messages) -> int:
        # parameters to send SMS
        destination = messages[0].recipients
        final_destination = ["+233" + str(i[1:]) for i in destination]
        
        params = {
            "apikey": api_key,
            "destination": final_destination,
            "message": messages[0].body,
            "source": sender_id,
            "dlr": 1,
            "type": 0,
        }

        response = requests.get('https://sms.textcus.com/api/send?', params=params)
        content =  response.json()["status"]

        try:
            if content != "0000":
                raise ProcessNotFinished
        except Exception:
            raise ProcessNotFinished
        return response.text


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
