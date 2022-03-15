from multiprocessing import context
from django.shortcuts import render, redirect 

from employee_details.forms import EmployeeForm
from employee_details.models import Employee
from .forms import EmployeeForm
# Create your views here.

def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request,"employee_details/employee_list.html",context)

def employee_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request,"employee_details/employee_form.html",{'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save() 
        return redirect('/employee/list')
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list') 