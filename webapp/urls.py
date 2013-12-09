from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
import api

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^chart', views.chart_test),
    url(r'^api/', include(api.urls)),
    url(r'^.*', views.index)
)
