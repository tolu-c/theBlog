from django import forms
from django.forms import fields
from .models import Comments


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentsForm(forms.Form):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'body')
