from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):



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