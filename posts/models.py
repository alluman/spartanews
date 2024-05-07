from django.db import models
from accounts.models import User

class Post(models.Model):
    TYPE_CHOICES = [('news', 'News'), ('show', 'Show'), ('ask', 'Ask')]
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255)
    content = models.TextField()
    link = models.URLField()
    post_like = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    post_upvote = models.ManyToManyField(User, related_name='upvoted_posts', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comments_like = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    comments_upvote = models.ManyToManyField(User, related_name='upvoted_posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_like = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    reply_upvote = models.ManyToManyField(User, related_name='upvoted_posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)