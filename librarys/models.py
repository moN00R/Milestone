from django.db import models
from courses.models import Course
from base_model import BaseModel
# Create your models here.


class Library(BaseModel):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    cousrse = models.ForeignKey(
        Course, on_delete=models.DO_NOTHING, related_name='course_library')
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.name
