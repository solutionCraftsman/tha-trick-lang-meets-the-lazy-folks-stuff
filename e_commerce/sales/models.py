from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from user.models import Merchant


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.TextField()
    category = models.CharField(
        max_length=50,
        choices=(
            ('Technology', 'Technology'),
            ('Fashion', 'Fashion'),
            ('Kids', 'Kids'),
            ('Ladies', 'Ladies'),
            ('Men', 'Men'),
            ('Interiors', 'Interiors'),
        )
    )
    price = models.DecimalField(decimal_places=2, max_digits=10)
    rating = models.IntegerField(
        validators =[MaxValueValidator(100), MinValueValidator(1)]
    )
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
