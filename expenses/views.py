from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from expenses.models import Expenses, Extract
from expenses.forms import ExpensesModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import Sum
from django.contrib import messages




class ExpensesOverview(View):

    def get(self, request):
        total_value = Expenses.objects.aggregate(total=Sum('value'))['total']
        return render(request, 'exp_overview.html', {'total_value': total_value})



class NewExp(View):
    def get(self, request):
        last_expense = Expenses.objects.last()
        form = ExpensesModelForm()
        context = {'form': form, 'page_title': 'Nova Despesa', 'last_expense': last_expense}
        return render(request, 'new_exp.html', context)
    
    
    def post(self, request):
        form = ExpensesModelForm(request.POST)
        context = {'form': form, 'page_title': 'Nova Despesa'}
        if form.is_valid():
            form.save()
            messages.success(request, 'Despesa cadastrada com sucesso!')
            return redirect('new_exp')
        return render(request, 'new_exp.html', context)        



class EditExp(View):
    def get(self, request, id):
        editexp = get_object_or_404(Expenses, pk=id)
        form = ExpensesModelForm(instance=editexp)
        return render(request, 'edit_exp.html', {'form': form})

    def post(self, request, id):
        editexp = get_object_or_404(Expenses, pk=id)
        form = ExpensesModelForm(request.POST or None, instance=editexp)
        if form.is_valid():
            form.save()
            return redirect('expenses_overview')
        return render(request, 'edit_exp.html', {'form': form})
    

class DeleteExp(View):
    def get(self, request, id):
        expense = get_object_or_404(Expenses, pk=id)
        form = ExpensesModelForm(instance=expense)
        return render(request, 'delete_exp.html', {'expense': expense, 'form': form})
    
    def post(self, request, id):
        expense = get_object_or_404(Expenses, pk=id)
        form = ExpensesModelForm(instance=expense)
        expense_deleted = expense.delete()
        return redirect('new_exp')
 