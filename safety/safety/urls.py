from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
	url(r'^debug/(?P<place>[A-Za-z]+)$', 'gamecompare.views.debug', name='debug'),
	url(r'^$', 'gamecompare.views.home', name='home'),	
    # Examples:
    # url(r'^$', 'safety.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
