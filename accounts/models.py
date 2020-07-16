from django.db import models


class upload(models.Model):
    username = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2  = models.CharField(max_length=100)
    email = models.EmailField(max_length=None)
    verification1 = models.CharField()


    