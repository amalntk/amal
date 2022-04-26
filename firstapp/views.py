from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
import os
# Create your views here.
def index(request):
    return render(request,"index.html")
def welcome(request):
    return render(request,"welcome.html")
# def login(request):
#     return render(request,"login.html")
# def register(request):
#     return render(request,"register.html")
def bmic(request):
    return render(request,"bmi.html")
def logout(request):
    return render(request,"welcome.html")


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            # messages.success(request,'Account was created for' + user)
            return redirect('login')
    context = {'form':form} 
    return render(request,'register.html',context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        user= authenticate(request,username=username,password=password)  
        if user is not None:
            auth_login(request,user)
            return redirect('index')
        else:
            pass
            # messages.info(request,'Username OR password is incorrect')
    context={}
    return render(request,'login.html',context)
def calorie(request):
    os.system('start cmd')
    return render(request,"index.html")
# def simple_function(request):
    
#     return render(request,'calorie.html')
def apc(request):
    os.system('start cmd')
    return render(request,"index.html")
