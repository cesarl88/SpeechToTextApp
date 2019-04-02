from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView
#from .serializers import UserSerializer
#from .models import User
# Create your views here.

#class UserListAPIView(APIView):
    
#    def get(self, request,id, name):
 #       print(id)
  #      users = User.objects.all()
  #      print(request)
  #      serializer_class = UserSerializer(users, many=True)
  #      return Response(serializer_class.data)

    

  #  def post(self, request, format = None):
  #      print(request.data)
        #serializer = UserSerializer(data = request.data)
  #      return Response(request.data, HTTP_200_OK)

  
