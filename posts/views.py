from rest_framework.response import Response
from accounts.serializers import UserCreateSerializer, UserUpdateSerializer
from accounts.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# Create your views here.

class CreateView(APIView):
    pass