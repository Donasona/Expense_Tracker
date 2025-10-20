from django.shortcuts import render

from django.views.generic import View

from user_app.forms import Userregisterform

# Create your views here.
class RegisterView(View):
    def get(self,request):
        form = Userregisterform()
        return render(request,"signup.html",{"form":form})