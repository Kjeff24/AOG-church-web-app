from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import  Profile, CurrentNews, LiveSession

def welcome(request):
    return render(request, 'myapp/welcome.html')
    
def homepage(request):
    news = CurrentNews.objects.all().order_by('-pub_date')[:3]
    liveSessions = LiveSession.objects.all().order_by('-pub_date')[:4]
    context = {'liveSessions':liveSessions, 'news':news}
    return render(request, 'myapp/homepage.html', context)

def about(request):
    news = CurrentNews.objects.all().order_by('-pub_date')[:3]
    liveSessions = LiveSession.objects.all().order_by('-pub_date')[:2]
    context = {'liveSessions':liveSessions, 'news':news}
    return render(request, 'myapp/about.html', context)

def department(request):
    return render(request, 'myapp/department.html')

def newsUpdate(request):
    news = CurrentNews.objects.all().order_by('-pub_date')
    return render(request, 'myapp/newsUpdate.html', {'news':news})   

def profile(request):
    profiles = Profile.objects.all()
    return render(request, 'myapp/profile.html', {'profiles': profiles})


def upcomingEvents(request):
    liveSessions = LiveSession.objects.all().order_by('-pub_date')
    context = {'liveSessions':liveSessions}
    return render(request, 'myapp/upcomingEvents.html', context)

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Username or Password does not exist')

    return render(request, 'myapp/login.html')

def logoutUser(request):
    logout(request)
    return redirect('welcome')

def signupPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('signup_success')
        else:
            messages.error(request, "Username already exits or password don't match")

    context = {'form':form}
    return render(request, 'myapp/signup.html', context)

def signup_success(request):
    return render(request, 'myapp/signupsuccess.html')

