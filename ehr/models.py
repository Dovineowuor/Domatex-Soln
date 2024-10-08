from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_medical_professional = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='ehr_user_set',
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=_('groups'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='ehr_user_set',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions'),
    )

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='patient', related_query_name='patient', verbose_name=_('user'), help_text=_('The user that this patient profile belongs to.'), default=None)
    first_name = models.CharField(_('first name'), max_length=255)
    last_name = models.CharField(_('last name'), max_length=255)
    date_of_birth = models.DateField(_('date of birth'))
    gender = models.CharField(_('gender'), max_length=10)
    contact_number = models.CharField(_('contact number'), max_length=20)
    email_address = models.EmailField(_('email address'))
    address = models.TextField(_('address'))
    insurance_provider = models.CharField(_('insurance provider'), max_length=255)
    insurance_policy_number = models.CharField(_('insurance policy number'), max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MedicalProfessional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='medical_professional', related_query_name='medical_professional', verbose_name=_('user'), help_text=_('The user that this medical professional profile belongs to.'), default=None)
    first_name = models.CharField(_('first name'), max_length=255)
    last_name = models.CharField(_('last name'), max_length=255)
    specialization = models.CharField(_('specialization'), max_length=255)
    contact_number = models.CharField(_('contact number'), max_length=20)
    email_address = models.EmailField(_('email address'))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medical_professional = models.ForeignKey(MedicalProfessional, on_delete=models.CASCADE)
    date = models.DateField(_('date'))
    time = models.TimeField(_('time'))
    purpose = models.TextField(_('purpose'))

    def __str__(self):
        return f"Appointment for {self.patient} on {self.date} at {self.time}"

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.TextField(_('diagnosis'))
    allergies = models.TextField(_('allergies'))
    chronic_conditions = models.TextField(_('chronic conditions'))

    def __str__(self):
        return f"Medical History for {self.patient}"

class VitalSigns(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(_('date'))
    time = models.TimeField(_('time'))
    blood_pressure = models.CharField(_('blood pressure'), max_length=20)
    heart_rate = models.PositiveIntegerField(_('heart rate'))
    temperature = models.DecimalField(_('temperature'), max_digits=5, decimal_places=2)
    weight = models.DecimalField(_('weight'), max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Vital Signs for {self.patient} on {self.date} at {self.time}"

class LabResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(_('test name'), max_length=255)
    test_result = models.CharField(_('test result'), max_length=255)
    date = models.DateField(_('date'))
    lab_technician = models.CharField(_('lab technician'), max_length=255)

    def __str__(self):
        return f"Lab Result for {self.patient} - {self.test_name}"

class MedicalImage(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    image = models.ImageField(_('image'), upload_to='medical_images/')
    description = models.TextField(_('description'))
    date = models.DateField(_('date'))
    uploaded_by = models.CharField(_('uploaded by'), max_length=255)

    def __str__(self):
        return f"Medical Image for {self.patient} - {self.date}"