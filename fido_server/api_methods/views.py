from django.shortcuts import render
from api_methods.send_sms import send_otp_sms
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def get_otp(request):
    if request.method == "POST":
        phone_number = request.data.get("phone_number", "0")
        if len(phone_number) != 10 or not phone_number or not phone_number.startswith("0"):
            return Response(
            {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Pass a valid phone_number",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
            
        
        send_otp_sms(phone_number)            
        
        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "An OTP has been sent to your phone_number: %s" % phone_number,
            },
            status=status.HTTP_200_OK,
        )
