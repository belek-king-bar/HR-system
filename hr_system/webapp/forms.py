from django import forms
from webapp.models import EmployeeData


class EmployeeDataForm(forms.ModelForm):
    class Meta:
        model = EmployeeData
        exclude = ['employee', 'corporate_email', 'is_active', 'is_confirmed', 'is_fired', 'is_manager']
