from django.contrib import admin
from .models import CourseType, Course

@admin.register(CourseType)
class CourseType(admin.ModelAdmin):
    list_display = (
        'id', 
        'name',
    )
    
@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = (
        'id', 
        'name',
        'category',
        'days',
        'hours',
    )