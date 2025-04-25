from django.shortcuts import render
from investments.models import Entry
from investments.forms import EntryModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewInvest(View):
    def get(self, request):
        last_entry = Entry.objects.last()
        form = EntryModelForm()
        context = {'form': form, 'last_entry': last_entry}
        return render(request, 'new_invest.html', context)
    
    def post(self, request):
        form = form = EntryModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Entrada cadastrada com sucesso!')
            return redirect('new_invest')
        return render(request, 'new_invest.html', {'form': form})
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class EditInvest(View):
    def get(self, request, id):
        editentry = get_object_or_404(Entry, pk=id)
        form = EntryModelForm(instance=editentry)
        return render(request, 'edit_invest.html', {'form': form})

    def post(self, request, id):
        editentry = get_object_or_404(Entry, pk=id)
        form = EntryModelForm(request.POST or None, instance=editentry)
        if form.is_valid():
            form.save()
            return redirect('new_invest')
        return render(request, 'edit_invest.html', {'form': form})
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class EntryDelete(View):
    def get(self, request, id):
        entry = get_object_or_404(Entry, pk=id)
        form = EntryModelForm(instance=entry)
        return render(request, 'delete_invest.html', {'form': form, 'entry': entry})
    
    def post(self, request, id):
        entry = get_object_or_404(Entry, pk=id)
        form = EntryModelForm(instance=entry)
        entry_deleted = entry.delete()
        return redirect('new_invest')
     

