from django.conf.urls import patterns, include, url
from doublekickApp import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'doublekick.views.home', name='home'),
    # url(r'^doublekick/', include('doublekick.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('doublekickApp.urls'))
)


from django.contrib import admin
admin.autodiscover()

urlpatterns += patterns('', url(r'^admin/', include(admin.site.urls)))