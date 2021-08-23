from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):

    class Meta:

        model = Post

        fields = ('title', 'author', 'content', 'created',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
            'created': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
        }

        labels = {
            'title': '',
            'author': '',
            'content': '',
            'created': '',
        }
