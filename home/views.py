from django.shortcuts import render,HttpResponse
from .models import *
from datetime import datetime


# Create your views here.

def index(request):
	return render (request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST.get('bonus', 0))
        phone = int(request.POST.get('phone', 0))
        dept = int(request.POST['dept'])
        
        designation = request.POST.get('designation', 0)
        try:
            deg = int(designation)
        except ValueError:
            return HttpResponse("Invalid designation value.")
        
        image = request.FILES.get('media', None) # Access the uploaded image file
        hire_date = datetime.now()

        if image is not None:
            if image.size > 1024 * 1024:  # 1MB = 1024KB = 1024 * 1024 bytes
                return HttpResponse("Image size should be less than 1MB.")
            else:
                new_emp = Employee(
                    first_name=first_name,
                    last_name=last_name,
                    salary=salary,
                    bonus=bonus,
                    phone=phone,
                    dept_id=dept,
                    deg_id=deg,  # Use the correct field name for the designation
                    image=image,
                    hire_date=hire_date
                )
                new_emp.save()
                return HttpResponse('Employee added Successfully')
        else:
            return HttpResponse("No image uploaded.")

    return render(request, 'add_emp.html')


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html',context)


def filter_emp(request):
	return render (request,'filter_emp.html')