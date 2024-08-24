# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from ehr.models import Appointment, MedicalHistory, MedicalProfessional, Patient, User, VitalSigns

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['username', 'password', 'password', 'first_name', 'last_name', 'date_of_birth', 'gender', 'contact_number', 'address', 'insurance_provider', 'insurance_policy_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))

class MedicalProfessionalRegistrationForm(forms.ModelForm):
    class Meta:
        model = MedicalProfessional
        fields = ['username', 'password', 'password', 'first_name', 'last_name', 'date_of_birth']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))

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
