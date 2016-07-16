from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from myapp.views import (
    MyAppCreate,
    MyAppDelete,
    MyAppDetail,
    MyAppListView,
    MyAppTemplateView,
    MyAppUpdate,
    # home,
	create,
	lista,
	detail,
	update,
    delete,
    )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', MyAppTemplateView.as_view(), name='home'),
    url(r'^create/$', MyAppCreate.as_view(), name='create'),
    url(r'^detail/(?P<pk>\d+)/$', MyAppDetail.as_view(), name='detail'),
    url(r'^detail/(?P<pk>\d+)/update/$', MyAppUpdate.as_view(), name='update'),
    url(r'^detail/(?P<pk>\d+)/delete/$', MyAppDelete.as_view(), name='delete'),
    url(r'^list/$', MyAppListView.as_view(), name='list'),
    # url(r'^create/$', create, name='create'),
    # url(r'^lista/$', lista, name='lista'),
    # url(r'^detail/(?P<pk>\d+)/$', detail, name='detail'),
    # url(r'^detail/(?P<pk>\d+)/edit/$', update, name='update'),
    # url(r'^detail/(?P<pk>\d+)/delete/$', delete, name='delete'),
]