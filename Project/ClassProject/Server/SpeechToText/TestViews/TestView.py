from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView
from SpeechToText.permissions import PublicEndpoint
from rest_framework.reverse import reverse as api_reverse
#from SpeechToText.models import User
# Create your views here.
class TestNotAuthenticatedAPIView(APIView):
    permission_classes = [PublicEndpoint]

    def get(self, request):

        return Response("TestNotAuthenticatedAPIView: " + api_reverse("account-api:Register-View"))

    

    def post(self, request, format = None):
        return Response("TestNotAuthenticatedAPIView Post")

class TestAuthenticatedAPIView(APIView):
    
    def get(self, request):
        return Response("TestAuthenticatedAPIView Get")

    def post(self, request, format = None):
        return Response("TestAuthenticatedAPIView Post")
