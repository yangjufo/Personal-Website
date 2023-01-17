from django import forms
from .models import PostComment, ProjectComment

BLOCKED_WORDS = ["free"]

class BaseCommentForm(forms.ModelForm):
    def is_valid(self) -> bool:
        if not super().is_valid():
            return False
        for word in BLOCKED_WORDS:
            if word in self.cleaned_data['text']:
                return False
        return True

class PostCommentForm(BaseCommentForm):
    class Meta:
        model = PostComment
        fields = ['name', 'email', 'url', 'text']


class ProjectCommentForm(BaseCommentForm):
    class Meta:
        model = ProjectComment
        fields = ['name', 'email', 'url', 'text']