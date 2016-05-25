from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView


from myapp.views import (
    home,
	create,
	lista,
	detail,
	update,
    delete,
    )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', home, name='home'),
    url(r'^create/$', create, name='create'),
    url(r'^lista/$', lista, name='lista'),
    url(r'^detail/(?P<pk>\d+)/$', detail, name='detail'),
    url(r'^detail/(?P<pk>\d+)/edit/$', update, name='update'),
    url(r'^detail/(?P<pk>\d+)/delete/$', delete, name='delete'),
]