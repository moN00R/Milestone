from uuid import uuid4
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User_info(models.Model):
    ERP_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(
        region='SY', blank=False, null=False, unique=True)
    password = models.CharField(max_length=50)
