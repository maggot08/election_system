from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')
    #return HttpResponse("This is my app.")

def userlogin(request):
    return render(request, 'login.html')

def handlelogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Welcome to Dashboard")
            return redirect("/login")
        else:
            messages.warning(request, "Invalid User")
            return redirect("/login")
    return HttpResponse("404 NOT FOUND")

def signup(request):
    return render(request, 'signup.html')


def handlesignup(request):
    if request.method=="POST":
        fname=request.POST['signupfname']
        lname=request.POST['signuplname']
        username=request.POST['signupusername']
        email=request.POST['signupemail']
        password=request.POST['signuppassword']
        password2=request.POST['signuppassword2']
        
        #check parameter
        if password!=password2:
            messages.error(request, "Password didn't match.")
            return HttpResponseRedirect('/signup')
        if User.objects.filter(username=username).first():
            messages.warning(request, "This username is already taken.")
            return HttpResponseRedirect('/signup')
        if User.objects.filter(email=email).first():
            messages.warning(request, "E-mail is already exist")
            return HttpResponseRedirect('/signup')

        #creating users.
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        return redirect('/login')
    else:
        return HttpResponse("404 error....")
    
def aboutus(request):
    return render(request, 'aboutus.html')

def events(request):
    return render(request, 'events.html')

def howtovote(request):
    return render(request, 'howtovote.html')

def dashboard(request):
    return render(request, 'dashboard/admindashboard.html')