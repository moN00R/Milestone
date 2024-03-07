from django.db import models
from courses.models import Subscription
from base_model import BaseModel
# Create your models here.


class StudentMark(BaseModel):
    FIRST = "first-quiz"
    SECOUND = "secound-quiz"
    WRIT = "writ-exam"
    ORALL = "orall"

    CHOICES_EXAM_TYPE = [
        (FIRST, "first-quiz"),
        (SECOUND, "secound-quiz"),
        (WRIT, "writ-exam"),
        (ORALL, "orall"),
    ]
    subscription_course = models.ForeignKey(
        Subscription, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=50, choices=CHOICES_EXAM_TYPE)
    mark = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return f'{self.subscription_course} {self.exam_type}'
