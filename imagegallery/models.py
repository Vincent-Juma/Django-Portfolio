from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class imggal(models.Model):
    imgtitle = models.CharField(max_length=100)
    imgdesc = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title  