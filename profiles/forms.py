from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label='Search by ID or Phone ',
                            widget=forms.TextInput(attrs={'size': 32, 'id': 'user_input',
                                                   'placeholder': 'Search by ID or Phone',
                                                          'data-provide': 'typeahead',
                                                          'class': 'form-control customer-search typeahead'}))

# Profiles forms.py