from django.contrib import admin
from courses.models import CourseType, Course, Subscription
from import_export.admin import ImportExportModelAdmin


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

@admin.register(Subscription)
class BookingCourse(ImportExportModelAdmin):
    list_display = (
        'id',
        'phonenumber',
        'course',
    )