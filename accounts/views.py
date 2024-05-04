from rest_framework.response import Response
from accounts.serializers import UserCreateSerializer, UserUpdateSerializer
from accounts.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class CreateView(APIView):

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if email and User.objects.filter(email=email).exists():
                return Response({'message': '중복된 email입니다.'}, status=status.HTTP_400_BAD_REQUEST)  
            user = serializer.save()
            password = serializer.validated_data['password']
            user.set_password(password)
            user.save()
            return Response({"message": "저장되었습니다", "userId": user.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)
        
    def put(self, request, username):

        if request.user.username != username:
            return Response({'message': '권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
        user = get_object_or_404(User, username=username)
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            if username!=user.username and User.objects.filter(username=username).exists():
                return Response({'message': '중복된 username'}, status=status.HTTP_400_BAD_REQUEST)
            email = serializer.validated_data.get('email')
            if email!=user.email and User.objects.filter(email=email).exists():
                return Response({'message': '중복된 email'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'message': '저장되었습니다', "userId": user.id}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=400)
        
