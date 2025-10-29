from django.shortcuts import render,redirect
from django.views.generic import View
# Create your views here.
from expense_app.forms import ExpenseForm
from expense_app.models import Expense
from django.shortcuts import get_object_or_404

class Add_expense_view(View):
    def get(self,request):
        form = ExpenseForm()
        return render(request,"expense_add.html",{"form":form})
    
    def post(self,request):
        print(request.POST)
        form =ExpenseForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
        return render(request,"expense_add.html",{"form":form})    
    
class ExpenseListView(View):
    def get(self,request):
        expenses = Expense.objects.filter(user =request.user)  
        return render(request,"expense_list.html",{"expenses":expenses})  
    
    # update view

class ExpenseUpdateView(View):
    def get(self,request,**kwargs):
        id = kwargs.get("pk")
        expense = Expense.objects.get(user= request.user,id=id)
        form =ExpenseForm(instance=expense)
        return render(request,"expense_update.html",{"form":form})

class Expensedelete(View):
    def get(self,request,**kwargs):
        id = kwargs.get("pk")
        expense =get_object_or_404(Expense,id=id,user=request.user)
        expense.delete()
        return redirect("home")   
