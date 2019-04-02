from .TestView import TestNotAuthenticatedAPIView, TestAuthenticatedAPIView
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    #url(r'^login/', UserListAPIView.as_view(), name = 'Login'),
    url(r'^AuthenticatedTest/$', TestAuthenticatedAPIView.as_view(), name = 'Test-Auth-View'),
    url(r'^NotAuthenticatedTest/$', TestNotAuthenticatedAPIView.as_view(), name = 'Test-Not-Auth-View')

]