from api_methods.models import Client
import sms

SUPPORT_CENTER = +233303898989


def request_user_callback(phone):

    

    message = "You will soon get a call from customer support on: +%s" % SUPPORT_CENTER
    
    # try:
    #     client = Client.objects.get(phone_number=phone)
    # except Client.DoesNotExist:
    #     raise UserDataNotFound
        
    with sms.get_connection() as connection:
        sms.Message(
            message,
            "+23444444888",
            [phone],
            connection=connection,
        ).send()
