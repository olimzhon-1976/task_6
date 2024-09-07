from django import forms
from .models import Customer, Seller, Sale, Product


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'last_name', 'email', 'phone']


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'last_name', 'email', 'phone']


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'customer', 'seller', 'date', 'amount']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock']