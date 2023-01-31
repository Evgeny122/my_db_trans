from django import forms
from .models import Carrier


class CarrierModelForm(forms.ModelForm):
    class Meta:
        model = Carrier
        fields = [
            'name',
            'telephone',
            'ati',
            'direction',
        ]