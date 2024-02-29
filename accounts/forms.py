from django import forms
from accounts.models import User,UserProfile

class Userform (forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['first_name','last_name','email','phone_number','password']