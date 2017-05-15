from django import forms
from .models import Debt


class CreateDebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        fields = '__all__'
