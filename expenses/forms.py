from django import forms
from expenses.models import Expenses

class ExpensesModelForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['exp_name', 'status', 'value', 'payday']
        widgets = {
            'exp_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Conta de Luz'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'value': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Ex: 250.00'
            }),
            'payday': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }, format='%Y-%m-%d'
            ),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Formatando o valor inicial para aparecer corretamente no input
            if self.instance and self.instance.payday:
                self.initial['payday'] = self.instance.payday.strftime('%Y-%m-%dT%H:%M')