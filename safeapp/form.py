from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from safeapp.models import UserProfile


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

        
class LoginForms(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class UserprofileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=("user",)




