from django.shortcuts import render
from .models import *
from datetime import datetime
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
	return render (request,'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        deg = int(request.POST['designation'])
        image = request.FILES['image']  # Access the uploaded image file
        hire_date = datetime.now()

        # Check image size
        if image.size > 1024 * 1024:  # 1MB = 1024KB = 1024 * 1024 bytes
            return HttpResponse("Image size should be less than 1MB.")

        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            bonus=bonus,
            phone=phone,
            dept_id=dept,
            designation_id=designation,
            image=image,  
            hire_date=hire_date
        )
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception Occurred! Employee Has Not Been Added")

def remove_emp(request):
	return render (request,'remove_emp.html')


def filter_emp(request):
	return render (request,'filter_emp.html')