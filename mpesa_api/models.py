import uuid
import jsonfield

from django.db import models

# Create your models here.

class MpesaLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transactionid = models.CharField(max_length=100, blank=True, null=True)
    resulttype = models.CharField(max_length=100, blank=True, null=True)
    resultcode = models.CharField(max_length=100, blank=True, null=True)
    resultdesc = models.TextField(blank=True, null=True)
    originatorconversationid = models.CharField(max_length=100, blank=True, null=True)
    conversationid = models.CharField(max_length=100, blank=True, null=True)
    referencedata = jsonfield.JSONField()


