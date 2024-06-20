from django import forms
from .models import user

class UserProfile(forms.ModelForm):
    class Meta:
        model = user
        fields = ['username','name','desc','photo']