from django import forms
from .models import Comment, Post


class PostAddform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'body',
                  'publish', 'status', 'tags')

        widgets = {
            'title': forms.TextInput(),
            'slug': forms.TextInput(),
            # 'author': forms.Select(),
            'author': forms.TextInput(attrs={'value': '', 'id': 'author', 'type': 'hidden'}),
            'body': forms.Textarea(),
            'publish': forms.DateTimeInput(),
            'status': forms.Select(),
            'tags': forms.TextInput(),
        }


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    query = forms.CharField()
