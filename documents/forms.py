from django import forms

class DocumentSearchForm(forms.Form):
    search_term = forms.CharField(label='Search Term', max_length=100)
