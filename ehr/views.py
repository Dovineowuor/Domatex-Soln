from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import AppointmentForm, MedicalHistoryForm, PatientRegistrationForm, MedicalProfessionalRegistrationForm, VitalSignsForm
from .models import Patient, MedicalProfessional

def register_patient(request):
    if request.method == 'POST':
        user_form = PatientRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_patient = True
            user.save()
            Patient.objects.create(
                user=user,
                first_name=user_form.cleaned_data.get('first_name'),
                last_name=user_form.cleaned_data.get('last_name'),
                date_of_birth=user_form.cleaned_data.get('date_of_birth'),
                gender=user_form.cleaned_data.get('gender'),
                contact_number=user_form.cleaned_data.get('contact_number'),
                address=user_form.cleaned_data.get('address'),
                insurance_provider=user_form.cleaned_data.get('insurance_provider'),
                insurance_policy_number=user_form.cleaned_data.get('insurance_policy_number')
            )
            login(request, user)
            return redirect('patient_success')
    else:
        user_form = PatientRegistrationForm()
    return render(request, 'registration/register_patient.html', {'form': user_form})

def register_medical_professional(request):
    if request.method == 'POST':
        user_form = MedicalProfessionalRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_medical_professional = True
            user.save()
            MedicalProfessional.objects.create(
                user=user,
                first_name=user_form.cleaned_data.get('first_name'),
                last_name=user_form.cleaned_data.get('last_name'),
                specialization=user_form.cleaned_data.get('specialization'),
                contact_number=user_form.cleaned_data.get('contact_number')
            )
            login(request, user)
            return redirect('medical_professional_success')
    else:
        user_form = MedicalProfessionalRegistrationForm()
    return render(request, 'registration/register_medical_professional.html', {'form': user_form})



def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})

def add_medical_history(request):
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page
    else:
        form = MedicalHistoryForm()
    return render(request, 'medical_history/add_medical_history.html', {'form': form})

def add_vital_signs(request):
    if request.method == 'POST':
        form = VitalSignsForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page
    else:
        form = VitalSignsForm()
    return render(request, 'vital_signs/add_vital_signs.html', {'form': form})

def patient_success(request):
    return render(request, 'registration/patient_success.html')

def medical_professional_success(request):
    return render(request, 'registration/medical_professional_success.html')

def home(request):
    return render(request, 'home.html')

def patient_home(request):
    return render(request, 'patient_home.html')

def medical_professional_home(request):
    return render(request, 'medical_professional_home.html')

def login(request):
    return render(request, 'registration/login.html')

def logout(request):
    return render(request, 'registration/logout.html')

def register(request):
    return render(request, 'registration/register.html')

def patient_profile(request):
    return render(request, 'patient_profile.html')

def medical_professional_profile(request):
    return render(request, 'medical_professional_profile.html')

def appointments(request):
    return render(request, 'appointments.html')
