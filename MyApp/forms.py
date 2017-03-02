from django import forms
from MyApp.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('employee_number', 'name', 'age', 'email', 'phone_number', 'photo')