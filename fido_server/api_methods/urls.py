from django.urls import path

from api_methods.views import get_otp


urlpatterns = [
    path('menu/get_otp', get_otp, name="get_otp")
]
