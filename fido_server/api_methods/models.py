import uuid
from django.db import models

# Create your models here.

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=255,  null=True, blank=True)
    otp = models.CharField(max_length=255,  null=True, blank=True)