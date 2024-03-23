from typing import Any
from base_model import BaseModel
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class UserManger(UserManager):
    def create_superuser(self, **extra_fields: Any) -> Any:
        return super().create_superuser(**extra_fields)

    def create_user(self, **extra_fields: Any) -> Any:
        return super().create_user(**extra_fields)


class User_info(AbstractUser, BaseModel):
    objects = UserManger()
    username = models.CharField(max_length=70, unique=True)
    name = models.CharField(max_length=100)

    phonenumber = models.CharField(max_length=13)
    password = models.CharField(max_length=100)

    # USERNAME_FIELD = 'ERP_Student_Id'


class UserData(models.Model):
    assessment_result_id = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    program_group = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    student_group_date = models.DateField
