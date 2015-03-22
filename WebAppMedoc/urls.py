"""
Definition of urls for WebAppMedoc.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about$', 'app.views.about', name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^head$', 'app.views._head', name='head'),
    url(r'^medoc$', 'app.views.medoc', name='medoc'),
	url(r'^en', 'app.views._en', name='en'),
	url(r'^kr', 'app.views._kr', name='kr'),
	url(r'^fr', 'app.views._fr', name='fr'),
    url(r'^medoc_kr$', 'app.views.medoc_kr', name='medoc_kr'),
    url(r'^head_kr$', 'app.views.head_kr', name='head_kr'),
    url(r'^contact_kr$', 'app.views.contact_kr', name='contact_kr'),
    url(r'^about_kr$', 'app.views.about_kr', name='about_kr'),
    url(r'^medoc_fr$', 'app.views.medoc_fr', name='medoc_fr'),
    url(r'^head_fr$', 'app.views.head_fr', name='head_fr'),
    url(r'^contact_fr$', 'app.views.contact_fr', name='contact_fr'),
    url(r'^about_fr$', 'app.views.about_fr', name='about_fr'),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
