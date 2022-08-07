from django import forms

from posts.models import Post


class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)


class PostForm2(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", 'content',]