from datetime import datetime
from django.db.models.sql import where
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from booksapp import models
import datetime
from passlib.hash import pbkdf2_sha256
from django.contrib.auth import authenticate
from django.views import View
from django.contrib.auth.decorators import login_required

def reg(request):
    context = {
        'form': RegisterForm,
    }
    return render(request, 'registration.html', context)

def submitform(request):
    username = request.GET['username']
    age = request.GET['age']
    password = request.GET['password']
    if models.User.objects.filter(username=username).exists():
        messages.add_message(request, messages.INFO, 'User with same username already exists!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    hashed_password = pbkdf2_sha256.hash(password)
    context = {
        'form': RegisterForm,
    }
    models.User.objects.create(username=username, password=hashed_password, age=age, created=datetime.datetime.now())
    context['success'] = 'You may login now!'
    return render(request, 'registration.html', context)

@login_required(login_url=" ")
def home(request):
    if request.method == "POST":
        context = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("username", username)
        print("username", password)

        if username != "":
            if models.User.objects.filter(username=username).exists():
                if password != "":
                    try:
                        hashed_pass = models.User.objects.filter(username=username).values('password')[0]['password']
                        user_age = models.User.objects.filter(username=username).values('age')[0]['age']
                        pbkdf2_sha256.verify(password, hashed_pass)
                        all_books = models.Book.objects.extra(where=["min_age <='{}'".format(user_age)])
                        context = {
                            'all_books' : all_books
                        }
                        return render(request, 'home.html', context)
                    except:
                        context['failed'] = 'Please check password!'
                        return render(request, 'registration.html', context)
                else:
                    context['failed'] = 'Please enter password'
                    return render(request, 'registration.html', context)
            else:
                context['failed'] = 'User not found'
                return render(request, 'registration.html', context)
        else:
            context['failed'] = 'Please enter username'
            return render(request, 'registration.html', context)
    return render(request, 'registration.html')
    