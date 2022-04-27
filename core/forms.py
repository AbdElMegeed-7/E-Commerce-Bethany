from django import forms
from .models import *


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-group'}),
            'category': forms.Select(attrs={'class': 'form-group'}),
            'desc': forms.Textarea(attrs={'class': 'form-group'}),
            'price': forms.NumberInput(attrs={'class': 'form-group'}),
            'product_available_count': forms.NumberInput(attrs={'class': 'form-group'}),
            'img': forms.FileInput(attrs={'class': 'form-group'}),
        }
