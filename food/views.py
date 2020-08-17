from django.shortcuts import render
from .serializers import UserListSerializer, UserCreateSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status


# Create your views here.

class UserListView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserListSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = UserCreateSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        return Response(user.error, status=status.HTTP_400_BAD_REQUEST)