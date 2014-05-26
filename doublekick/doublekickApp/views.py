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
from math import *
import json


def index(request):
	return render(request, 'doublekickApp/UI/index.html',{});