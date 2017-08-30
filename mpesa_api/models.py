import uuid
import jsonfield

from django.db import models

# Create your models here.

class MpesaLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    result_type = models.CharField(max_length=100)
    result_code = models.CharField(max_length=100)
    result_desc = models.TextField()
    originator_conversation_id = models.CharField(max_length=100)
    conversation_id = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100)
    reference_data = jsonfield.JSONField()


