import uuid
import jsonfield

from django.db import models

# Create your models here.

class MpesaLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    request = jsonfield.JSONField()