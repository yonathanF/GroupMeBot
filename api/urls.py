from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^', views.index, name="index"),
    url(r'^schedule', views.schedule, name="schedule"),
    url(r'^memes', views.memes, name="memes"),
    url(r'^callback', views.callback, name="calback"),
]
