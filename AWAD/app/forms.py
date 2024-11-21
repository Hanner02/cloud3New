"""
Definition of forms.
"""

from django import forms
from app.models import LogMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
        

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        

class LogForm(forms.ModelForm):
    class Meta:
        model=LogMessage 
        fields=("title","message","rating")
        


        
        
     