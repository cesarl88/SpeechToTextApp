from rest_framework.serializers import  ModelSerializer, SerializerMethodField, ValidationError, Serializer
from rest_framework import serializers
from django.contrib.auth.models import User
from SpeechToText.models import File
from django.contrib.auth import authenticate

class FileSerializer(ModelSerializer):
    # username = serializers.CharField()
    # password = serializers.CharField()
    class Meta:
        model = File
        fields = ('id', 'Name', 'Transcript', 'UploadedDate', 'Content', 'Type', 'User', 'Comment', 'TypeName')
        read_only_fields = ('User',)
        #extra_kwargs = {'password': {'write_only': True}}



# class LoginUserSerializer(Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Unable to log in with provided credentials.")

class FileUpdateSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ('Name', 'Comment',)




    