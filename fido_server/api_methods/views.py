from api_methods.exceptions.errors import WrongPhoneNumber
from api_methods.utils.send_sms import send_otp_sms
from api_methods.utils.check_balance import check_user_balance
from api_methods.utils.request_callback import request_user_callback, SUPPORT_CENTER
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def get_otp(request):
    if request.method == "POST":
        phone_number = request.data.get("phone_number", "0")
        if (
            len(phone_number) != 10
            or not phone_number
            or not phone_number.startswith("0")
        ):
            raise WrongPhoneNumber

        send_otp_sms(phone_number)

        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "An OTP has been sent to your phone_number: %s"
                % phone_number,
            },
            status=status.HTTP_200_OK,
        )


@api_view(["POST"])
def check_balance(request):
    if request.method == "POST":
        phone_number = request.data.get("phone_number", "0")
        otp_id = request.data.get("otp_id", "0")
        if (
            len(phone_number) != 10
            or not phone_number
            or not phone_number.startswith("0")
        ):
            raise WrongPhoneNumber

        balance = check_user_balance(phone_number, otp_id)

        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "Your available balace is: %s"
                % balance,
            },
            status=status.HTTP_200_OK,
        )
        
@api_view(["POST"])
def request_callback(request):
    if request.method == "POST":
        phone_number = request.data.get("phone_number", "0")
        if (
            len(phone_number) != 10
            or not phone_number
            or not phone_number.startswith("0")
        ):
            raise WrongPhoneNumber

        request_user_callback(phone_number)
        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "You will soon get a call from customer support on: +%s"
                % SUPPORT_CENTER,
            },
            status=status.HTTP_200_OK,
        )

