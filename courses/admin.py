from django.contrib import admin
from .models import *
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    model = Course
    search_fields = ['name', 'category']

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Subscription)

