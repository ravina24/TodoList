from django.conf.urls import url
from . import views # . is current folder

urlpatterns = [
    url(r'^$', views.index, name='index')
]