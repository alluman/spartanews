from django.db import models
from accounts.models import User

class Post(models.Model):
    TYPE_CHOICES = [('news', 'News'), ('show', 'Show'), ('ask', 'Ask')]
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255)
    content = models.TextField()
    link = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)