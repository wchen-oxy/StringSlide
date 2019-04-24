from django.urls import path
from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    path("entries/<int:guitar_id>", views.entry_page, name="entry_page"),


]