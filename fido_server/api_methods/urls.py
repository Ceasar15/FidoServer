from django.urls import path

from .views import send_fullname


urlpatterns = [
    path('api/v1', send_fullname )
]
