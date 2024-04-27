from django.db import models
from base_model import BaseModel 
from phonenumber_field.modelfields import PhoneNumberField




class CourseType(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    


class Course(BaseModel):
    Sunday = 'Sunday'
    Monday = 'Monday'
    Tuesday = 'Tuesday'
    Wednesday = 'Wednesday'
    Thursday = 'Thursday'
    Saturday = 'Saturday'
    Fraiday = 'Fraiday'
    Sunday_Tuesday_Thursday = "Sunday - Tuesday - Thursday"
    Monday_Wednesday_Saturday = "Monday - Wednesday - Saturday"

    CHOICES_DAYS = [
        (Sunday, 'Sunday'),
        (Monday, 'Monday'),
        (Tuesday, 'Tuesday'),
        (Wednesday, 'Wednesday'),
        (Thursday, 'Thursday'),
        (Saturday, 'Saturday'),
        (Fraiday, 'Fraiday'),
        (Sunday_Tuesday_Thursday, "Sunday - Tuesday - Thursday"),
        (Monday_Wednesday_Saturday, "Monday - Wednesday - Saturday")
    ]

    TIME1 = "12:00 - 1:30"
    TIME2 = "1:30 - 3:00"
    TIME3 = "3:00 - 4:30"
    TIME4 = "4:30 - 6:00"
    TIME5 = "6:00 - 7:30"
    TIME6 = "7:30 - 9:00"

    CHOICES_TIME = [
        (TIME1, "12:00 - 1:30"),
        (TIME2, "1:30 - 3:00"),
        (TIME3, "3:00 - 4:30"),
        (TIME4, "4:30 - 6:00"),
        (TIME5, "6:00 - 7:30"),
        (TIME6, "7:30 - 9:00"),
    ]

    name = models.CharField(max_length=100)
    category = models.ForeignKey(CourseType, on_delete=models.PROTECT, related_name='type')
    description = models.TextField()
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='courses/media')
    days = models.CharField(max_length=100, choices=CHOICES_DAYS, default=Sunday_Tuesday_Thursday)
    hours = models.CharField(max_length=100, choices=CHOICES_TIME, default=TIME1)
    limit_booking = models.PositiveIntegerField(default=0, null=True, blank=True, unique=False)
    open_to_booking = models.BooleanField(default=False)
    number_of_student = models.PositiveIntegerField(default=0, null=True, blank=True)


    def __str__(self) -> str:
        return f'{self.name} - {self.days}'
    

class Subscription(BaseModel):
    phonenumber = PhoneNumberField(region='SY')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subscription')

    def __str__(self):
        return f'{self.phonenumber}  in {self.course}'
