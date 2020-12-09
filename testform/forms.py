from django import forms
from .models import Property


class PropForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ["types", "price", "size", "city", "owner"]