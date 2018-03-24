from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('', views.schedule, name="schedule"),
    path('', views.memes, name="memes"),
]
