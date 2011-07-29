from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangomongo.views.home', name='home'),
    # url(r'^djangomongo/', include('djangomongo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    # Index
    (r'^$', 'mysite.views.aindex'),
    # Projects
    (r'^projects/$', 'django.views.generic.simple.direct_to_template', {'template': 'projects.html'}),
    # Contact
    (r'^contacts/$', 'django.views.generic.simple.direct_to_template', {'template': 'contacts.html'}),
    # Django Admin
    (r'^admin/', include(admin.site.urls)),
)
