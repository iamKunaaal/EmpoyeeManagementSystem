from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, template_name='index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    # print(context)
    return render(request, template_name='all_emp.html' , context=context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])      
        dept = request.POST['dept']
        role = request.POST['role']
        new_emp = Employee(first_name = first_name, last_name = last_name, salary = salary, bonus = bonus, phone = phone, dept_id = dept, role_id = role, hire_date = datetime.now())
        new_emp.save() 
        return HttpResponse("employee added succsessfully")
    elif request.method == 'GET': 
        return render(request, template_name='add_emp.html')
    else:
        return HttpResponse("An Exeption Occured!!")   
  

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_remove = Employee.objects.get(id = emp_id)
            emp_to_be_remove.delete()
            return HttpResponse("Employee Deleted Succsuccfully")
        except:
            return HttpResponse("please enter a valid employee id")
    
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    
    return render(request, template_name='remove_emp.html', context=context)

def filter_emp(request):
     if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name = dept)

        context = {
             'emps': emps
                 }
        return render(request, template_name='all_emp.html' , context=context)
     elif request.method == 'GET':
        return render(request, template_name='filter_emp.html')
     else:
        return HttpResponse("an Error ouures")   
