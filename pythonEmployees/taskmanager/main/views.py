from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Employee
from .forms import EmployeeForm, EmployeeUpdate
# Create your views here.


def home(request):
    return render(request, 'main/home.html')


def list_employee(request):
    employees = Employee.objects.all()
    return render(request, "main/list.html", {'employees': employees})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = EmployeeForm()
    context = {
        'form': form
    }
    return render(request, 'main/add.html', context)


def edit_employee(request, id):
    if id:
        employee = Employee.objects.get(id=id)
        if request.method == 'POST':
            form = EmployeeForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
                return redirect('home')
    form = EmployeeForm()
    context = {
        'form': form
    }
    return render(request, 'main/edit.html', context)