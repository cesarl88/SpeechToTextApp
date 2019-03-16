from .AccountView import RegistrationAPI, LoginAPI, LogoutView, UserUpdatePassword, UserUpdateProfile
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    # url(r'^login/', UserListAPIView.as_view(), name = 'Login'),
    url(r'^register/$', RegistrationAPI.as_view(), name = 'Register-View'),
    url(r'^login/$', LoginAPI.as_view(), name = 'Login-View'),
    url(r'^logout/$', LogoutView.as_view(), name='Logout-View'),
    url(r'^update-password/$', UserUpdatePassword.as_view(), name='Logout-View'),
    url(r'^update-profile/(?P<id>\d+)/$', UserUpdateProfile.as_view(), name='Update-Profile-View'),
    #url('^', include('django.contrib.auth.urls')),

]