from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        if int(self.cleaned_data.get('price')) > 1000:
            raise ValidationError('Product is too expensive')
        if len(self.cleaned_data.get('description')) <= 20:
            raise ValidationError('Product must have a good description')
        return self.cleaned_data
