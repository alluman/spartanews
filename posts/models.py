from django.db import models
from accounts.models import User
from django.utils import timezone


class Post(models.Model):
    TYPE_CHOICES = [('news', 'News'), ('show', 'Show'), ('ask', 'Ask')]
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255)
    content = models.TextField()
    link = models.URLField()
    post_like = models.ManyToManyField(
        User, related_name='liked_posts', blank=True)
    post_upvote = models.ManyToManyField(
        User, related_name='upvoted_posts', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def postlist_points(self):
        after_day = (timezone.now() - self.created_at).days
        after_day_point = -5 * after_day

        comments_count = self.comments.count()
        comments_count_point = 3 * comments_count

        likes_count = self.post_like.count()
        likes_count_point = 1 * likes_count

        return after_day_point + comments_count_point + likes_count_point


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    comments = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comments_likes = models.ManyToManyField(
        User, related_name='liked_comments', blank=True)
    comments_upvotes = models.ManyToManyField(
        User, related_name='upvoted_comments', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    unique_together = ['post', 'author']
    parent_comment = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')


class Reply(models.Model):
    comment = models.ForeignKey(
        Comment, related_name='reply_comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_likes = models.ManyToManyField(
        User, related_name='liked_replies', blank=True)
    reply_upvotes = models.ManyToManyField(
        User, related_name='upvoted_replies', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
