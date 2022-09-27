import datetime
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import Task

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "You've successfully created a new account!")
            return redirect('todolist:login')

    context = {'form' : form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Wrong username or password :(')
    
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url = '/todolist/login/')
def show_todolist(request):
    data = Task.objects.all()

    context = {
        'data_todolist' : data,
        'last_login' : request.COOKIES['last_login']
    }

    return render(request, "todolist.html", context)

def create_task(request):
    form = UserCreationForm()

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            user = request.user
            date = datetime.date.today()
            title = request.POST.get('task_name')
            description = request.POST.get('task_description')

            task = Task.objects.create(user = user, date = date, title = title, description = description)
            messages.success(request, "Successfully added task!")
            return redirect('todolist:show_todolist')

    context = {'form' : form}
    return render(request, 'create_task.html', context)