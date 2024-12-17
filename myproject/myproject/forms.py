from django import forms
from .models import Product, Import, Export, Inventory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ImportForm(forms.ModelForm):
    class Meta:
        model = Import
        fields = '__all__'
        widgets = {
            'product_code': forms.Select(attrs={'class': 'form-control'}),
        }

class ExportForm(forms.ModelForm):
    class Meta:
        model = Export
        fields = '__all__'
        widgets = {
            'product_code': forms.Select(attrs={'class': 'form-control'}),
        }

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
        widgets = {
            'product_code': forms.Select(attrs={'class': 'form-control'}),
        }
