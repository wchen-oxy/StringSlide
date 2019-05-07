from django.urls import path
from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url("test", views.index, name="test"),
    url("new",views.new, name="new"),
    url("search/", views.search, name="search"),
    path("entries/<int:guitar_id>", views.entry_page, name="entry_page"),


]