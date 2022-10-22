from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, null=False)
    content = models.TextField()
    date_of_creation = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title[:20]