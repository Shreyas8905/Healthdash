from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model


class usercred(models.Model):
    user = models.ForeignKey(User, default=False, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=40,default=1)
    phone = models.CharField(max_length=20,default=1)
    guardian = models.CharField(max_length=40,default=1)
    guardphn = models.CharField(max_length=20,default=1)
    health = models.CharField(max_length=40,default=1)
    bloodgroup = models.CharField(max_length=40,default=1)
    insurance = models.CharField(max_length=40,default=1)
    def __str__(self):
        return self.user.username

class hospital(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.DecimalField(decimal_places=10,max_digits=10)
    longitude = models.DecimalField(decimal_places=10,max_digits=10)