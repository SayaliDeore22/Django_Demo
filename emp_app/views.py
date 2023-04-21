from django.shortcuts import render, HttpResponse
from . models import Employee, Department, Role
from datetime import datetime

def index(request):
    return render(request, "index.html")


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        "emps": emps
    }
    print(context)
    return render(request, "all_emp.html", context)


def add_emp(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        salary = int(request.POST["salary"])
        bonus = int(request.POST["bonus"])
        phone = int(request.POST["phone"])
        dept = int(request.POST["dept"])
        role = int(request.POST["role"])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone,
                 dept_id=dept, role_id=role, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully!!")
    elif request.method == "GET":
        return render(request, "add_emp.html")
    else:
        return HttpResponse("An Exception occurred")


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_remove = Employee.objects.get(id=emp_id)
            emp_remove.delete()
            return HttpResponse("Employee Removed Successfully!!!")
        except:
            return  HttpResponse("Please enter valid emp_id!!")

    emps = Employee.objects.all()
    context = {
        "emps": emps
    }
    print(context)
    return render(request, "remove_emp.html", context)


def filter_emp(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        role = request.POST["role"]

        emps = Employee.objects.all()

        if first_name:
            emps = emps.filter(first_name__icontains=first_name)
        if last_name:
            emps = emps.filter(last_name__icontains=last_name)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {
            "emps": emps
        }
        return render(request, "all_emp.html", context)

    elif request.method == "GET":
        return render(request, "filter_emp.html")

    else:
        return HttpResponse("Exception occurs")
