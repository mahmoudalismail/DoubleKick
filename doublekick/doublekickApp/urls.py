from django.conf.urls import patterns, include, url
from doublekickApp import views
from django.contrib.auth import authenticate, login


urlpatterns = patterns('',
    # the index login page 
    url(r'^$', views.index, name='index'),
    url(r'loginForm/$', views.loginForm, name='loginForm'),
    url(r'login/$', views.custom_login, name='login'),
    url(r'signupForm/$', views.signupForm, name='signupForm'),
    url(r'signup/$', views.signup, name='signup'),
    url(r'dashboard/$', views.dashboard, name='dashboard'),
    url(r'newGameForm/$', views.newGameForm, name='newGameForm'),
    url(r'newGame/$', views.newGame, name='newGame'),
    url(r'logout/$', views.logoutUser, name='logout'),
    # decode for loading the logos from the database
	url(r'^decode/(?P<playerID>\d+)/$', views.decode, name='decode'),
	url(r'^decodeField/(?P<fieldID>\d+)/$', views.decodeField, name='decodeField'),
	url(r'^joinGame1/(?P<gameID>\d+)/$', views.joinGame1, name='joinGame1'),
	url(r'^joinGame2/(?P<gameID>\d+)/$', views.joinGame2, name='joinGame2'),
	url(r'teams/$', views.teams, name='teams'),
	url(r'^showGame/(?P<gameID>\d+)/$', views.showGame, name='showGame'),
    # url(r'login/$', views.custom_login, name='login'),
    # url(r'home/$', views.loadHome, name='loadHome'),
    # url(r'quest/$', views.loadQuest, name='loadQuest'),
    # url(r'ranking/$', views.loadRanking, name='loadRanking'),
    # url(r'createquiz/$', views.loadCreate, name='loadCreate'),
    # url(r'searchquiz/$', views.loadSearch, name='loadSearch'),
    # url(r'friends/$', views.friends, name='friends'),
    # url(r'getCoordinates/(?P<coords>.+)/$', views.getCoordinates, name='getCoordinates'),
    # url(r'/$', views.testing, name='testing'),
    )