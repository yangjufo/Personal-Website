from django import forms
from .models import PostComment, ProjectComment


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['name', 'email', 'url', 'text']


class ProjectCommentForm(forms.ModelForm):
    class Meta:
        model = ProjectComment
        fields = ['name', 'email', 'url', 'text']