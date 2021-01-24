from rest_framework import serializers
from .models import *

# create serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','email','password')

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        exclude = ['is_active', ]

class CounsellorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsellor
        exclude = ['is_active',]

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        exclude = ['is_active',]

