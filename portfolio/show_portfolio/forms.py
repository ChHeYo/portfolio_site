from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('title', 'summary', 'content', 'link', 'post_type', 'thumbnail')
        
        labels = {
            'title': '',
            'content': '',
            'summary': '',
            'post_type': '',
            'link': '',
        }

        widgets = {
            'title' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title',
            }),
            'summary' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'summary',
            }),
            'post_type' : forms.Select(attrs={
                'class': 'form-control',
            }),
            'link' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'link',
            }),
            'content' : forms.Textarea(attrs={
                'class': 'editable medium-editor-textarea postcontent form-control',
                'placeholder': 'content',
            })
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'content')

        widgets = {
            'author' : forms.TextInput(attrs={
                'class': 'textinputclass'
            }),
            'content' : forms.Textarea(attrs={
                'class': 'editable medium-editor-textarea'
            })
        }