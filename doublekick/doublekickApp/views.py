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

from doublekickApp.models import *
# from django.db import models
# from math import *
import json
import string

def index(request):
	return render(request, 'doublekickApp/UI/design/newindex/index.html',{});

def signupForm(request):
	
	return render(request,'doublekickApp/UI/design/signup.html',{});

def signup(request):
	firstName = request.POST['firstName']
	username = request.POST['username']
	user = User.objects.create_user(username, "",request.POST['password'])

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
					passing=0,
					upcomingGames=""
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
    print "user---->", user
    if user is not None:
    	if user.is_active:
    		login(request, user)
    		return HttpResponseRedirect(reverse('doublekickApp.views.dashboard',))
    #     else:
    #         # Return a 'disabled account' error message
    else:
    	print "user is none"
    #     # Return an 'invalid login' error message.

# load the home once the user is logged in
@login_required(login_url='/app/loginForm')
def loadHome(request):
    e = Member.objects.get(userLinked=1)
    return render(request, 'doublekickApp/UI/home.html',{'userinfo':e})

@login_required(login_url='/app/loginForm/')
def dashboard(request):
	# get the current signed in user
	print request.user
	player = Player.objects.get(playerInfo = request.user)
	# get the user's upcoming games
	upcomingMatches = player.upcomingGames.split(",")
	print "upcomingMatches---->", upcomingMatches
	
	################
	# very stupid code
	##################
	# not empty lists
	for i in upcomingMatches:
		if i == '':
			upcomingMatches.remove(i)

	# convert them to numbers
	for i in range(0, len(upcomingMatches)):
		if upcomingMatches[i] == '':
			print "EMPTY"
			upcomingMatches.remove(upcomingMatches[i])
		else:
			print "HERE=====>", upcomingMatches[i]
			upcomingMatches[i] = int(upcomingMatches[i])
	
	#####################

	# filter all the games
	# print "finished parsing========\n\n\n\n\n\n"
	# print upcomingMatches
	games = Game.objects.filter(pk__in=upcomingMatches)

	# print "HERERERER", games[0].field.fieldName

	players = Player.objects.all()
	avalgames = Game.objects.all()
	return render(request, 'doublekickApp/UI/design/dashboard.html',{'games': games, 'players': players,'avalgames': avalgames});

@login_required(login_url='/app/loginForm/')
def newGameForm(request):
	return render(request, 'doublekickApp/UI/design/new-game.html',{});

@login_required(login_url='/app/loginForm/')
def logoutUser(request):
	logout(request)
	return HttpResponseRedirect(reverse('doublekickApp.views.index',))

@login_required(login_url='/app/loginForm/')
def newGame(request):
	# get the field number
	fieldID = request.GET['field']
	

	# create a new game
	# teams format => userID, teamNumber,
	# teamDate format => time|date
	game = Game(teams=str(request.user.id)+",1",
				field=Field.objects.get(id=fieldID),
				timeDate=request.GET['time']+"|"+request.GET['date'],
				gameFinished=False)
	game.save()

	#fix the user's profile
	
	# upcomingGames format => idOfGames, idOfGames

	player = Player.objects.get(playerInfo=request.user)
	
	if player.upcomingGames == None:
		player.upcomingGames = game.id
	else:
		player.upcomingGames = player.upcomingGames+","+str(game.id)
	
	player.save()

	return HttpResponseRedirect(reverse('doublekickApp.views.dashboard',))

@login_required(login_url='/app/login/')
# get the profile image for the players
def decode(request, playerID):
	print "DECODING THE IMAGE ========> "
	player = Player.objects.get(id = playerID)
	# , mimetype=loggedInClub.mime_type
	# no mime_type is being saved because the image is saved through the admin page
	return HttpResponse(player.profileImg.read())

@login_required(login_url='/app/login/')
def decodeField(request, fieldID):
	print "DECODING THE IMAGE ========> "
	field = Field.objects.get(id = fieldID)
	# , mimetype=loggedInClub.mime_type
	# no mime_type is being saved because the image is saved through the admin page
	return HttpResponse(field.fieldImage.read())

@login_required(login_url='/app/login/')
def joinGame1(request, gameID):
	player = Player.objects.get(playerInfo=request.user)
	game = Game.objects.get(id=gameID)

	player.upcomingGames = player.upcomingGames+","+gameID
	game.teams = game.teams + ","+ str(request.user.id) + "," + "1"
	player.save()
	game.save()

@login_required(login_url='/app/login/')
def joinGame2(request, gameID):
	player = Player.objects.get(playerInfo=request.user)
	game = Game.objects.get(id=gameID)

	player.upcomingGames = player.upcomingGames+","+gameID
	game.teams = Game.teams + ","+ str(request.user.id) + "," + "2"
	
	player.save()
	game.save()

@login_required(login_url='/app/login/')
def teams(request):
	return render(request, 'doublekickApp/UI/design/teams.html',{});
