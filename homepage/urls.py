from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Rajasthan/', views.Rajasthan, name='index'),
    path('contactus/',views.contactus,name='contactus'),
    path('package/<int:id>/<int:rid>/',views.openpackage,name='package'),
]