from django.shortcuts import render,redirect
from .forms import Employeeform
from .models import Employee
from .filters import OrderFilter
# Create your views here.
def employee_list(request):
    emplist = Employee.objects.all()
    myFilter = OrderFilter(request.GET,queryset=emplist)
    emplist = myFilter.qs
    context = {'employee_list':emplist,'myFilter':myFilter}
    return render(request,"employee_register/employee_list.html",context)

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

def employee_delete(request,id):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')