from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    # Uncomment below Only If you want to call index.html page first
    # path('', views.index, name='index'),
    path('', include(('homepage.urls','home'),namespace='home')),
    path('home/', include(('homepage.urls','home'),namespace='home')),
    path('login/', include('login.urls')),
    path('manageUsers/', include('manageUsers.urls')),
    path('manageDestinations/',include('manageDestinations.urls')),
    path('manageResorts/',include('manageResorts.urls')),
    path('admin/', admin.site.urls),
]