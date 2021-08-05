from django.contrib import admin
from .models import table_proxy,same_table
# Register your models here.
@admin.register(table_proxy)
class AdminDept(admin.ModelAdmin):
    list_display = ['Dept_name','Dept_code']

@admin.register(same_table)
class AdminDept(admin.ModelAdmin):
    list_display = ['Dept_name','Dept_code']