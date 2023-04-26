from django import forms
from django.forms import ModelForm 
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Employeeform(forms.ModelForm):

    class Meta:
        model=Employee
        fields='__all__'
        labels= {
            'fullname':'Full Name',
            'emp_code':'EMP. Code'
        }

    def __init__(self,*args,**kwargs):
        super(Employeeform,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required=False
        self.fields['user'].required = False
        self.fields['profile_pic'].required = False
        self.fields['manager'].required = False
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']