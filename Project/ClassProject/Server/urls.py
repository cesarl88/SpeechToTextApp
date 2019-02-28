"""ClassProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from SpeechToText.views import UserListAPIView
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    #url(r'^login/', UserListAPIView.as_view(), name = 'Login'),
    url(r'^login/(?P<id>\d+)/', UserListAPIView.as_view(), name = 'Login-ID'),
    url(r'^test/', include('SpeechToText.TestViews.urls')),

]
