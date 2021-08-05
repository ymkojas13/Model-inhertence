from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class AdminStudentDetails(admin.ModelAdmin):
    list_display = ['st_id','name','age','place']

