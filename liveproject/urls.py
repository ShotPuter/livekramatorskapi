"""took URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from adminmy.views import return_version
from rest_framework.authtoken import views
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from userapi import views as userviews

admin.autodiscover()
urlpatterns = [
	#Django  admin
    url(r'^admin/', admin.site.urls),
    url(r'^api/',include('myapi.urls')),
    #url(r'',return_version),
    #url(r'^users/', views.UserList.as_view()),
    #url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    #url(r'accounts/', include('rest_registration.api.urls')), 
    url(r'^userapi/register-user',userviews.register_user),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^userapi/login/', userviews.login_user),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
