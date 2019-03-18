from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_406_NOT_ACCEPTABLE
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView, RetrieveAPIView
#from SpeechToText.serializers import UserSerializer
#from SpeechToText.models import User
from SpeechToText.permissions import PublicEndpoint
from knox.models import AuthToken
from .serializers import UserRegisterSerializer, CreateUserSerializer, UserSerializer, LoginUserSerializer, UserUpdateProfileSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password
#from django.contrib.auth.forms import UserCreationForm
#from django.urls import reverse_lazy
#from django.views import generic
# Create your views here.

from rest_framework import serializers
from django.contrib.auth.models import User
#from rest_framework.authtoken.models import Token

class UserUpdatePassword(APIView):
    serializer_class = UserSerializer
    def post(self, request):
        
        currentPassword = self.request.data['Password']

        user = get_object_or_404(User, username = self.request.user.username)
        #print(currentPassword)
        if(not check_password(currentPassword, user.password)):
            return Response(status=403, data= { "error": "Incorrect Password"})

        newPassword = self.request.data['newPassword']
        confirmPassword = self.request.data['confirmPassword']


        if(newPassword != confirmPassword):
            return Response(status=406, data= { "error": "Passwords don't match"})

        user.set_password(newPassword)
        user.save()

        return Response(status = 202, data = {
            "user": UserSerializer(user).data,
        })

class UserUpdateProfile(UpdateAPIView):
    serializer_class = UserUpdateProfileSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
    # def post(self, request):
    #     user =  User.objects.filter(id = self.request.user.id)
    #     return Response({
    #         "user": user
    #     })


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [PublicEndpoint]

    def post(self, request, *args, **kwargs):
        #print("Here")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        #token = Token.objects.create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    permission_classes = [PublicEndpoint]

    def post(self, request, *args, **kwargs):
        print("Here")
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        print(user)
        #token = Token.objects.create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })

class LogoutView(APIView):
    #authentication_classes = (TokenAuthentication, )
    def post(self, request):
        tokens = AuthToken.objects.filter(user = self.request.user)

        for t in tokens:
            t.delete()
        return Response(status=204)


#class Reset(generic.CreateView):
 #   form_class = UserCreationForm
 #   success_url = reverse_lazy('login')
 #   template_name = 'home.html'
