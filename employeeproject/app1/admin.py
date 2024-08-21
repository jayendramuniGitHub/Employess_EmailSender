from django.contrib import admin
from .models import employee
# Register your models here.
class employeeadmin(admin.ModelAdmin):
    list_display=['name','email','phone_number']

admin.site.register(employee,employeeadmin)