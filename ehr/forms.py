# forms.py
from datetime import date
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from ehr.models import Appointment, MedicalHistory, MedicalProfessional, Patient, User, VitalSigns
from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.layout import Submit

class PatientRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Date of birth',
        error_messages={'invalid': 'Enter a valid date.'})
    gender = forms.CharField(max_length=10)
    contact_number = forms.CharField(max_length=20)
    email_address = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    insurance_provider = forms.CharField(max_length=255)
    insurance_policy_number = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birth', 'gender', 'contact_number', 'email_address', 'address', 'insurance_provider', 'insurance_policy_number']

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        if dob > date.today():
            raise forms.ValidationError('Date of birth cannot be in the future.')
        return dob
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
            patient = Patient(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                date_of_birth=self.cleaned_data['date_of_birth'],
                gender=self.cleaned_data['gender'],
                contact_number=self.cleaned_data['contact_number'],
                email_address=self.cleaned_data['email_address'],
                address=self.cleaned_data['address'],
                insurance_provider=self.cleaned_data['insurance_provider'],
                insurance_policy_number=self.cleaned_data['insurance_policy_number']
            )
            patient.save()
        return user

class MedicalProfessionalRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    specialization = forms.CharField(max_length=255)
    contact_number = forms.CharField(max_length=20)
    email_address = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'specialization', 'contact_number', 'email_address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_medical_professional = True
        if commit:
            user.save()
            medical_professional = MedicalProfessional(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                specialization=self.cleaned_data['specialization'],
                contact_number=self.cleaned_data['contact_number'],
                email_address=self.cleaned_data['email_address']
            )
            medical_professional.save()
        return user

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'medical_professional', 'date', 'time', 'purpose']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = ['patient', 'diagnosis', 'allergies']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

class VitalSignsForm(forms.ModelForm):
    class Meta:
        model = VitalSigns
        fields = ['patient', 'date', 'time', 'blood_pressure']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login'))

class PatientSearchForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    date_of_birth = forms.DateField(required=False)
    diagnosis = forms.CharField(required=False)
    allergies = forms.CharField(required=False)
    chronic_conditions = forms.CharField(required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.add_input(Submit('submit', 'Search'))

class MedicalProfessionalSearchForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    specialization = forms.CharField(required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.add_input(Submit('submit', 'Search'))

class AppointmentSearchForm(forms.Form):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), required=False)
    medical_professional = forms.ModelChoiceField(queryset=MedicalProfessional.objects.all(), required=False)
    date = forms.DateField(required=False)
    purpose = forms.CharField(required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.add_input(Submit('submit', 'Search'))

class MedicalHistorySearchForm(forms.Form):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), required=False)
    diagnosis = forms.CharField(required=False)
    allergies = forms.CharField(required=False)
    chronic_conditions = forms.CharField(required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.add_input(Submit('submit', 'Search'))

class VitalSignsSearchForm(forms.Form):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), required=False)
    date = forms.DateField(required=False)
    time = forms.TimeField(required=False)
    blood_pressure = forms.CharField(required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.add_input(Submit('submit', 'Search'))

class UserSearchForm(forms.Form):
    username = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    date_of_birth = forms.DateField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.add_input(Submit('submit', 'Search'))

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

class MedicalProfessionalUpdateForm(forms.ModelForm):
    class Meta:
        model = MedicalProfessional
        fields = ['first_name', 'last_name', 'specialization', 'contact_number', 'email_address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'purpose']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        
class MedicalHistoryUpdateForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = ['diagnosis', 'allergies', 'chronic_conditions']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

class VitalSignsUpdateForm(forms.ModelForm):
    class Meta:
        model = VitalSigns
        fields = ['date', 'time', 'blood_pressure']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
