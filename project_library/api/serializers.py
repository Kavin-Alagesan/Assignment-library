from rest_framework import serializers
from .models import BookModel, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password','is_superuser']
        extra_kwargs= {
            'password' : {'write_only' : True}
        }
    
    def create(self, validated_data):
        user = User.objects.create(
        username = validated_data['username'],
        password = make_password(validated_data['password'])
        )
        return user
    
    def get_username(self, name):
        name = User.objects.filter(username=name)
        if name.exists():
            raise serializers.ValidationError("username is already taken")
        return name

class BookSerializer(serializers.ModelSerializer):   
    class Meta:
        model = BookModel
        fields = ['book_id', 'name', 'author' ,'book_number', 'category']

class BookTakenSerializerNested(serializers.ModelSerializer):
    user_id = UserSerializer()
    
    class Meta:
        model = BookModel
        fields = ['book_id', 'name', 'author' ,'book_number', 'category','user_id']

class BookTakenSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['book_id', 'name', 'author' ,'book_number', 'category','user_id']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attr):
        data=super().validate(attr)
        token=self.get_token(self.user)
        data['user']=str(self.user)
        data['id']=self.user.id
        userprofobj=UserProfile.objects.get(user=self.user)
        data['role']=userprofobj.role
        return data
