from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Write a post ...'
            }))

    class Meta:
        model = Post
        fields = ['content']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '3',
                    'placeholder': 'Write a comment...'}
        ))

    class Meta:
        model = Comment
        fields = ['comment']