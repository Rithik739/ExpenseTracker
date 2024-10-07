from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'category', 'description', 'amount']
        
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'DD/MM/YYYY'}),
            'category': forms.Select(choices=Expense.CATEGORY_CHOICES),
            'description': forms.TextInput(attrs={'placeholder': 'Enter description'}),
            'amount': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'Enter amount'}),
        }

class DateForm(forms.Form):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Enter Date",
        input_formats=['%Y-%m-%d']
    )

class CategoryForm(forms.Form):
    CATEGORY_CHOICES = [('', '---')] + Expense.CATEGORY_CHOICES  # Blank option as placeholder

    category = forms.ChoiceField(
        choices=Expense.CATEGORY_CHOICES,  # Use the same choices defined in the Expense model
        label="Select Category",
        required=True

    )
