from django import forms
from .models import Product
from django.contrib.auth.models import Group

# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     price = forms.DecimalField(max_digits=8, decimal_places=2)
#     description = forms.CharField(widget=forms.Textarea)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'discount']


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']