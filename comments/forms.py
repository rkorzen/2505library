from django import forms

from comments.models import CommentPost


class CommentForm(forms.Form):
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)


class CommentForm2(forms.ModelForm):

    class Meta:
        model = CommentPost
        exclude = ["post"]