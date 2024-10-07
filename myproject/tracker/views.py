from django.shortcuts import render
from .forms import ExpenseForm
from django.contrib import messages
from .models import Expense
from .forms import DateForm
from django.db import models
from .forms import CategoryForm



# Create your views here.
def index(request):
    return render(request, 'index.html')

# def add_expense(request):
#     return render(request, 'add_expense.html')

def summary_by_date(request):
    return render(request, 'summary_by_date.html')

def summary_by_category(request):
    return render(request, 'summary_by_category.html')

def exit(request):
    return render(request, 'exit.html')

def add_expense_to_db(date, category, description, amount):
    expense = Expense(date=date, category=category, description=description, amount=amount)
    expense.save() 

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
             # Use the form data to call the custom function and add an expense
            date = form.cleaned_data['date']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            amount = form.cleaned_data['amount']
            
            add_expense_to_db(date, category, description, amount)
            
            messages.success(request, 'Expense added successfully!')
            
            # Clear the form after successful submission
            form = ExpenseForm()  # Reset the form

           # form.save()  # Save the form data to the database
    else:
        form = ExpenseForm()
    
    return render(request, 'add_expense.html', {'form': form})



def summary_by_date(request):
    expenses = []
    total_amount = 0

    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            # Get the selected date from the form
            selected_date = form.cleaned_data['date']
            
            # Filter the expenses for the selected date
            expenses = Expense.objects.filter(date=selected_date)
            
            # Calculate the total amount for the selected date
            total_amount = expenses.aggregate(total=models.Sum('amount'))['total'] or 0
            
    else:
        form = DateForm()

    return render(request, 'summary_by_date.html', {
        'form': form,
        'expenses': expenses,
        'total_amount': total_amount,
    })


def summary_by_category(request):
    expenses = []
    total_amount = 0

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            # Get the selected category from the form
            selected_category = form.cleaned_data['category']
            
            # Filter the expenses for the selected category
            expenses = Expense.objects.filter(category=selected_category)
            
            # Calculate the total amount for the selected category
            total_amount = expenses.aggregate(total=models.Sum('amount'))['total'] or 0
            
    else:
        form = CategoryForm()

    return render(request, 'summary_by_category.html', {
        'form': form,
        'expenses': expenses,
        'total_amount': total_amount,
        'selected_category': form.cleaned_data.get('category') if form.is_bound else None
    })