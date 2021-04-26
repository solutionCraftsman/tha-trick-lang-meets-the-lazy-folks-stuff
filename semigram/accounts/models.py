from django.db import models

# Create your models here.


class Owner(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(blank=True, max_length=15)
    profile_picture = models.ImageField(upload_to="gallery/", default="gallery/user.png")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
