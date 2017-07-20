from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
import uuid  # The uuid module



class User (AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(unique=True , max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    

class Depreciation (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dclass = models.CharField(max_length=5)
    rate = models.FloatField()

    def __str__(self):
        return self.Class


class Assets (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=25)
    serialnumber = models.CharField(max_length=15)
    price = models.FloatField()
    doa = models.DateField()
    assignee = models.ForeignKey(User)
    depreciation = models.ForeignKey(Depreciation)

    def __str__(self):
        return self.Class


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)