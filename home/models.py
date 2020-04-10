from django.db import models

# Create your models here.
class Post(models.Model):
    topic = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic