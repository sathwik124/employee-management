from django import forms
from django.forms import ModelForm 
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Employeeform(forms.ModelForm):

    class Meta:
        model=Employee
        exclude = ["profile_pic","user"]
        labels= {
            'fullname':'Full Name',
            'emp_code':'EMP. Code'
        }

    def __init__(self,*args,**kwargs):
        super(Employeeform,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required=False

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProfileForm(forms.ModelForm):

    class Meta:
        model=Employee
        fields = ['fullname','mobile','profile_pic']
        def __init__(self,*args,**kwargs):
            super(Employeeform,self).__init__(*args,**kwargs)
            self.fields['profile_pic'].required = False
