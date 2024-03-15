from typing import Any
from base_model import BaseModel
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# class UserManger(UserManager):
#     def create_superuser(self, **extra_fields: Any) -> Any:
#         extra_fields['username'] = '.'
#         return super().create_superuser(**extra_fields)

#     def create_user(self, **extra_fields: Any) -> Any:
#         extra_fields['username'] = '.'
#         return super().create_user(**extra_fields)


class User_info(AbstractUser, BaseModel):
    # objects = UserManger()
    username = models.CharField(max_length=70, unique=True)
    name = models.CharField(max_length=100)
    # ERP_Student_Id = models.CharField(max_length=70, unique=True)
    phonenumber = models.CharField(max_length=13)
    password = models.CharField(max_length=100)

    # USERNAME_FIELD = 'ERP_Student_Id'
