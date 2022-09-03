from django import forms
from .models import Comment, Post


class EmailPostForm(forms.Form):
    """Форма модели Email"""
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    """Форма модели Comments"""
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class PostForm(forms.ModelForm):
    """Форма нового Post"""
    class Meta:
        model = Post
        fields = ('title', 'body')
        labels = {'title': ''}
