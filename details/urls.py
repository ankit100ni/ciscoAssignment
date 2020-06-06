from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createdata/', views.createdata, name='createdata'),
]
