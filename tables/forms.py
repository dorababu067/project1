from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(
                        attrs = {'class':'form-control','placeholder':'Enter Password Here...'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(
                        attrs = {'class':'form-control','placeholder':'Confirm Password...'}))
    username  = forms.CharField(widget = forms.TextInput(
                        attrs = {'class':'form-control','placeholder':'Username','autofocus':'autofocus'}))
    first_name  = forms.CharField(widget = forms.TextInput(
                        attrs = {'class':'form-control','placeholder':'Firstname'}))
    last_name  = forms.CharField(widget = forms.TextInput(
                        attrs = {'class':'form-control','placeholder':'Lastname'}))
    email  = forms.CharField(widget = forms.TextInput(
                        attrs = {'class':'form-control','placeholder':'example@gmail.com'}))
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch")
        return confirm_password