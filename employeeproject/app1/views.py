from django.shortcuts import render, redirect, get_object_or_404
from .forms import employeeForm
from .models import employee
from django.http import HttpResponse
from django.conf import settings
import smtplib

def home(request):
    form = employeeForm()
    if request.method == 'POST':
        if 'register_employee' in request.POST:
            form = employeeForm(request.POST)
            if form.is_valid():
                print("Registration form is valid. Saving employee data.")
                form.save()
                print("Employee data saved successfully.")
                return redirect('home')  # Redirect to the home page after saving
            else:
                print("Registration form is not valid.")
                print(form.errors)
        elif 'send_email' in request.POST:
            try:
                print("Attempting to send email.")
                server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
                server.starttls()
                server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                server.sendmail(
                    settings.EMAIL_HOST_USER,
                    'jayaanem@gmail.com',  # Change this to the actual receiver email
                    'Subject: hello jayendramuni'  # Replace with the actual message
                )
                server.quit()
                print("Email sent successfully.")
                return HttpResponse("Email sent successfully")
            except Exception as e:
                print(f"Failed to send email: {e}")
                return HttpResponse(f"Failed to send email: {e}")

    employees = employee.objects.all()
    print("Employee data retrieved:", employees)

    context = {
        'form': form,
        'data': employees,
    }
    return render(request, 'app1/index.html', context)

def delete_employee(request, id):
    print(f"Attempting to delete employee with ID: {id}")
    try:
        employee_obj = employee.objects.get(pk=id)
        employee_obj.delete()
        print("Employee deleted successfully.")
    except employee.DoesNotExist:
        print("Employee not found.")
    return redirect('home')

def update_employee(request, id):
    employee_obj = get_object_or_404(employee, pk=id)
    if request.method == 'POST':
        form = employeeForm(request.POST, instance=employee_obj)
        if form.is_valid():
            print("Update form is valid. Updating employee data.")
            form.save()
            print("Employee data updated successfully.")
            return redirect('home')
        else:
            print("Update form is not valid.")
            print(form.errors)
    else:
        form = employeeForm(instance=employee_obj)

    context = {
        'form': form,
    }
    return render(request, 'app1/update.html', context)
