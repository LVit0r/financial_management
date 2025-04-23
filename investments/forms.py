from django import forms
from investments.models import Entry

class EntryModelForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['value', 'origin', 'date']
        widgets = {
            'value': forms.NumberInput(attrs={
                'class': 'form-control', 
                'step': '0.01',
                'placeholder': 'Ex: 150.00'
            }),
            'origin': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Salário'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }