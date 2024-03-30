from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(User_info)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'name',
        'phonenumber',
    )
