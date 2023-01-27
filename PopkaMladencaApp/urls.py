from django.urls import path

from . import views

urlpatterns = [
    path('/', views.custom_registration),
    path('/check', views.registration),


]