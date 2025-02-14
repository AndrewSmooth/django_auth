from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import FieldDoesNotExist

import datetime

# Create your models here.
class MyUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=8)

    def update(self, **kwargs):
        for k, val in kwargs.items():
            try:
                field = MyUser._meta.get_field(k)
            except FieldDoesNotExist:
                field = None
            finally:
                if field:
                    if k == "username":
                        self.username = val
                    if k == "email":
                        self.email = val
                self.save()

class RefreshToken(models.Model):
    token = models.CharField(max_length=32, unique=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    iat = models.DateTimeField()
    exp = models.DateTimeField()

    def set_time(self):
        self.iat = datetime.datetime.now()
        self.exp = self.iat + datetime.timedelta(30)