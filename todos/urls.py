from django.conf.urls import url
from . import views # . is current folder
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details),
    url(r'^add', views.add, name='add'),
    url(r'^details/(?P<id>\w{0,50})/edit/$', views.edit, name='edit'),
    url(r'^details/(?P<id>\w{0,50})/delete/$', views.delete, name='delete'),
]

urlpatterns += staticfiles_urlpatterns() # to load css