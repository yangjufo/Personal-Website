from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class PostComment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('myblog.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]


@python_2_unicode_compatible
class ProjectComment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('myprojects.Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]