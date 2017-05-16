from django import forms
from .models import Customer


class SearchForm(forms.Form):
    query = forms.CharField(label='Search by ID or Phone ',
                            widget=forms.TextInput(attrs={'size': 32, 'id': 'user_input',
                                                   'placeholder': 'Search by ID or Phone',
                                                          'data-provide': 'typeahead',
                                                          'class': 'form-control customer-search typeahead'}))


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
