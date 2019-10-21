from .models import Image,Profile
from django import forms
#......
class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pub_date', 'likes', 'comments', 'profile.user']

class UpdatebioForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        