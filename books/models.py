from django.db import models
from base_model import BaseModel
from django.core.validators import FileExtensionValidator

class Library(BaseModel):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='link/', validators=[FileExtensionValidator(['mp3', 'mp4', 'pdf'])])
    publish = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.publish}'
