from django.contrib import admin
from .models import *


# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_filter = ("user__name", "user__email")
    display_list = ("user__name", "user__email")

class CounsellorAdmin(admin.ModelAdmin):
    list_filter = ("user__name", "user__email")

class AppointmentAdmin(admin.ModelAdmin):
    list_filter = ("patient__user", "counsellor__user","appointment_date")

admin.site.register(Patient,PatientAdmin)
admin.site.register(Counsellor,CounsellorAdmin)
admin.site.register(Appointment,AppointmentAdmin)
