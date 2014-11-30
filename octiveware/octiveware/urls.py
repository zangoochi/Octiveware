from django.conf.urls import patterns, include, url
from django.contrib import admin
import login


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'octiveware.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'octiveware.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('login.urls', namespace="login")),
    url(r'^profile/', include('userprofile.urls', namespace="userprofile")),
    url(r'^(\w+)/$', 'octiveware.views.workFlow'),  
    url(r'^accounts/password-change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^accounts/password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done')
)
