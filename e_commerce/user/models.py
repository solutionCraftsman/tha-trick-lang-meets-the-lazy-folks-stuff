from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Merchant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    store_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    rating = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )

    def __str__(self):
        return self.name


class Buyer:
    name = models.CharField()
    phone_number = models.CharField()

    def __str__(self):
        return self.name
