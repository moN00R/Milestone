from base_model import BaseModel
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User_info(BaseModel):
    name = models.CharField(max_length=100)
    ERB_Student_Id = models.CharField(max_length=70)
    phonenumber = models.CharField(max_length=13)
    password = models.CharField(max_length=100)
