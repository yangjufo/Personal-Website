"""mysite URL Configuration

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
    2. Add a URL to urlpatterns:  path('myblog/', include('myblog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myblog.feeds import AllPostRssFeed
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all/rss/', AllPostRssFeed(), name='rss'),
    path('search/', include('haystack.urls')),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('projects/', include("myprojects.urls")),
    path('blog/', include('myblog.urls')),
    path('', include('mycomments.urls')),        
    path('android_browser/', views.android_browser),
]
