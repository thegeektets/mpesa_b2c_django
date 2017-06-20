from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings



class Depreciation (models.Model):
    Class = models.CharField(max_length=5)
    Rate = models.FloatField()

    def __str__(self):
        return self.Class


class Assets (models.Model):
    Name = models.CharField(max_length=25)
    SerialNumber = models.CharField(max_length=15)
    Price = models.FloatField()
    DOA = models.DateField()
    Assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    DepClass = models.ForeignKey(Depreciation, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)