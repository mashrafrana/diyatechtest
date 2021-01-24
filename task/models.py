from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class BaseModel(models.Model):
    is_active = models.CharField(max_length=50 , default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self):
        self.is_active = 'inactive'
        self.save()

    def restore(self):
        self.is_active = 'active'
        self.save()

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100 , validators=[MinLengthValidator(8)])

    class Meta:
        db_table = 'User'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name

class Patient(BaseModel,models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE,primary_key=True , related_name='patient_user')

    class Meta:
        db_table = 'patient'
        verbose_name = 'patient'
        verbose_name_plural = 'patients'

class Counsellor(BaseModel,models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE,primary_key=True ,related_name='counsellor_user')

    class Meta:
        db_table = 'counsellor'
        verbose_name = 'counsellor'
        verbose_name_plural = 'counsellors'

class Appointment(BaseModel,models.Model):
    patient = models.ForeignKey(Patient , on_delete=models.CASCADE ,related_name='appointment_patient')
    counsellor = models.ForeignKey(Counsellor , on_delete=models.CASCADE , related_name='appointment_counsellor')
    appointment_date = models.DateTimeField()

    def __str__(self):
        return  str(self.patient.user.name) + str(self.counsellor.user.name)

    class Meta:
        db_table = 'appointment'
        verbose_name = 'appointment'
        verbose_name_plural = 'appointments'
        unique_together = (('patient', 'counsellor', 'appointment_date'),)
