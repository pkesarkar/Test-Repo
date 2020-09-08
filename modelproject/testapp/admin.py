from django.contrib import admin
from testapp.models import Employee
# Register your models here.

class Employeeadmin(admin.ModelAdmin):
    list_display=['eno','ename','esal']

admin.site.register(Employee,Employeeadmin)
