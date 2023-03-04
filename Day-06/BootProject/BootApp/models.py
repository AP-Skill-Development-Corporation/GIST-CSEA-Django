from django.db import models

# Create your models here.
class Student(models.Model):
	usname = models.CharField(max_length=120)
	pwd = models.CharField(max_length=120)
	email = models.EmailField(max_length=200)
