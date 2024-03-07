from django.contrib import admin
from .models import *
# Register your models here.


class UserInline(admin.ModelAdmin):
    search_fields = ['phone_number', 'first_name']
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserInline)
