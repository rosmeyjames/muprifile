from django.db import models

# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=200)
    phno=models.IntegerField()
    address=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    skills=models.CharField(max_length=200)


class portfolio(models.Model):
    qual=models.CharField(max_length=200)
    certification=models.CharField(max_length=200)
    experience=models.CharField(max_length=200)
    project=models.CharField(max_length=200)
    image=models.ImageField()

class project(models.Model):
    project_name=models.CharField(max_length=200)
    project_desc=models.CharField(max_length=200)
    lang=models.CharField(max_length=200)
    project_image=models.ImageField()

