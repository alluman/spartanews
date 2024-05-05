from rest_framework.response import Response
from posts.serializers import PostSerializer
from posts.models import Post
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostCreate(APIView):
    def post(self, request):
        data = request.data.copy()
        data['author'] = request.user.id
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            product = serializer.save()            
            return Response({"message": "등록완료", "productId": product.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)