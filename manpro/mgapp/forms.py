from django import forms
from .models import *

class productsform(forms.ModelForm):

    class Meta:
        model =product
        fields = '__all__'
        exclude = ['createdat']