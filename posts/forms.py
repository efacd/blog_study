from django import forms
from posts.models import Post, Tag

class PostForm(forms.ModelForm):
    class Meta:
        # 정해진 양식
        model = Post
        fields = ['author', 'contents']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['author', 'contents']