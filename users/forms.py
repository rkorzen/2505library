from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField()
    email = forms.EmailField()

    def clean_email(self):
        if self.cleaned_data["email"] != "rkorzen@wp.pl":
            raise forms.ValidationError("Wrong email")