from django.urls import path
from . import views

app_name = 'myprojects'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('project/P<int:pk>', views.ProjectDetailView.as_view(), name='detail'),
    path('archives/<int:year>', views.ArchivesView.as_view(), name='archives'),
    path('category/C<int:pk>', views.CategoryView.as_view(), name='category'),
    path('tag/T<int:pk>', views.TagView.as_view(), name='tag'),
]