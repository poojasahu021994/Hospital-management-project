from django.urls import path
from .import views

urlpatterns=[
    path('',views.index, name='index'),
    path('apponimant',views.apponimant, name='apponimant'),
    path('login',views.login, name='login'),
    path('home',views.home, name='home'),
    path('registration',views.registration, name='registration'),

]