from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from hello.views import DashView
import hello.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello.views.DashView.as_view()),
    url(r'^admin/', include(admin.site.urls)),

)
