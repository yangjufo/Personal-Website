from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('comments/post/P<int:post_pk>', views.post_comment, name='post_comment'),
    path('comments/project/P<int:project_pk>', views.project_comment, name='project_comment')
]