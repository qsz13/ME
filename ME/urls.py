from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from ME import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ME.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', "ME.views.home", name="home"),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include("account.urls")),
    url(r'^story/', include("story.urls")),
    url(r'^friends/', include("friends.urls")),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
