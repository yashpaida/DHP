from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    # Uncomment below Only If you want to call index.html page first
    # path('', views.index, name='index'),
    path('', include('homepage.urls')),
    path('home/', include('homepage.urls')),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
]