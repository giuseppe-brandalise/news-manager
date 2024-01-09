from django import forms


class CategoryForm(forms.Form):
    name = forms.CharField(
        label='Nome',
        max_length=200,
        widget=forms.TextInput(attrs=({'type': 'text'}))
        )