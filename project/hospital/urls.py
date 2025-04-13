from django.urls import path
from .import views

urlpatterns=[
    path('',views.index, name='index'),
    path('appointments/',views.appointments, name='appointments'),
    path('login/',views.login, name='login'),
    path('home/',views.home, name='home'),
    path('registration/',views.registration, name='registration'),
    path('department/', views.department, name='department'),
    path('admindeshboard/',views.admindeshboard, name='admindeshboard'),
    path('doctorReports/',views.doctorReports,name='doctorReports'),
    path('logout/',views.Logout, name='logout'),
    path('doctordeshboard/<int:pk>',views.doctordeshboard, name='doctordeshboard'),
    path('doctorprofile/<int:pk>',views.doctorprofile, name='doctorprofile'),
    path('removedoctor/<int:pk>',views.removedoctor, name='removedoctor'),
    path('patientRegister/',views.patientRegister, name='patientRegister'),



]