from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    obj = Student.objects.all()
    return render(request,'home.html',{'obj':obj})

