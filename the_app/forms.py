from django import forms
from .models import Listings

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Listings
        fields = ["title", "condition", "delivery", "price"]