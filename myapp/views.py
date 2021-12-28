from django.contrib.auth.models import User
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from myapp.form import *

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
            if request.user.is_superuser:
                messages.success(request, "Welcome to Admin Dashboard!!")
                return redirect("/dashboard")
            else:
                messages.warning(request, "Successfully Loged In as User!!")
                return redirect("/events")
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

def contestants(request, id):
    try:
        contestant=Contestant.objects.get(pk=id)
    except Contestant.DoesNotExist:
        contestant=None
    context={
        'contestants':contestant
    }

    return render(request, 'contestants.html', context)

def events(request):
    event=Event.objects.all()
    context={
        'events':event
    }
    return render(request, 'events.html',context)


def howitworks(request):
    return render(request, 'howitworks.html')

def eventdetail(request):
    return render(request, 'eventdetail.html')

def dashboard(request):
    if request.user.is_authenticated and request.user.is_superuser:
        pass
    else:
        messages.warning(request, "You are not Authorized to access this page!!")    
        return redirect("/")
    return render(request, 'dashboard/admindashboard.html')

def handlelogout(request):
    logout(request)
    messages.warning(request, "Successfully Logged Out")
    return redirect('/index')

def event(request):
    if request.user.is_authenticated and request.user.is_superuser:
        pass
    else:
        messages.warning(request, "You are not Authorized to access this page!!")    
        return redirect("/")
    event=Event.objects.all()
    context={
        'events':event
    }
    return render(request, 'dashboard/event.html',context)

def profile(request):
    if request.user.is_authenticated and request.user.is_superuser:
        pass
    else:
        messages.warning(request, "You are not Authorized to access this page!!")    
        return redirect("/")
    return render(request, 'dashboard/profile.html')

def addevent(request):
    if request.user.is_authenticated and request.user.is_superuser:
        pass
    else:
        messages.warning(request, "You are not Authorized to access this page!!")    
        return redirect("/")
    if request.method=="POST":
        form=Addeventform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Event added successfully")
            form=Addeventform()
            return redirect("/event")
    else:
        form=Addeventform()
    return render(request, 'dashboard/addevent.html',{'form':form})

def deleteevent(request, event_id):
    event=Event.objects.get(pk=event_id)
    event.delete()

    messages.warning(request, "Event Deleted!!!")   
    return redirect('event')

def editevent(request, id):
    if request.method=="POST":
        event=Event.objects.get(pk=id)
        form=Eventform(request.POST, request.FILES, instance=event)
        if form.is_valid:
            form.save()
            messages.success(request, "Event updated successfully!!!")
            form=Eventform()
            return redirect("/event")
    else:
        event=Event.objects.get(pk=id)
        form=Eventform(instance=event)
    
    return render(request,'dashboard/editevent.html', {'event':event,'form':form})

def contestant(request):
    if request.user.is_authenticated and request.user.is_superuser:
        pass
    else:
        messages.warning(request, "You are not Authorized to access this page!!")    
        return redirect("/")
    if request.method=="POST":
        form=Contestantfrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "added successfully")
            form=Contestantfrom()
            return redirect("/contestanttable")
    else:
        form=Contestantfrom()

    return render(request, 'dashboard/contestanttable.html',{'form':form})
