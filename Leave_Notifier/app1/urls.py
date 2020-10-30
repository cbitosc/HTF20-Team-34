from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
   path('', views.login, name="login")
]