from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
	 url(r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': 'static'}
  ),
    

    url(r'^$', 'login.views.userlogin'),
	url(r'^logout$', 'login.views.user_logout'),
    url(r'^welcome/$', 'login.views.welcome'),
	url(r'^view_film$', 'film.views.view_film'),
    url(r'^admin/', include(admin.site.urls)),
   	
	url(r'^selectedfilm','film.views.selected_film'),
	url(r'^buyticket','film.views.get_ticket'),
	
	
)

if settings.DEBUG:
    urlpatterns += patterns('',url(r'^film_images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),)
