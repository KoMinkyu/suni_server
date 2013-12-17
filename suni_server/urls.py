from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('suni_server.restapi.urls', namespace="suni_api")),
    url(r'^docs/', include('rest_framework_swagger.urls', namespace="swagger")),
    # Examples:
    # url(r'^$', 'suni_server.views.home', name='home'),
    # url(r'^suni_server/', include('suni_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
