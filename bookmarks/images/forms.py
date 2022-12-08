from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        nodel = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }