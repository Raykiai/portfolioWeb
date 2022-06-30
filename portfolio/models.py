from django.db import models

# Create your models here.
class Experience(models.Model):
    position = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start = models.DateField(max_length=200, null=True)
    to = models.DateField(max_length=200, null=True)