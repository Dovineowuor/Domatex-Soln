# urls.py
from django.urls import path
from django.views.generic.base import TemplateView
from .views import home, logout, medical_professional_home, patient_home, patient_profile, register_patient, register_medical_professional, medical_professional_profile, book_appointment, add_medical_history, add_vital_signs, custom_login

urlpatterns = [
    path('register/patient/', register_patient, name='register_patient'),
    path('register/medical-professional/', register_medical_professional, name='register_medical_professional'),
    path('register/patient/success/', TemplateView.as_view(template_name="registration/patient_success.html"), name='patient_success'),
    path('register/medical-professional/success/', TemplateView.as_view(template_name="registration/medical_professional_success.html"), name='medical_professional_success'),
    path('home/', home, name='home'),
    path('patient/home/', patient_home, name='patient_home'),
    path('medical-professional/home/', medical_professional_home, name='medical_professional_home'),
    path('logout/', logout, name='logout'),
    path('patient/profile/', patient_profile, name='patient_profile'),
    path('medical-professional/profile/', medical_professional_profile, name='medical_professional_profile'),
    path('book-appointment/', book_appointment, name='book_appointment'),
    path('add-medical-history/', add_medical_history, name='add_medical_history'),
    path('add-vital-signs/', add_vital_signs, name='add_vital_signs'),
    path('accounts/login/', custom_login, name='login'),  # Custom login view
]