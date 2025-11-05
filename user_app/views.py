from django.shortcuts import render,redirect

from django.views.generic import View

from user_app.forms import Userregisterform

from user_app.models import User

from django.contrib.auth import authenticate,login,logout
from expense_app.models import Expense

# Create your views here.
class RegisterView(View):
    def get(self,request):
        form = Userregisterform()
        return render(request,"signup.html",{"form":form})
    
    def post(self,request):
        print(request.POST)  
        username =request.POST.get('username')

        first_name =request.POST.get('first_name')

        last_name =request.POST.get('last_name')

        password =request.POST.get('password')  

        email =request.POST.get('email')

        User.objects.create_user(username=username,
                                 first_name=first_name,
                                 last_name=last_name,
                                 password=password,
                                 email=email)
        form = Userregisterform()
        return redirect("login")

#login view
# get post    

class LoginView(View):
    def get(self,request):

        return render(request,'signin.html')
    
    def post(self,request):
        username =request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("home")
        return render(request,"signin.html")

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("home")    
        
class Baseview(View):
    def get(self,request):
        if request.user.is_authenticated:

            expenses = Expense.objects.filter(user = request.user)
                                                                      # collection of objects (obj1, obj2, obj3)
            total_expense = sum(i.amount for i in expenses)

            return render(request,"home.html",{"expenses":expenses,"total_expense":total_expense})
        return render(request,"home.html")
