from django import forms
from .models import User
from .models import Employee
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'username', 'password', 'phone_number', 'address', 'age', 'pin_code']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Employee_name', 'CategoryID', 'ServiceID', 'Date_of_birth', 'Phone_number', 'Address', 'Age', 'Pin_code']
