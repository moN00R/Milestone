from typing import Any
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser, UserManager
from base_model import BaseModel


class UserManager(UserManager):

    def create_superuser(self, **extra_fields: Any) -> Any:
        extra_fields['username'] = '.'
        extra_fields['roll'] = 0
        return super().create_superuser(**extra_fields)

    def create_user(self, **extra_fields: Any) -> Any:
        extra_fields['username'] = '.'
        return super().create_user(**extra_fields)


class User(AbstractUser, BaseModel):
    objects = UserManager()

    ADMIN = 0
    STUDENT = 1

    CHOICES_ROLL = [
        (ADMIN, 'admin'),
        (STUDENT, 'student')
    ]
    username = models.CharField(
        max_length=1, unique=False, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    phone_number = PhoneNumberField(region='SY',
                                    blank=False, null=False, unique=True)
    password = models.CharField(max_length=255)
    roll = models.IntegerField(
        choices=CHOICES_ROLL, default=1)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
