from django.contrib import admin
from django.urls import path
from Form import views

urlpatterns = [
    path('', views.homepage),
    path('captcha/',views.captcha),
]