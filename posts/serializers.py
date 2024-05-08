from rest_framework import serializers
from .models import Post, Comment, Reply
from accounts.models import User

class PostSerializer(serializers.ModelSerializer):
    post_likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    post_upvotes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = Post
        fields = ['id', 'type', 'title', 'content', 'link', 'post_likes', 'post_upvotes', 'author']

class CommentSerializer(serializers.ModelSerializer):
    comments_likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments_upvotes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'author', 'comments_likes', 'comments_upvotes', 'created_at']

class ReplySerializer(serializers.ModelSerializer):
    reply_likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    reply_upvotes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Reply
        fields = ['id', 'comment', 'content', 'author', 'reply_likes', 'reply_upvotes', 'created_at']
