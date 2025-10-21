from django import forms
from user_app.models import User
class Userregisterform(forms.ModelForm):

    class Meta:

        model = User
        
        fields = ['username','first_name','last_name','password','email']



# class Userregisterform(forms.Form):

#     username =forms.CharField(max_length=50)

#     first_name =forms.CharField(max_length=50)

#     last_name =forms.CharField(max_length=50)

#     email =forms.EmailField()

#     password =forms.CharField(max_length=50)