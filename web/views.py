from django.shortcuts import render
from django.views import generic
from .models import Diary, Month, Money
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    ordering = ['-time']
    login_url = '/accounts/login/'
        
class DiaryCreate(CreateView):
    model = Diary
    fields = '__all__'
    success_url = "/"
    template_name = 'form.html'    

class DiaryUpdate(UpdateView):
    model = Diary
    fields = '__all__'
    success_url = "/"   
    template_name = 'form.html'      

class DiaryDelete(DeleteView):
    model = Diary
    success_url = "/"
    template_name = 'confirm_delete.html'    
    
class MoneyListView(generic.ListView):
    model = Money
    ordering = ['-time']
        
class MoneyCreate(CreateView):
    model = Money
    fields = '__all__'
    success_url = "/web/money"
    template_name = 'form.html'

class MoneyUpdate(UpdateView):
    model = Money
    fields = '__all__'
    success_url = "/web/money"    
    template_name = 'form.html'      

class MoneyDelete(DeleteView):
    model = Money
    success_url = "/web/money"   
    template_name = 'confirm_delete.html'       