from django.shortcuts import render,redirect
from .forms import Employeeform,CreateUserForm
from .models import Employee
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decoraters import unauthenticated_user,allowed_users,admin_only
# Create your views here.
@login_required(login_url='/employee/login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def employee_list(request):
    emplist = Employee.objects.all()
    myFilter = OrderFilter(request.GET,queryset=emplist)
    emplist = myFilter.qs
    context = {'employee_list':emplist,'myFilter':myFilter}
    return render(request,"employee_register/employee_list.html",context)

@login_required(login_url='/employee/login')

@admin_only
def employee_form(request,id=0):
    if request.method == "GET":
       if id==0:
           form=Employeeform()
       else:
           employee=Employee.objects.get(pk=id)
           form=Employeeform(instance=employee)
       return render(request,"employee_register/employee_form.html",{'form':form})
    else:
        if id==0:
           form=Employeeform(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            form=Employeeform(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')    

@login_required(login_url='/employee/login')
@allowed_users(allowed_roles=['admin'])
def employee_delete(request,id):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')

@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/employee')
        else:
            messages.info(request,'Username OR Password is incorrect')
    context = {}
    return render(request, "employee_register/login.html", context)
def logoutUser(request):
    logout(request)
    return redirect('/employee/login')

@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='employees')
            user.groups.add(group)
            
            messages.success(request,'Account has been created for ' + username)

            return redirect('/employee/login')
    context = {'form':form}
    return render(request, "employee_register/register.html", context)
@login_required(login_url='/employee/login')
def userPage(request):
    return render(request,"employee_register/user.html")