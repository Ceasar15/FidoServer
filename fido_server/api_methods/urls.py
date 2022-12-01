from django.urls import path

from api_methods.views import get_otp, check_balance, request_callback


urlpatterns = [
    path('menu/get_otp', get_otp, name="get_otp"), 
    path('menu/check_balance', check_balance, name="check_balance"),
    path('menu/request_callback', request_callback, name="request_callback")
]
