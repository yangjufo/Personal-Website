from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/P<int:pk>', views.detail, name='detail')
]