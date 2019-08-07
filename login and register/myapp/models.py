from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.BooleanField(default=True)
    grade = models.IntegerField()


class users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

