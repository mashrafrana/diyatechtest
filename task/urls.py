"""taskapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('patients/',PatientView.as_view() ,name='patients'),
    path('patients/<int:pk>/' ,PatientDetailView.as_view() ,name='patient_details'),
    path('consellors/', CounsellorView.as_view(), name='consollors'),
    path('consellors/<int:pk>/', CounsellorDetailView.as_view(), name='consollors_details'),
    path('appointment/', AppointmentView.as_view(), name='appointments'),
    path('appointment/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_details'),
    path('patients/<int:patient_id>/appointments/', PatientAppointmentDetailView.as_view(), name='patient_appointments'),
    path('consellors/<int:counsellor_id>/appointments/', CounsellorAppointmentDetailView.as_view(), name='consellor_details'),
    path('appointments-report/', AppointmentDetailByDateView.as_view(),name='appointments_details'),

]





