from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User 
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated



# Create your views here.
# User and book create and view APIs
class UserCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookCreate(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

# User and book update and delete APIs
class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookUpdateDelete(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

# User login and logout
class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# view, borrow, and return available Books
# class BorrowBooks


class Logout(generics.RetrieveUpdateDestroyAPIView):
    pass

