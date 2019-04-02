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

#from SpeechToText.views import UserListAPIView
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    #url(r'^api/', include(endpoints)),
    #url(r'^api/auth/', include('knox.urls')),
    url(r'^test/', include('SpeechToText.TestViews.urls')),
    url(r'^account/', include(('SpeechToText.AccountView.urls','app-name'), namespace ='account-api')),
    url(r'^account-files/', include(('SpeechToText.FileView.urls','app-name'), namespace ='account-file-api')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
