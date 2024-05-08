from rest_framework.response import Response
from posts.serializers import PostSerializer, CommentSerializer, ReplySerializer
from posts.models import Post, Comment, Reply
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from accounts.models import User
from rest_framework import generics
from .serializers import CommentSerializer, ReplySerializer


class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostCreate(APIView):
    def post(self, request):
        data = request.data
        data['author'] = request.user.id
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            product = serializer.save(author=request.user)
            return Response({"message": "등록완료", "productId": product.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def patch(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "수정완료"}, serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response({"message": "삭제완료"}, status=status.HTTP_204_NO_CONTENT)


class CommentCreate(APIView):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        data = request.data
        data['post'] = post.pk
        data['author'] = request.user.id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentUpdate(APIView):
    def get(self, request, post_id, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id, post__id=post_id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def patch(self, request, post_id, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id, post__id=post_id)
        serializer = CommentSerializer(
            comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id, post__id=post_id)
        comment.delete()
        return Response({"message": "삭제완료"}, status=status.HTTP_204_NO_CONTENT)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentsList(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = Comment.objects.filter(
            post=post).order_by('created_at').values()
        replies = Reply.objects.filter(
            comment__post=post).order_by('created_at').values()
        post_list = list(comments) + list(replies)
        post_list.sort(key=lambda x: x['created_at'], reverse=True)
        return Response(post_list)


# 메뉴의 [쓰레드] 누르면 작성한 comments, reply 모두 최신순으로 나열


class UserCommentsListView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        comments = Comment.objects.filter(
            author=user).order_by('created_at').values()
        replies = Reply.objects.filter(
            author=user).order_by('created_at').values()
        post_list = list(comments) + list(replies)
        post_list.sort(key=lambda x: x['created_at'], reverse=True)
        return Response(post_list)


class ReplyCreateAPIView(APIView):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(comment=comment, author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReplyListAPIView(APIView):
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        replies = comment.reply_comments.all()
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)
