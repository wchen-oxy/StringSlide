from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url("entries/", views.entry_page, name="entry"),


]