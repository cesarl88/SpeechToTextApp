from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_406_NOT_ACCEPTABLE
from rest_framework.response import Response
from rest_framework.views import APIView
#from SpeechToText.serializers import UserSerializer
#from SpeechToText.models import User
from SpeechToText.permissions import PublicEndpoint
from knox.models import AuthToken
from .serializers import UserRegisterSerializer, CreateUserSerializer, UserSerializer, LoginUserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
# Create your views here.

from rest_framework import serializers
from django.contrib.auth.models import User
#from rest_framework.authtoken.models import Token

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
        #django_logout(request)
        return Response(status=204)