from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    price = models.FloatField(default=0)


def __str__(self):
    return self.title


