from django.db import models


# Create your models here.
class MenDem(models.Model):
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    description = models.TextField()
    image = models.FilePathField(path='/img')
