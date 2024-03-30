from django.db import models
from base_model import BaseModel 

class CourseType(models.Model):
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
    image = models.ImageField(upload_to='courses/media', null=True, blank=True)
    days = models.CharField(max_length=100, choices=CHOICES_DAYS, default=Sunday_Tuesday_Thursday)
    hours = models.CharField(max_length=100, choices=CHOICES_TIME, default=TIME1)

    def __str__(self) -> str:
        return f'{self.name} - {self.days}'
    