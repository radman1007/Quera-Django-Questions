from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'stock']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price > 1000:
            raise ValidationError("Product is too expensive")
        return price

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) <= 20:
            raise ValidationError("Product must have a good description")
        return description
