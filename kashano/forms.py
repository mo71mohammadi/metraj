from django import forms
from . import models


class EstateForm(forms.ModelForm):
    class Meta:
        model = models.Estate
        fields = '__all__'
