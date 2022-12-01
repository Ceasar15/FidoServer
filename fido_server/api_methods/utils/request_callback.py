from api_methods.models import Client
import json
import sms
from datetime import datetime

SUPPORT_CENTER = +233303898989


def request_user_callback(phone):

    message = "You will soon get a call from customer support on: +%s" % SUPPORT_CENTER
    
    # #  update records for requested callbacks
    # with open('request_callback.json', 'r+', encoding='utf-8') as file:
    #     file_data = json.load(file)
    #     file_data["request_callback"].append(new_data)
    #     file.seek(0)
    #     json.dump(file_data, file, ensure_ascii=False, indent=4)
    
    #  send an sms to confirm
    with sms.get_connection() as connection:
        sms.Message(
            message,
            "+23444444888",
            [phone],
            connection=connection,
        ).send()
    return True
