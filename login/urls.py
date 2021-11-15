from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('signupUser', views.signupUser, name='signupUser'),
]