from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField('date published')

    def __str__(self):
        return self.topic