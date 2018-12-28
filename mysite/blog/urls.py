from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/P<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('archives/<int:year>/<int:month>', views.ArchivesView.as_view(), name='archives'),
    path('category/C<int:pk>', views.CategoryView.as_view(), name='category'),
    path('tag/T<int:pk>', views.TagView.as_view(), name='tag'),    
]