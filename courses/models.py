from django.db import models
from accounts.models import User
from base_model import BaseModel
# Create your models here.


class Category(BaseModel):
    name = models.CharField(max_length=255)

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

    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, null=True, blank=True)
    days_to_start = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    limit_booking = models.PositiveIntegerField(null=False, blank=False)
    active = models.BooleanField(default=True)
    open_to_booking = models.BooleanField(default=False)
    days = models.CharField(
        max_length=50, choices=CHOICES_DAYS, default=Fraiday)
    hours = models.CharField(
        max_length=50, choices=CHOICES_TIME, default=TIME1)
    # user = models.ManyToManyField('self', through='Subscription')
    number_of_student = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Subscription(BaseModel):
    PENDING = 0
    ACCEPTANCE = 1
    REJECT = 2

    CHOICES_STATUS = [
        (PENDING, 'pending'),
        (ACCEPTANCE, 'acceptance'),
        (REJECT, 'reject')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.IntegerField(choices=CHOICES_STATUS, default=PENDING)
    cach = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user}  in {self.course}'
