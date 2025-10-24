from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from expense_app.forms import ExpenseForm

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