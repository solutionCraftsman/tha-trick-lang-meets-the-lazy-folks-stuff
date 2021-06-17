from django.db import models
from account.models import Owner


# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='post_owner')
    description = models.TextField()
    image = models.ImageField(upload_to='image/post')
    date_created = models.DateTimeField(auto_now_add=True)
    number_of_likes = models.IntegerField(default=0)
    number_of_comments = models.IntegerField(default=0)

    def __str__(self):
        return self.description


class Comment(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='comment_owner')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    content = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username


There isn’t anything to compare.
indev is up to date with all commits from ayodele. Try switching the base for your comparison.
