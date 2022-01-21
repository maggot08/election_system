from django.contrib.auth.models import User
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from myapp.form import *
import pdb 

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
    contestant=Contestant.objects.filter(event_id=id)
    current_user = request.user
    user_id = current_user.id
    vote = Voted.objects.filter(event_id=id)
    if len(vote) > 0:
        user_ids = []
        user_details = vote.values('voting_user_id')
        for user in user_details:
            for id in user['voting_user_id']:
                user_ids.append(id)
            # pdb.set_trace()
        # event_id = []
        # for event in vote_details:
        #     event_id.append(event['event_id'])
        # voted = vote.values('is_voted')[0]['is_voted']
        # pdb.set_trace()
        # pdb.set_trace()
        if user_id in user_ids:
            user_voted = True
        else:
            user_voted = False 
    else:
        user_voted= False
    # pdb.set_trace()
    voting=Voted.objects.all()
    event=Event.objects.all()
    context={
        'contestants':contestant,
        'votings':voting,
        'events':event,
        'voted': user_voted,
    }

    return render(request, 'contestants.html', context)

def voted(request, id):
    if request.user.is_authenticated:
        contestant=Contestant.objects.get(pk=id)
        event=Event.objects.get(pk=int(request.META.get('HTTP_REFERER').split('/')[-1]))
        previous_count = Voted.objects.filter(voting_user_id=request.user.id)
        # if len(previous_count) > 0:
        vote = Voted.objects.filter(contestant_id=id)
        # pdb.set_trace()
        if len(vote) > 0:
            user_ids = []
            user_details = vote.values('voting_user_id')
            for user in user_details:
                for id in user['voting_user_id']:
                    user_ids.append(id)
            # pdb.set_trace()
            user_ids.append(request.user.id)
            count = vote.values('count')[0]['count']
            obj = vote.update(count=count+1, voting_user_id=user_ids)
            # obj.count = count+1
            # pdb.set_trace()
            # obj.save()
        else:
            #vote_count=Voted.objects.filter('count')
            user=request.user
            # pdb.set_trace()
            is_voted=True
            count=1
            isvoted=Voted(is_voted= is_voted, voting_user_id= [user.id], count=count,contestant=contestant, event=event)
            print (contestant.contestant_name)
            isvoted.save()

        messages.success(request, "Your vote is successful!!!")
        return redirect ('/events')     
    else:
        messages.success(request, "First Login To Vote!!!")
        return redirect ('/login')

def events(request):
    event=Event.objects.all()
    context={
        'events':event
    }
    return render(request, 'events.html',context)


def howitworks(request):
    return render(request, 'howitworks.html')

def contestant_profile(request):
    return render(request, 'contestant_profile.html')

def eventdetail(request):
    return render(request, 'eventdetail.html')

def dashboard(request):
    contestant=Contestant.objects.all()
    voting=Voted.objects.all()
    if request.user.is_authenticated and request.user.is_superuser:
        pass
    else:
        messages.warning(request, "You are not Authorized to access this page!!")    
        return redirect("/")
    context={
        'contestants':contestant,
        'votings':voting
    }
    
    return render(request, 'dashboard/admindashboard.html', context)

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

def adminprofile(request):
    if request.user.is_authenticated and request.user.is_superuser:
        pass
    else:
        messages.warning(request, "You are not Authorized to access this page!!")    
        return redirect("/")
    return render(request, 'dashboard/adminprofile.html')

def voteresults(request):
    event=Event.objects.all()
    context={
        'events':event
    }
    return render(request, 'dashboard/vote_results.html', context)

def results(request, id):
    voting=Voted.objects.filter(event_id=id)
    #if Voted.objects.filter(Contestant.contestant_id)
    contestant=Contestant.objects.filter(event_id=id)

    context={
        'votings':voting,
        'contestants':contestant,
    }
    return render(request, 'dashboard/result_chart.html', context)

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

def contestanttables(request, id):
    contestant=Contestant.objects.filter(event_id=id)
    voting=Voted.objects.all()
    event=Event.objects.all()
    
    context={
        'contestants':contestant,
        'votings':voting,
        'events':event,
    }

    return render(request, 'dashboard/contestanttables.html', context)

def addcontestant(request):
    if request.user.is_authenticated and request.user.is_superuser:
        pass
    else:
        messages.warning(request, "You are not Authorized to access this page!!")    
        return redirect("/")
    if request.method=="POST":
        form=Contestantform(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Contestant added successfully!!!")
            form=Contestantform()
            print (request.GET.get('event', ''))
            return redirect("/event")
    else:
        form=Contestantform()
    return render(request, 'dashboard/addcontestant.html',{'form':form})

def deletecontestant(request, contestant_id):
    contestant=Contestant.objects.get(pk=contestant_id)
    contestant.delete()

    messages.warning(request, "contestant Deleted!!!")   
    return redirect('contestanttables')

def editcontestant(request, id):
    if request.method=="POST":
        contestant=Contestant.objects.get(pk=id)
        form=Contestantform(request.POST, request.FILES, instance=contestant)
        if form.is_valid:
            form.save()
            messages.success(request, "Contestant updated successfully!!!")
            form=Contestantform()
            return redirect("/event")
    else:
        contestant=Contestant.objects.get(pk=id)
        form=Contestantform(instance=contestant)
    
    return render(request,'dashboard/editcontestant.html', {'contestant':contestant,'form':form})

