# registration/urls.py

from django.urls import path
from . import views

urlpatterns = [
      path('welcome/', views.welcome, name='welcome'),
    # path('register/', views.register, name='register'),
    path('', views.welcome, name='welcome')


]
