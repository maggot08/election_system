from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')
    #return HttpResponse("This is my app.")

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def signup(request):
    if request.method=="POST":
        name=request.POST['signupname']
        username=request.POST['signupusername']
        email=request.POST['signupemail']
        password=request.POST['signuppassword']
        repeatpassword=request.POST['signuppassword2']
        myuser=User.objects.create_user(username,email,password)
        myuser.name=name
        myuser.save()
        return redirect('/signup')
    else:
        return HttpResponse("404 error")

    return render(request, 'signup.html')
    
def aboutus(request):
    return render(request, 'aboutus.html')

def events(request):
    return render(request, 'events.html')

def howtovote(request):
    return render(request, 'howtovote.html')