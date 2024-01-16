from django.shortcuts import render
from django.http import HttpResponse
from . models import Department
from . models import *
from . forms import Bookingform,ContactForm

# Create your views here.
# def index(request):
#     return HttpResponse("django")
def index(request):
    return render(request,"home.html")
def index1(request):
    return render(request,"about.html")

def index2(request):
    if request.method =='POST':
        form=Bookingform(request.POST)
        if form.is_valid():
            form.save()
            
    form=Bookingform
    dict_form={
        'form':form
    }
    return render(request,"booking.html",dict_form)


def index4(request):
    dict_doc={
        'doc':Doctors.objects.all()
    }
    return render(request,"doctors.html",dict_doc)

def index5(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request,"department.html",dict_dept)

def index3(request):
    if request.method =='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form=ContactForm
    dict_cont ={
        'form':form
    }
    return render(request,"contact.html", dict_cont )