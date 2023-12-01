from .models import CustomUser, Code
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "phone_number", "password1"]
                
class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ["code"]   