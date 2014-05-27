# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import logout

from doublekickApp.models import Player
# from django.db import models
# from math import *
import json


def index(request):
	return render(request, 'doublekickApp/UI/design/index.html',{});

def signupForm(request):
	
	return render(request,'doublekickApp/UI/design/signup.html',{});

def signup(request):
	firstName = request.POST['firstName']
	username = request.POST['username']
	user = User.objects.create_user(user, request.POST['password'])

	lastName = request.POST['lastName']
	age = request.POST['age']
	email = request.POST['email']
	mobileNumber = request.POST['mobileN']
	height = request.POST['height']
	weight = request.POST['weight']
	position = request.POST['position']
	
	player = Player(playerInfo=user,
					firstName=firstName,
					lastName=lastName,
					dateofbirth=age,
					email=email,
					mobileN=mobileNumber,
					nMatchesPlayed=0,
					height=height,
					weight=weight,
					position=position,
					matchesPlayed=0,
					tournPlayed=0,
					goals=0,
					speed=0,
					shooting=0,
					teamWork=0,
					passing=0
					)
	player.save()
	
	# redirection is here
	return HttpResponseRedirect(reverse('doublekickApp.views.dashboard',))

def loginForm(request):
	return render(request, 'doublekickApp/UI/design/login.html',{});

def custom_login(request):
    #get username
    username = request.POST['username']
    #get password
    password = request.POST['password']

    print "username", username
    print "password", password
    #authenticate user
    user = authenticate(username=username, password=password)

    if user is not None:
    	if user.is_active:
    		login(request, user)
    		return HttpResponseRedirect(reverse('doublekickApp.views.dashboard',))
    #     else:
    #         # Return a 'disabled account' error message
    # else:
    #     # Return an 'invalid login' error message.

# load the home once the user is logged in
@login_required(login_url='/app/loginForm')
def loadHome(request):
    e = Member.objects.get(userLinked=1)
    return render(request, 'doublekickApp/UI/home.html',{'userinfo':e})

@login_required(login_url='/app/loginForm/')
def dashboard(request):
	print "HELLO"
	return render(request, 'doublekickApp/UI/design/dashboard.html',{});

