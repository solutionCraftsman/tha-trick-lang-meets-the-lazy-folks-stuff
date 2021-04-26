from django.db import models
from accounts.models import Owner

# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='post_owner')
    image = models.ImageField(upload_to='gallery/')
    description = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.owner.username


class Comment(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='comment_owner')
    content = models.CharField(max_length=120)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.owner.username
