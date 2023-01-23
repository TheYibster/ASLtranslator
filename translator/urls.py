from django.contrib import admin
from django.urls import path, include
from translator import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("pogtranslator/", views.livecam, name = "livecam"),
    
]