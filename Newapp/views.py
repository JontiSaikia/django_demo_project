from django.shortcuts import render, redirect
from datetime import datetime
from Newapp.models import Contact
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import logout , authenticate ,login
# Create your views here.

def index(request):
    context = {
        'var':"your request is sent"
    }
    #messages.success(request,"This is a test message")
    return render(request,'index.html')
    #return HttpResponse("this is homepage")

def about(request):
    return render(request,'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message is sent!')
        
    return render(request,'contact.html')
    # return HttpResponse("this is contact page")
    
#password for test user is ##Jonti@123$$
# Create your views here.
# def index(request):
#     print(request.user)
#     if request.user.is_anonymous:
#         return redirect("/")
#     return render(request,'index.html')
    
def loginUser(request):
    if request.method=="POST":
            #check if user has entered correct information
        username= request.POST.get('username')
        password = request.POST.get('password')
        
        print(username,password)
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/index")
        else:
             # No backend authenticated the creden
            return render(request,'login.html')
    
    return render(request,'login.html')
    
def logoutUser(request):
    logout(request)
    return redirect("/loginUser")

