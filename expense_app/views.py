from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from expense_app.forms import ExpenseForm

class Add_expense_view(View):
    def get(self,request):
        form = ExpenseForm()
        return render(request,"expense_add.html",{"form":form})
