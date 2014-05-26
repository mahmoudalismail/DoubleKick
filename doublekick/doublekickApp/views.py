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

from doublekick.models import *
# from math import *
import json


def index(request):
	return render(request, 'doublekickApp/UI/index.html',{});


def loginForm(request):
	return render(request, 'doublekickApp/UI/loginForm.html',{});

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
    		return HttpResponseRedirect(reverse('doublekickApp.views.loadHome',))
    #     else:
    #         # Return a 'disabled account' error message
    # else:
    #     # Return an 'invalid login' error message.

# load the home once the user is logged in
@login_required(login_url='/app/')
def loadHome(request):
    e = Member.objects.get(userLinked=1)
    return render(request, 'doublekickApp/UI/home.html',{'userinfo':e})
