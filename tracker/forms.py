from django import forms

from . models import Item

class ItemModelForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('name','price','image')
