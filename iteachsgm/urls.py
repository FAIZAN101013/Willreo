from django.urls import path
from . import views

urlpatterns = [
    path('/tea/', views.main, name='main'),
    path('/stu/', views.main_stu, name='main_stu'),
    path('upload', views.upload_page, name='upload'),
    path('help/', views.help, name='help'),
    path('profile/', views.profile, name='profile'),
    path('help_stu/', views.help_stu, name='help_stu'),
    path('profile_stu/', views.profile_stu, name='profile_stu')
    ]