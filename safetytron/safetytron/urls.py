from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/?$', 'safety.views.home_page', name='home'),
    
    # ajax apis
    url(r'^api/update/?$', 'safety.views.update_on_click', name='update click'),
)
