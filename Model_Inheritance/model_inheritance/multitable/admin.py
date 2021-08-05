from django.contrib import admin
from .models import Dept, stu_information
# Register your models here.
@admin.register(Dept)
class AdminDept(admin.ModelAdmin):
    list_display = ['Dept_name','Dept_code']

@admin.register(stu_information)
class AdminDept(admin.ModelAdmin):
    list_display = ['stu_name','age']