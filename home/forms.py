from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


# class SignUpForm(UserCreationForm):
#     full_name = forms.CharField(max_length=255, required=True)
#     phone_number = forms.CharField(max_length=15, required=True)
#     address = forms.CharField(max_length=255, required=True)
#     age = forms.IntegerField(required=True)
#     pin_code = forms.CharField(max_length=10, required=True)

#     class Meta:
#         model = User
#         fields = ['full_name','password', 'phone_number', 'address', 'age', 'pin_code']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.full_name = self.cleaned_data['full_name']
#         user.phone_number = self.cleaned_data['phone_number']
#         user.address = self.cleaned_data['address']
#         user.age = self.cleaned_data['age']
#         user.pin_code = self.cleaned_data['pin_code']

#         if commit:
#             user.save()

#         return user

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Employee_name', 'CategoryID', 'ServiceID', 'Date_of_birth', 'Phone_number', 'Address', 'Age', 'Pin_code']
