from uuid import uuid4
from django.db import models
from django.conf import settings


UserModel = settings.AUTH_USER_MODEL


class BaseModel(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # is_deleted = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        UserModel, models.DO_NOTHING, null=True, blank=True, related_name="+")
    updated_by = models.ForeignKey(
        UserModel, models.DO_NOTHING, null=True, blank=True, related_name="+")
    deleted_by = models.ForeignKey(
        UserModel, models.DO_NOTHING, null=True, blank=True, related_name="+")
