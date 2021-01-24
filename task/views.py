from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView ,RetrieveAPIView
from rest_framework.response import Response
from django.db.models import F
from .serializers import *
from django.contrib.auth.hashers import make_password

# Create your views here.
class PatientView(ListCreateAPIView):
    queryset = Patient.objects.filter(is_active ='active')
    serializer_class = PatientSerializer

    def post(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid(raise_exception=True):
            user =  user_serializer.save()
            request.data['user'] = user.pk
            response = self.create(request, *args, **kwargs)
            return  response

    def get(self, request, *args, **kwargs):
        patient_queryset = Patient.objects.filter(is_active ='active')
        if patient_queryset.exists():
            patient_queryset = patient_queryset.values(id=F('user_id'),name=F('user__name') ,email=F('user__email'))
            return Response(patient_queryset)
        else:
            return Response({"error": "patient not found"})

class PatientDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.filter(is_active ='active')
    serializer_class = PatientSerializer

    def get(self, request,pk, *args, **kwargs):
        patient_queryset = Patient.objects.filter(is_active ='active',user_id= pk)
        if patient_queryset.exists():
            patient_queryset = patient_queryset.values(id=F('user_id'),name=F('user__name') ,email=F('user__email'))
            return Response(patient_queryset)
        else:
            return Response({"error": "patient not found"})

class CounsellorView(ListCreateAPIView):
    queryset = Counsellor.objects.filter(is_active ='active')
    serializer_class = CounsellorSerializer

    def post(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
            request.data['user'] = user.pk
            response = self.create(request, *args, **kwargs)
            return response

    def get(self, request, *args, **kwargs):
        patient_queryset = Counsellor.objects.filter(is_active='active')
        if patient_queryset.exists():
            patient_queryset = patient_queryset.values(id=F('user_id'), name=F('user__name'), email=F('user__email'))
            return Response(patient_queryset)
        else:
            return Response({"error": "patient not found"})

class CounsellorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Counsellor.objects.filter(is_active ='active')
    serializer_class = CounsellorSerializer

    def get(self, request,pk, *args, **kwargs):
        counsellor_queryset = Counsellor.objects.filter(is_active ='active',user_id= pk)
        if counsellor_queryset.exists():
            counsellor_queryset = counsellor_queryset.values(id=F('user_id'),name=F('user__name') ,email=F('user__email'))
            return Response(counsellor_queryset)
        else:
            return Response({"error": "counsellor not found"})

class AppointmentView(ListCreateAPIView):
    queryset = Appointment.objects.filter(is_active ='active')
    serializer_class = AppointmentSerializer

class AppointmentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.filter(is_active ='active')
    serializer_class = AppointmentSerializer

class PatientAppointmentDetailView(RetrieveAPIView):
    queryset =  Appointment.objects.filter(is_active ='active')
    serializer_class = AppointmentSerializer

    def get(self, request,patient_id, *args, **kwargs):

        patient_appointments = Appointment.objects.filter(is_active ='active',patient_id = patient_id).values()
        if patient_appointments.exists():
            return Response(patient_appointments)
        else:
            return Response({'error':'record not found'})

class CounsellorAppointmentDetailView(RetrieveAPIView):
    queryset =  Appointment.objects.filter(is_active ='active')
    serializer_class = AppointmentSerializer

    def get(self, request,counsellor_id, *args, **kwargs):

        counsellor_appointments = Appointment.objects.filter(is_active ='active',counsellor_id = counsellor_id).values()
        if counsellor_appointments.exists():
            return Response(counsellor_appointments)
        else:
            return Response({'error':'record not found'})

class AppointmentDetailByDateView(RetrieveAPIView):
    queryset =  Appointment.objects.filter(is_active ='active')
    serializer_class = AppointmentSerializer

    def get(self, request, *args, **kwargs):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        counsellor_appointments = Appointment.objects.filter(is_active ='active',appointment_date__gte=start_date,appointment_date__lte=end_date).order_by('-appointment_date') #, appointment_date__lte=request.GET.get('start_date'), appointment_date__gt=request.GET.get('end_date')).values().order_by('-appointment_date')
        if counsellor_appointments.exists():
            return Response(counsellor_appointments.values())
        else:
            return Response({'error':'record not found'})


