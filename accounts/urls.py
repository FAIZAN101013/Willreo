from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Login, name='login1'),
    path('login', views.Login, name='login'),
    path('register', views.Register, name='register'),
    path('logout', views.logout, name="logout")
]