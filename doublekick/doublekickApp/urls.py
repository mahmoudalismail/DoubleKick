from django.conf.urls import patterns, include, url
from doublekickApp import views
from django.contrib.auth import authenticate, login


urlpatterns = patterns('',
    # the index login page 
    url(r'^$', views.index, name='index')#,
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