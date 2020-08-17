from django.shortcuts import render
from .serializers import UserListSerializer
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