from .AccountView import RegistrationAPI, LoginAPI, LogoutView
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    # url(r'^login/', UserListAPIView.as_view(), name = 'Login'),
    url(r'^register/$', RegistrationAPI.as_view(), name = 'Register-View'),
    url(r'^login/$', LoginAPI.as_view(), name = 'Login-View'),
    url(r'^logout/$', LogoutView.as_view(), name='Logout-View'),

]