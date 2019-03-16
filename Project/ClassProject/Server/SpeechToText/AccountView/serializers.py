from rest_framework.serializers import  ModelSerializer, SerializerMethodField, ValidationError, Serializer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password", "email")

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class UserUpdateProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')




class CreateUserSerializer(ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        #print(self.data)
        user = User.objects.create_user(validated_data['username'],
                                        validated_data['email'],
                                        validated_data['password'])
        user.first_name = self.data['first_name']
        user.last_name = self.data['last_name']
        user.save()
        return user


class LoginUserSerializer(Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")




    