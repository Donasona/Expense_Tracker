from django.shortcuts import render,redirect
from django.views.generic import View,UpdateView
# Create your views here.
from expense_app.forms import ExpenseForm
from expense_app.models import Expense
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q

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

# class ExpenseUpdateView(View):
#     def get(self,request,**kwargs):
#         id = kwargs.get("pk")
#         expense = Expense.objects.get(user= request.user,id=id)
#         form =ExpenseForm(instance=expense)
#         return render(request,"expense_update.html",{"form":form})
    
class ExpenseUpdateView(UpdateView):
    model=Expense
    form_class =ExpenseForm
    template_name ="expense_update.html"
    success_url = reverse_lazy("home")
    
    def get_queryset(self):
        return Expense.objects.filter(user =self.request.user)


class Expensedelete(View):
    def get(self,request,**kwargs):
        id = kwargs.get("pk")
        expense =get_object_or_404(Expense,id=id,user=request.user)
        expense.delete()
        return redirect("home")   
    
class ExpenseSearchView(View):
    template_name = "expense_search.html"
    def get(self,request):
        # filtering all expense of the logined user
        query =request.GET.get("q") 
        expenses = Expense.objects.filter(user =request.user)
        # filtering using the given query from the filtered expense above 
        if query:
            expenses = expenses.filter(Q(title_icontains =query) | Q(category_icontains =query)) 
